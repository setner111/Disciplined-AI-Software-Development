<img src="https://banes-lab.com/assets/images/banes_lab/700px_Main_Animated.gif" width="70" />

## 📂 Folder: src\api - Current Tree Structure
```
📂 api
├─ 🔄 middleware.js (36 lines)
├─ 🛣️ routes.js (86 lines)
└─ 📜 server.js (85 lines)
```

## 📄 Project File Contents


=== File: src\api\middleware.js (36 lines) ===

```javascript
function authenticate(req, res, next) {
    const token = req.headers.authorization?.replace('Bearer ', '');
    const validToken = process.env.API_TOKEN;
    
    if (!validToken) {
        return res.status(500).json({ error: 'API not configured' });
    }
    
    if (!token || token !== validToken) {
        return res.status(401).json({ error: 'Unauthorized' });
    }
    
    next();
}

function validateGuildId(req, res, next) {
    const { guildId } = req.params;
    
    if (!guildId || !/^\d+$/.test(guildId)) {
        return res.status(400).json({ error: 'Invalid guild ID' });
    }
    
    next();
}

function handleAsync(fn) {
    return (req, res, next) => {
        Promise.resolve(fn(req, res, next)).catch(next);
    };
}

module.exports = {
    authenticate,
    validateGuildId,
    handleAsync
};
```

=== File: src\api\routes.js (86 lines) ===

```javascript
const express = require('express');
const { queryAuditLogs, getAuditStats } = require('../handlers/audit');
const { select } = require('../data');
const { DATABASE_TABLES } = require('../core/constants');
const { getLoadedPlugins } = require('../handlers/command');
const { validateGuildId, handleAsync } = require('./middleware');

const router = express.Router();

router.get('/stats', handleAsync(async (req, res) => {
    const plugins = getLoadedPlugins();
    const stats = {
        plugins: {
            commands: plugins.commands?.length || 0,
            slash: plugins.slash?.length || 0,
            messages: plugins.messages?.length || 0,
            interactions: plugins.interactions?.length || 0
        },
        uptime: process.uptime(),
        memory: process.memoryUsage()
    };
    res.json(stats);
}));

router.get('/servers', handleAsync(async (req, res) => {
    const servers = await select(DATABASE_TABLES.SERVERS);
    const serverList = Array.isArray(servers) ? servers : (servers ? [servers] : []);
    
    const response = serverList.map(server => ({
        guild_id: server.guild_id,
        created_at: server.created_at,
        updated_at: server.updated_at
    }));
    
    res.json(response);
}));

router.get('/servers/:guildId/config', validateGuildId, handleAsync(async (req, res) => {
    const { guildId } = req.params;
    const server = await select(DATABASE_TABLES.SERVERS, { guild_id: guildId });
    
    if (!server) {
        return res.status(404).json({ error: 'Server not found' });
    }
    
    const config = JSON.parse(server.config || '{}');
    res.json(config);
}));

router.get('/servers/:guildId/audit', validateGuildId, handleAsync(async (req, res) => {
    const { guildId } = req.params;
    const { limit = 50, action, userId } = req.query;
    
    const filters = { limit: parseInt(limit) };
    if (action) filters.action = action;
    if (userId) filters.userId = userId;
    
    const logs = await queryAuditLogs(guildId, filters);
    res.json(logs);
}));

router.get('/servers/:guildId/stats', validateGuildId, handleAsync(async (req, res) => {
    const { guildId } = req.params;
    const stats = await getAuditStats(guildId);
    res.json(stats);
}));

router.put('/servers/:guildId/config', validateGuildId, handleAsync(async (req, res) => {
    const { guildId } = req.params;
    const newConfig = req.body;
    
    if (!newConfig || typeof newConfig !== 'object') {
        return res.status(400).json({ error: 'Invalid config data' });
    }
    
    const { insert } = require('../data');
    await insert(DATABASE_TABLES.SERVERS, {
        guild_id: guildId,
        config: JSON.stringify(newConfig),
        updated_at: new Date().toISOString()
    });
    
    res.json({ message: 'Config updated successfully' });
}));

module.exports = router;
```

=== File: src\api\server.js (85 lines) ===

```javascript
const express = require('express');
const cors = require('cors');
const rateLimit = require('express-rate-limit');
const config = require('../core/config');
const routes = require('./routes');
const middleware = require('./middleware');

let server = null;

function createApiServer() {
    const app = express();
    
    app.use(cors({
        origin: process.env.CORS_ORIGIN || '*',
        methods: ['GET', 'POST', 'PUT', 'DELETE'],
        allowedHeaders: ['Content-Type', 'Authorization']
    }));
    
    app.use(express.json({ limit: '10mb' }));
    
    const limiter = rateLimit({
        windowMs: 15 * 60 * 1000,
        max: 100,
        message: { error: 'Too many requests' }
    });
    app.use(limiter);
    
    app.use(middleware.authenticate);
    
    app.use('/api', routes);
    
    app.get('/health', (req, res) => {
        res.json({ status: 'ok', timestamp: new Date().toISOString() });
    });
    
    app.use((req, res) => {
        res.status(404).json({ error: 'Endpoint not found' });
    });
    
    app.use((error, req, res, next) => {
        console.error('API Error:', error);
        res.status(500).json({ error: 'Internal server error' });
    });
    
    return app;
}

function startApiServer() {
    if (!config.api.enabled || server) return null;
    
    const app = createApiServer();
    
    return new Promise((resolve, reject) => {
        server = app.listen(config.api.port, (err) => {
            if (err) {
                reject(err);
                return;
            }
            console.log(`API server running on port ${config.api.port}`);
            resolve(server);
        });
        
        server.setTimeout(config.api.timeout);
    });
}

function stopApiServer() {
    return new Promise((resolve) => {
        if (server) {
            server.close(() => {
                server = null;
                console.log('API server stopped');
                resolve();
            });
        } else {
            resolve();
        }
    });
}

module.exports = {
    startApiServer,
    stopApiServer,
    isRunning: () => server !== null
};
```
