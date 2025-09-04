<img src="https://banes-lab.com/assets/images/banes_lab/700px_Main_Animated.gif" width="70" />

## 📂 The Project - Current Tree Structure
```
📂 src
├─ 🏠 main.js (16 lines)
├─ 📂 api
│   ├─ 🔄 middleware.js (36 lines)
│   ├─ 🛣️ routes.js (86 lines)
│   └─ 📜 server.js (85 lines)
├─ 📂 core
│   ├─ 📜 client.js (49 lines)
│   ├─ ⚙️ config.js (61 lines)
│   ├─ 🔢 constants.js (116 lines)
│   └─ 📜 shutdown.js (40 lines)
├─ 📂 data
│   ├─ 📊 database.js (68 lines)
│   ├─ 🤝 helpers.js (56 lines)
│   ├─ 📇 index.js (19 lines)
│   ├─ 📜 operations.js (95 lines)
│   └─ 📋 schemas.sql (51 lines)
├─ 📂 handlers
│   ├─ 📋 audit.js (115 lines)
│   ├─ 📜 command.js (98 lines)
│   ├─ 🎬 interaction.js (118 lines)
│   ├─ 📜 message.js (132 lines)
│   └─ 📜 slash.js (126 lines)
├─ 📂 plugins
│   ├─ 📂 commands
│   │   └─ 📜 ping.js (15 lines)
│   ├─ 📂 interactions
│   │   └─ 📜 button.js (24 lines)
│   ├─ 📂 messages
│   │   └─ 📜 welcome.js (14 lines)
│   └─ 📂 slash
│       └─ 📜 info.js (20 lines)
├─ 📂 security
│   ├─ 🔒 permissions.js (110 lines)
│   └─ 📜 ratelimit.js (143 lines) ⚠️
└─ 📂 utils
    ├─ 📜 docs-generator.js (140 lines) ⚠️
    ├─ 📝 logger.js (87 lines)
    └─ 📂 docs
        ├─ 📜 analyzer.js (66 lines)
        ├─ 📜 ast-parser.js (100 lines)
        ├─ 📜 file-scanner.js (40 lines)
        ├─ 📦 module-parser.js (110 lines)
        ├─ 📘 readme-generator.js (150 lines) ⚠️
        └─ 📜 writer.js (48 lines)
📂 tests
├─ ⚡ benchmark.js (138 lines)
├─ 📜 check-regressions.js (117 lines)
├─ 📜 result-paths.js (19 lines)
├─ ⚡ run-benchmarks.js (32 lines)
├─ 🧪 run-stress-tests.js (48 lines)
├─ 📜 stress.js (108 lines)
├─ 📂 data
│   ├─ 🔧 baseline.json (197 lines)
│   ├─ 🔧 pr-baseline.json (197 lines)
│   ├─ 🔧 pr-results.json (0 lines)
│   ├─ 🔧 results.json (197 lines)
│   └─ 🔧 stress-results.json (97 lines)
├─ 📂 helpers
│   └─ 📇 index.js (113 lines)
├─ 📂 stress
│   ├─ 🔌 stress-api.js (21 lines)
│   ├─ ⚙️ stress-config.js (29 lines)
│   ├─ 📊 stress-database.js (33 lines)
│   ├─ 📜 stress-lifecycle.js (19 lines)
│   ├─ 📜 stress-memory.js (30 lines)
│   ├─ 📜 stress-operations.js (81 lines)
│   ├─ 🔌 stress-plugins.js (24 lines)
│   ├─ 🔐 stress-security.js (40 lines)
│   └─ 📜 stress-validators.js (54 lines)
└─ 📂 suites
    ├─ 🧪 core-tests.js (30 lines)
    ├─ 📊 data-tests.js (30 lines)
    ├─ 🧪 handler-tests.js (63 lines)
    └─ 🧪 security-tests.js (39 lines)
📂 scripts
└─ 📜 generate-docs.js (22 lines)
📂 data
└─ 🤖 bot.db (0 lines)
📦 package.json (32 lines)
📝 .env.template (20 lines)
```

## 📄 Project File Contents


=== File: src\main.js (16 lines) ===

```javascript
// Bootstrap entry point
const config = require('./core/config');
const client = require('./core/client');
const shutdown = require('./core/shutdown');

process.on('SIGINT', shutdown);
process.on('SIGTERM', shutdown);
process.on('uncaughtException', (error) => {
    console.error('Uncaught exception:', error);
    shutdown();
});

client.login(config.discord.token).catch(error => {
    console.error('Failed to login:', error);
    process.exit(1);
});
```

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

=== File: src\core\client.js (49 lines) ===

```javascript
const { Client, GatewayIntentBits, REST, Routes } = require('discord.js');
const config = require('./config');
const { INTENTS } = require('./constants');
const { initializeDatabase } = require('../data');
const { registerEventHandlers } = require('../handlers/command');
const { getSlashCommandData } = require('../handlers/slash');
const { startApiServer } = require('../api/server');

const client = new Client({
    intents: [
        GatewayIntentBits[INTENTS.GUILDS],
        GatewayIntentBits[INTENTS.GUILD_MESSAGES],
        GatewayIntentBits[INTENTS.MESSAGE_CONTENT],
        GatewayIntentBits[INTENTS.DIRECT_MESSAGES]
    ]
});

client.once('clientReady', async () => {
    try {
        await initializeDatabase();
        registerEventHandlers(client);

        const rest = new REST({ version: '10' }).setToken(config.discord.token);

        await rest.put(
            Routes.applicationGuildCommands(config.discord.clientId, config.discord.guildId),
            { body: getSlashCommandData() }
        );

        if (config.api.enabled) {
            await startApiServer();
        }

        console.log(`Logged in as ${client.user.tag} - All systems ready`);
    } catch (error) {
        console.error('Bot initialization failed:', error);
        process.exit(1);
    }
});

client.on('error', (error) => {
    console.error('Discord client error:', error);
});

client.on('warn', (warning) => {
    console.warn('Discord client warning:', warning);
});

module.exports = client;
```

=== File: src\core\config.js (61 lines) ===

```javascript
// Environment configuration
require('dotenv').config();

function validateRequired(key) {
    const value = process.env[key];
    if (!value) {
        throw new Error(`Missing required environment variable: ${key}`);
    }
    return value;
}

function validateNumber(key, defaultValue = null) {
    const value = process.env[key];
    if (!value) {
        if (defaultValue === null) {
            throw new Error(`Missing required environment variable: ${key}`);
        }
        return defaultValue;
    }
    const parsed = parseInt(value, 10);
    if (isNaN(parsed)) {
        throw new Error(`Invalid number for environment variable: ${key}`);
    }
    return parsed;
}

function validateBoolean(key, defaultValue = false) {
    const value = process.env[key];
    if (!value) return defaultValue;
    return value.toLowerCase() === 'true';
}

const config = Object.freeze({
    discord: {
        token: validateRequired('DISCORD_TOKEN'),
        clientId: validateRequired('CLIENT_ID'),
        guildId: validateRequired('GUILD_ID')
    },
    database: {
        path: process.env.DB_PATH || './data/bot.db',
        connectionTimeout: validateNumber('DB_CONNECTION_TIMEOUT', 5000),
        busyTimeout: validateNumber('DB_BUSY_TIMEOUT', 3000)
    },
    api: {
        port: validateNumber('API_PORT', 3000),
        enabled: validateBoolean('API_ENABLED', false),
        timeout: validateNumber('API_TIMEOUT', 30000)
    },
    security: {
        rateLimitWindow: validateNumber('RATE_LIMIT_WINDOW', 60000),
        rateLimitMaxRequests: validateNumber('RATE_LIMIT_MAX_REQUESTS', 10),
        commandCooldown: validateNumber('COMMAND_COOLDOWN', 1000)
    },
    logging: {
        level: process.env.LOG_LEVEL || 'info',
        maxFileSize: validateNumber('LOG_MAX_FILE_SIZE', 10485760),
        maxFiles: validateNumber('LOG_MAX_FILES', 5)
    }
});

module.exports = config;
```

=== File: src\core\constants.js (116 lines) ===

```javascript
// Global constants
const DISCORD_PERMISSIONS = Object.freeze({
    ADMINISTRATOR: 'Administrator',
    MANAGE_GUILD: 'ManageGuild',
    MANAGE_CHANNELS: 'ManageChannels',
    MANAGE_MESSAGES: 'ManageMessages',
    MANAGE_ROLES: 'ManageRoles',
    KICK_MEMBERS: 'KickMembers',
    BAN_MEMBERS: 'BanMembers',
    SEND_MESSAGES: 'SendMessages',
    VIEW_CHANNEL: 'ViewChannel',
    READ_MESSAGE_HISTORY: 'ReadMessageHistory'
});

const RESPONSE_STATUS = Object.freeze({
    SUCCESS: 'success',
    ERROR: 'error',
    WARNING: 'warning',
    INFO: 'info',
    RATE_LIMITED: 'rate_limited',
    PERMISSION_DENIED: 'permission_denied',
    NOT_FOUND: 'not_found'
});

const RESPONSE_MESSAGES = Object.freeze({
    SUCCESS: 'Command executed successfully',
    ERROR: 'An error occurred while processing your request',
    PERMISSION_DENIED: 'You do not have permission to use this command',
    RATE_LIMITED: 'You are being rate limited. Please wait before trying again',
    NOT_FOUND: 'Command not found',
    DATABASE_ERROR: 'Database operation failed',
    INVALID_INPUT: 'Invalid input provided'
});

const DATABASE_TABLES = Object.freeze({
    SERVERS: 'servers',
    USERS: 'users',
    AUDIT_LOGS: 'audit_logs',
    RATE_LIMITS: 'rate_limits'
});

const DATABASE_COLUMNS = Object.freeze({
    SERVERS: {
        GUILD_ID: 'guild_id',
        CONFIG: 'config',
        CREATED_AT: 'created_at',
        UPDATED_AT: 'updated_at'
    },
    USERS: {
        USER_ID: 'user_id',
        GUILD_ID: 'guild_id',
        PERMISSIONS: 'permissions',
        DATA: 'data',
        CREATED_AT: 'created_at'
    },
    AUDIT_LOGS: {
        ID: 'id',
        GUILD_ID: 'guild_id',
        USER_ID: 'user_id',
        ACTION: 'action',
        TIMESTAMP: 'timestamp',
        DATA: 'data'
    },
    RATE_LIMITS: {
        IDENTIFIER: 'identifier',
        COUNT: 'count',
        RESET_TIME: 'reset_time'
    }
});

const AUDIT_ACTIONS = Object.freeze({
    COMMAND_EXECUTED: 'command_executed',
    PERMISSION_DENIED: 'permission_denied',
    RATE_LIMITED: 'rate_limited',
    ERROR_OCCURRED: 'error_occurred',
    USER_JOINED: 'user_joined',
    USER_LEFT: 'user_left',
    SERVER_ADDED: 'server_added',
    SERVER_REMOVED: 'server_removed'
});

const LOG_LEVELS = Object.freeze({
    ERROR: 'error',
    WARN: 'warn',
    INFO: 'info',
    DEBUG: 'debug'
});

const COMMAND_PREFIXES = Object.freeze({
    DEFAULT: '!',
    ADMIN: '!!',
    DEBUG: '?'
});

const INTENTS = Object.freeze({
    GUILDS: 'Guilds',
    GUILD_MESSAGES: 'GuildMessages',
    GUILD_MESSAGE_REACTIONS: 'GuildMessageReactions',
    MESSAGE_CONTENT: 'MessageContent',
    DIRECT_MESSAGES: 'DirectMessages'
});

const EPHEMERAL = 64;

module.exports = {
    DISCORD_PERMISSIONS,
    RESPONSE_STATUS,
    RESPONSE_MESSAGES,
    DATABASE_TABLES,
    DATABASE_COLUMNS,
    AUDIT_ACTIONS,
    LOG_LEVELS,
    COMMAND_PREFIXES,
    INTENTS,
    EPHEMERAL
};
```

=== File: src\core\shutdown.js (40 lines) ===

```javascript
const client = require('./client');
const { closeDatabase } = require('../data');
const { stopApiServer } = require('../api/server');

let isShuttingDown = false;

async function shutdown() {
    if (isShuttingDown) return;
    isShuttingDown = true;

    console.log('Shutting down gracefully...');

    try {
        await stopApiServer();
        console.log('API server stopped');
    } catch (error) {
        console.error('Error during API server shutdown:', error);
    }

    try {
        await closeDatabase();
        console.log('Database connections closed');
    } catch (error) {
        console.error('Error during database shutdown:', error);
    }

    try {
        if (client.isReady()) {
            await client.destroy();
            console.log('Discord client disconnected');
        }
    } catch (error) {
        console.error('Error during client shutdown:', error);
    }

    console.log('Shutdown complete');
    process.exit(0);
}

module.exports = shutdown;
```

=== File: src\data\database.js (68 lines) ===

```javascript
const sqlite3 = require('sqlite3').verbose();
const fs = require('fs');
const path = require('path');
const config = require('../core/config');

let db = null;

function initializeDatabase() {
    return new Promise((resolve, reject) => {
        const dbPath = config.database.path;
        const dbDir = path.dirname(dbPath);
        
        if (!fs.existsSync(dbDir)) {
            fs.mkdirSync(dbDir, { recursive: true });
        }
        
        db = new sqlite3.Database(dbPath, (err) => {
            if (err) {
                reject(err);
                return;
            }
            
            db.configure('busyTimeout', config.database.busyTimeout);
            runMigrations().then(resolve).catch(reject);
        });
    });
}

function runMigrations() {
    return new Promise((resolve, reject) => {
        const schemaPath = path.join(__dirname, 'schemas.sql');
        const schema = fs.readFileSync(schemaPath, 'utf8');
        
        db.exec(schema, (err) => {
            if (err) reject(err);
            else resolve();
        });
    });
}

function closeDatabase() {
    return new Promise((resolve) => {
        if (db) {
            db.close((err) => {
                if (err) console.error('Database close error:', err);
                db = null;
                resolve();
            });
        } else {
            resolve();
        }
    });
}

function getDatabaseConnection() {
    return db;
}

function isDatabaseReady() {
    return db !== null;
}

module.exports = {
    initializeDatabase,
    closeDatabase,
    getDatabaseConnection,
    isDatabaseReady
};
```

=== File: src\data\helpers.js (56 lines) ===

```javascript
const { insert, deleteRows } = require('./operations');
const { DATABASE_TABLES } = require('../core/constants');

function insertAuditLog(guildId, userId, action, data = {}) {
    const auditData = {
        guild_id: guildId,
        user_id: userId,
        action: action,
        data: JSON.stringify(data),
        timestamp: new Date().toISOString()
    };
    return insert(DATABASE_TABLES.AUDIT_LOGS, auditData);
}

function cleanupExpiredRateLimits() {
    const now = Date.now();
    return deleteRows(DATABASE_TABLES.RATE_LIMITS, { reset_time: `< ${now}` });
}

function insertServer(guildId, configData = {}) {
    const serverData = {
        guild_id: guildId,
        config: JSON.stringify(configData),
        created_at: new Date().toISOString(),
        updated_at: new Date().toISOString()
    };
    return insert(DATABASE_TABLES.SERVERS, serverData);
}

function insertUser(userId, guildId, permissions = [], userData = {}) {
    const userRecord = {
        user_id: userId,
        guild_id: guildId,
        permissions: JSON.stringify(permissions),
        data: JSON.stringify(userData),
        created_at: new Date().toISOString()
    };
    return insert(DATABASE_TABLES.USERS, userRecord);
}

function insertRateLimit(identifier, count, resetTime) {
    const rateLimitData = {
        identifier: identifier,
        count: count,
        reset_time: resetTime
    };
    return insert(DATABASE_TABLES.RATE_LIMITS, rateLimitData);
}

module.exports = {
    insertAuditLog,
    cleanupExpiredRateLimits,
    insertServer,
    insertUser,
    insertRateLimit
};
```

=== File: src\data\index.js (19 lines) ===

```javascript
const { initializeDatabase, closeDatabase, isDatabaseReady } = require('./database');
const { insert, select, deleteRows, parseJsonFields, prepareJsonData } = require('./operations');
const { insertAuditLog, cleanupExpiredRateLimits, insertServer, insertUser, insertRateLimit } = require('./helpers');

module.exports = {
    initializeDatabase,
    closeDatabase,
    isDatabaseReady,
    insert,
    select,
    deleteRows,
    parseJsonFields,
    prepareJsonData,
    insertAuditLog,
    cleanupExpiredRateLimits,
    insertServer,
    insertUser,
    insertRateLimit
};
```

=== File: src\data\operations.js (95 lines) ===

```javascript
const { getDatabaseConnection } = require('./database');

function insert(table, data) {
    return new Promise((resolve, reject) => {
        const db = getDatabaseConnection();
        if (!db) {
            reject(new Error('Database not initialized'));
            return;
        }
        
        const keys = Object.keys(data);
        const placeholders = keys.map(() => '?').join(', ');
        const sql = `INSERT OR REPLACE INTO ${table} (${keys.join(', ')}) VALUES (${placeholders})`;
        
        db.run(sql, Object.values(data), function(err) {
            if (err) reject(err);
            else resolve({ id: this.lastID, changes: this.changes });
        });
    });
}

function select(table, where = {}) {
    return new Promise((resolve, reject) => {
        const db = getDatabaseConnection();
        if (!db) {
            reject(new Error('Database not initialized'));
            return;
        }
        
        const whereKeys = Object.keys(where);
        let sql = `SELECT * FROM ${table}`;
        
        if (whereKeys.length > 0) {
            const whereClause = whereKeys.map(key => `${key} = ?`).join(' AND ');
            sql += ` WHERE ${whereClause}`;
        }
        
        const method = whereKeys.length > 0 ? 'get' : 'all';
        const values = Object.values(where);
        
        db[method](sql, values, (err, result) => {
            if (err) reject(err);
            else resolve(result);
        });
    });
}

function deleteRows(table, where) {
    return new Promise((resolve, reject) => {
        const db = getDatabaseConnection();
        if (!db) {
            reject(new Error('Database not initialized'));
            return;
        }
        
        const whereKeys = Object.keys(where);
        const whereClause = whereKeys.map(key => `${key} = ?`).join(' AND ');
        const sql = `DELETE FROM ${table} WHERE ${whereClause}`;
        
        db.run(sql, Object.values(where), function(err) {
            if (err) reject(err);
            else resolve({ changes: this.changes });
        });
    });
}

function parseJsonFields(row, jsonFields) {
    if (!row) return null;
    
    const parsed = { ...row };
    jsonFields.forEach(field => {
        if (parsed[field]) {
            parsed[field] = JSON.parse(parsed[field]);
        }
    });
    return parsed;
}

function prepareJsonData(data, jsonFields) {
    const prepared = { ...data };
    jsonFields.forEach(field => {
        if (prepared[field] && typeof prepared[field] === 'object') {
            prepared[field] = JSON.stringify(prepared[field]);
        }
    });
    return prepared;
}

module.exports = {
    insert,
    select,
    deleteRows,
    parseJsonFields,
    prepareJsonData
};
```

=== File: src\data\schemas.sql (51 lines) ===

```sql
-- Database table schemas
-- servers table: guild configuration storage
CREATE TABLE IF NOT EXISTS servers (
    guild_id TEXT PRIMARY KEY,
    config TEXT NOT NULL DEFAULT '{}',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- users table: per-server user data and permissions
CREATE TABLE IF NOT EXISTS users (
    user_id TEXT NOT NULL,
    guild_id TEXT NOT NULL,
    permissions TEXT DEFAULT '[]',
    data TEXT DEFAULT '{}',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id, guild_id),
    FOREIGN KEY (guild_id) REFERENCES servers(guild_id) ON DELETE CASCADE
);

-- audit_logs table: system and user action tracking
CREATE TABLE IF NOT EXISTS audit_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    guild_id TEXT NOT NULL,
    user_id TEXT,
    action TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    data TEXT DEFAULT '{}',
    FOREIGN KEY (guild_id) REFERENCES servers(guild_id) ON DELETE CASCADE
);

-- rate_limits table: command rate limiting storage
CREATE TABLE IF NOT EXISTS rate_limits (
    identifier TEXT PRIMARY KEY,
    count INTEGER NOT NULL DEFAULT 0,
    reset_time INTEGER NOT NULL
);

-- Performance indexes
CREATE INDEX IF NOT EXISTS idx_servers_guild_id ON servers(guild_id);
CREATE INDEX IF NOT EXISTS idx_users_guild_user ON users(guild_id, user_id);
CREATE INDEX IF NOT EXISTS idx_audit_guild_timestamp ON audit_logs(guild_id, timestamp);
CREATE INDEX IF NOT EXISTS idx_audit_user_timestamp ON audit_logs(user_id, timestamp);
CREATE INDEX IF NOT EXISTS idx_rate_limits_reset ON rate_limits(reset_time);

-- Cleanup trigger for updated_at on servers
CREATE TRIGGER IF NOT EXISTS servers_updated_at 
AFTER UPDATE ON servers
BEGIN
    UPDATE servers SET updated_at = CURRENT_TIMESTAMP WHERE guild_id = NEW.guild_id;
END;
```

=== File: src\handlers\audit.js (115 lines) ===

```javascript
const { select, insertAuditLog } = require('../data');
const { DATABASE_TABLES, LOG_LEVELS, AUDIT_ACTIONS } = require('../core/constants');
const logger = require('../utils/logger');

async function logEvent(level, action, guildId, userId, data = {}) {
    const message = `${action}: ${guildId}${userId ? `:${userId}` : ''}`;
    
    if (level === LOG_LEVELS.ERROR || level === LOG_LEVELS.DEBUG) {
        console.log(`[${level.toUpperCase()}] ${message}`, data);
    }
    
    await logger.write(level, message, data);
    
    if (guildId && level !== LOG_LEVELS.DEBUG) {
        try {
            await insertAuditLog(guildId, userId, action, data);
        } catch (error) {
            console.error('Failed to insert audit log:', error);
        }
    }
}

async function logCommandExecution(guildId, userId, command, args, success = true) {
    const action = success ? AUDIT_ACTIONS.COMMAND_EXECUTED : AUDIT_ACTIONS.ERROR_OCCURRED;
    const level = success ? LOG_LEVELS.INFO : LOG_LEVELS.ERROR;
    await logEvent(level, action, guildId, userId, { command, args });
}

async function logPermissionDenied(guildId, userId, command, requiredPermission) {
    await logEvent(LOG_LEVELS.WARN, AUDIT_ACTIONS.PERMISSION_DENIED, guildId, userId, {
        command, requiredPermission
    });
}

async function logRateLimit(guildId, userId, command) {
    await logEvent(LOG_LEVELS.WARN, AUDIT_ACTIONS.RATE_LIMITED, guildId, userId, { command });
}

async function logError(error, context = {}) {
    await logEvent(LOG_LEVELS.ERROR, AUDIT_ACTIONS.ERROR_OCCURRED, context.guildId, context.userId, {
        error: error.message,
        stack: error.stack,
        context
    });
}

async function logUserJoin(guildId, userId) {
    await logEvent(LOG_LEVELS.INFO, AUDIT_ACTIONS.USER_JOINED, guildId, userId);
}

async function logUserLeave(guildId, userId) {
    await logEvent(LOG_LEVELS.INFO, AUDIT_ACTIONS.USER_LEFT, guildId, userId);
}

async function logServerAdd(guildId) {
    await logEvent(LOG_LEVELS.INFO, AUDIT_ACTIONS.SERVER_ADDED, guildId, null);
}

async function logServerRemove(guildId) {
    await logEvent(LOG_LEVELS.INFO, AUDIT_ACTIONS.SERVER_REMOVED, guildId, null);
}

async function queryAuditLogs(guildId, filters = {}) {
    try {
        const whereClause = { guild_id: guildId };
        
        if (filters.userId) whereClause.user_id = filters.userId;
        if (filters.action) whereClause.action = filters.action;
        
        const logs = await select(DATABASE_TABLES.AUDIT_LOGS, whereClause);
        
        if (Array.isArray(logs)) {
            return logs.slice(0, filters.limit || 100);
        }
        
        return logs ? [logs] : [];
        
    } catch (error) {
        console.error('Failed to query audit logs:', error);
        return [];
    }
}

async function getAuditStats(guildId) {
    try {
        const logs = await select(DATABASE_TABLES.AUDIT_LOGS, { guild_id: guildId });
        const logArray = Array.isArray(logs) ? logs : (logs ? [logs] : []);
        
        const stats = {
            totalEvents: logArray.length,
            commandsExecuted: logArray.filter(log => log.action === AUDIT_ACTIONS.COMMAND_EXECUTED).length,
            errorsOccurred: logArray.filter(log => log.action === AUDIT_ACTIONS.ERROR_OCCURRED).length,
            permissionsDenied: logArray.filter(log => log.action === AUDIT_ACTIONS.PERMISSION_DENIED).length,
            rateLimited: logArray.filter(log => log.action === AUDIT_ACTIONS.RATE_LIMITED).length
        };
        
        return stats;
    } catch (error) {
        console.error('Failed to get audit stats:', error);
        return { totalEvents: 0, commandsExecuted: 0, errorsOccurred: 0, permissionsDenied: 0, rateLimited: 0 };
    }
}

module.exports = {
    logCommandExecution,
    logPermissionDenied,
    logRateLimit,
    logError,
    logUserJoin,
    logUserLeave,
    logServerAdd,
    logServerRemove,
    queryAuditLogs,
    getAuditStats
};
```

=== File: src\handlers\command.js (98 lines) ===

```javascript
const { processMessage } = require('./message');
const { processSlashCommand } = require('./slash');
const { processInteraction } = require('./interaction');
const { logUserJoin, logUserLeave, logServerAdd, logServerRemove, logError } = require('./audit');

function registerEventHandlers(client) {
    client.on('messageCreate', async (message) => {
        try {
            await processMessage(message);
        } catch (error) {
            console.error('Message processing error:', error);
            await logError(error, { 
                guildId: message.guild?.id,
                userId: message.author?.id,
                messageId: message.id 
            });
        }
    });
    
    client.on('interactionCreate', async (interaction) => {
        try {
            if (interaction.isChatInputCommand()) {
                await processSlashCommand(interaction);
            } else {
                await processInteraction(interaction);
            }
        } catch (error) {
            console.error('Interaction processing error:', error);
            await logError(error, { 
                guildId: interaction.guild?.id,
                userId: interaction.user?.id,
                interactionId: interaction.id 
            });
        }
    });
    
    client.on('guildMemberAdd', async (member) => {
        try {
            await logUserJoin(member.guild.id, member.user.id);
        } catch (error) {
            console.error('Guild member add logging error:', error);
        }
    });
    
    client.on('guildMemberRemove', async (member) => {
        try {
            await logUserLeave(member.guild.id, member.user.id);
        } catch (error) {
            console.error('Guild member remove logging error:', error);
        }
    });
    
    client.on('guildCreate', async (guild) => {
        try {
            await logServerAdd(guild.id);
            console.log(`Joined server: ${guild.name} (${guild.memberCount} members)`);
        } catch (error) {
            console.error('Guild create logging error:', error);
        }
    });
    
    client.on('guildDelete', async (guild) => {
        try {
            await logServerRemove(guild.id);
            console.log(`Left server: ${guild.name}`);
        } catch (error) {
            console.error('Guild delete logging error:', error);
        }
    });
}

function reloadAllPlugins() {
    const { reloadPlugins } = require('./message');
    const { reloadSlashPlugins } = require('./slash');
    const { reloadInteractionPlugins } = require('./interaction');
    
    reloadPlugins();
    reloadSlashPlugins();
    reloadInteractionPlugins();
}

function getLoadedPlugins() {
    const { getLoadedPlugins: getMessagePlugins } = require('./message');
    const { getLoadedPlugins: getSlashPlugins } = require('./slash');
    const { getLoadedPlugins: getInteractionPlugins } = require('./interaction');
    
    return {
        ...getMessagePlugins(),
        slash: getSlashPlugins(),
        interactions: getInteractionPlugins()
    };
}

module.exports = {
    registerEventHandlers,
    reloadAllPlugins,
    getLoadedPlugins
};
```

=== File: src\handlers\interaction.js (118 lines) ===

```javascript
const fs = require('fs');
const path = require('path');
const { checkRateLimit } = require('../security/ratelimit');
const { insertAuditLog } = require('../data');
const { AUDIT_ACTIONS, EPHEMERAL } = require('../core/constants');

const interactionPlugins = new Map();

function loadInteractionPlugins() {
    const pluginDir = path.join(__dirname, '../plugins/interactions');
    
    if (!fs.existsSync(pluginDir)) {
        fs.mkdirSync(pluginDir, { recursive: true });
        return;
    }
    
    const files = fs.readdirSync(pluginDir).filter(file => file.endsWith('.js'));
    
    files.forEach(file => {
        try {
            const pluginPath = path.join(pluginDir, file);
            delete require.cache[require.resolve(pluginPath)];
            const plugin = require(pluginPath);
            
            if (plugin.type === 'interaction' && plugin.name) {
                interactionPlugins.set(plugin.name, plugin);
            }
        } catch (error) {
            console.error(`Failed to load interaction plugin ${file}:`, error);
        }
    });
}

async function processInteraction(interaction) {
    if (interaction.isChatInputCommand()) return;
    
    const userId = interaction.user.id;
    const guildId = interaction.guild?.id;
    
    for (const plugin of interactionPlugins.values()) {
        try {
            if (plugin.filter && !plugin.filter(interaction)) continue;
            
            if (guildId) {
                const rateLimit = await checkRateLimit(userId, guildId, `interaction_${plugin.name}`);
                if (!rateLimit.allowed) {
                    await interaction.reply({ 
                        content: `Rate limited. Try again in ${Math.ceil(rateLimit.resetIn / 1000)} seconds.`,
                        flags: EPHEMERAL
                    });
                    await insertAuditLog(guildId, userId, AUDIT_ACTIONS.RATE_LIMITED, { 
                        interaction: plugin.name 
                    });
                    continue;
                }
            }
            
            await plugin.execute(interaction);
            
            if (guildId) {
                await insertAuditLog(guildId, userId, AUDIT_ACTIONS.COMMAND_EXECUTED, { 
                    interaction: plugin.name,
                    type: getInteractionType(interaction)
                });
            }
            
            break;
            
        } catch (error) {
            console.error(`Interaction plugin ${plugin.name} error:`, error);
            
            if (guildId) {
                await insertAuditLog(guildId, userId, AUDIT_ACTIONS.ERROR_OCCURRED, { 
                    interaction: plugin.name,
                    error: error.message 
                });
            }
            
            if (plugin.handleError) {
                await plugin.handleError(interaction, error);
            } else {
                try {
                    const content = 'An error occurred while processing your interaction.';
                    
                    if (interaction.deferred || interaction.replied) {
                        await interaction.editReply({ content, flags: EPHEMERAL });
                    } else {
                        await interaction.reply({ content, flags: EPHEMERAL });
                    }
                } catch (replyError) {
                    console.error('Failed to send error response:', replyError);
                }
            }
        }
    }
}

function getInteractionType(interaction) {
    if (interaction.isButton()) return 'button';
    if (interaction.isStringSelectMenu()) return 'select';
    if (interaction.isModalSubmit()) return 'modal';
    if (interaction.isContextMenuCommand()) return 'context';
    return 'unknown';
}

function reloadInteractionPlugins() {
    interactionPlugins.clear();
    loadInteractionPlugins();
    console.log(`Loaded ${interactionPlugins.size} interaction plugins`);
}

loadInteractionPlugins();

module.exports = {
    processInteraction,
    reloadInteractionPlugins,
    getLoadedPlugins: () => Array.from(interactionPlugins.keys())
};
```

=== File: src\handlers\message.js (132 lines) ===

```javascript
const fs = require('fs');
const path = require('path');
const { COMMAND_PREFIXES } = require('../core/constants');
const { checkRateLimit } = require('../security/ratelimit');
const { checkCommandPermission } = require('../security/permissions');
const { insertAuditLog } = require('../data');
const { AUDIT_ACTIONS } = require('../core/constants');

const messagePlugins = new Map();
const commandPlugins = new Map();

function loadPlugins() {
    const pluginDirs = [
        path.join(__dirname, '../plugins/messages'),
        path.join(__dirname, '../plugins/commands')
    ];
    
    pluginDirs.forEach(dir => {
        if (!fs.existsSync(dir)) {
            fs.mkdirSync(dir, { recursive: true });
            return;
        }
        
        const files = fs.readdirSync(dir).filter(file => file.endsWith('.js'));
        
        files.forEach(file => {
            try {
                const pluginPath = path.join(dir, file);
                delete require.cache[require.resolve(pluginPath)];
                const plugin = require(pluginPath);
                
                if (plugin.type === 'message') {
                    messagePlugins.set(plugin.name, plugin);
                } else if (plugin.type === 'command') {
                    commandPlugins.set(plugin.name, plugin);
                }
            } catch (error) {
                console.error(`Failed to load plugin ${file}:`, error);
            }
        });
    });
}

function parseCommand(content, guildId) {
    const prefixes = Object.values(COMMAND_PREFIXES);
    const usedPrefix = prefixes.find(prefix => content.startsWith(prefix));
    
    if (!usedPrefix) return null;
    
    const args = content.slice(usedPrefix.length).trim().split(/\s+/);
    const command = args.shift().toLowerCase();
    
    return { command, args, prefix: usedPrefix };
}

async function processMessage(message) {
    if (message.author.bot) return;
    if (!message.guild) return;
    
    for (const plugin of messagePlugins.values()) {
        try {
            if (plugin.filter && !plugin.filter(message)) continue;
            await plugin.execute(message);
        } catch (error) {
            console.error(`Message plugin ${plugin.name} error:`, error);
        }
    }
    
    const parsedCommand = parseCommand(message.content, message.guild.id);
    if (!parsedCommand) return;
    
    await processCommand(message, parsedCommand);
}

async function processCommand(message, parsedCommand) {
    const { command, args, prefix } = parsedCommand;
    const plugin = commandPlugins.get(command);
    
    if (!plugin) return;
    
    const userId = message.author.id;
    const guildId = message.guild.id;
    
    try {
        const rateLimit = await checkRateLimit(userId, guildId, command);
        if (!rateLimit.allowed) {
            await message.reply(`Rate limited. Try again in ${Math.ceil(rateLimit.resetIn / 1000)} seconds.`);
            await insertAuditLog(guildId, userId, AUDIT_ACTIONS.RATE_LIMITED, { command });
            return;
        }
        
        if (plugin.permission) {
            const hasPermission = await checkCommandPermission(userId, guildId, plugin.permission);
            if (!hasPermission) {
                await message.reply('You do not have permission to use this command.');
                await insertAuditLog(guildId, userId, AUDIT_ACTIONS.PERMISSION_DENIED, { command });
                return;
            }
        }
        
        await plugin.execute(message, args);
        await insertAuditLog(guildId, userId, AUDIT_ACTIONS.COMMAND_EXECUTED, { command, args });
        
    } catch (error) {
        console.error(`Command ${command} error:`, error);
        await insertAuditLog(guildId, userId, AUDIT_ACTIONS.ERROR_OCCURRED, { command, error: error.message });
        
        if (plugin.handleError) {
            await plugin.handleError(message, error);
        } else {
            await message.reply('An error occurred while processing your command.');
        }
    }
}

function reloadPlugins() {
    messagePlugins.clear();
    commandPlugins.clear();
    loadPlugins();
    console.log(`Loaded ${messagePlugins.size} message plugins and ${commandPlugins.size} command plugins`);
}

loadPlugins();

module.exports = {
    processMessage,
    reloadPlugins,
    getLoadedPlugins: () => ({ 
        messages: Array.from(messagePlugins.keys()), 
        commands: Array.from(commandPlugins.keys()) 
    })
};
```

=== File: src\handlers\slash.js (126 lines) ===

```javascript
const fs = require('fs');
const path = require('path');
const { checkRateLimit } = require('../security/ratelimit');
const { checkCommandPermission } = require('../security/permissions');
const { insertAuditLog } = require('../data');
const { AUDIT_ACTIONS, EPHEMERAL } = require('../core/constants');

const slashPlugins = new Map();

function loadSlashPlugins() {
    const pluginDir = path.join(__dirname, '../plugins/slash');
    
    if (!fs.existsSync(pluginDir)) {
        fs.mkdirSync(pluginDir, { recursive: true });
        return;
    }
    
    const files = fs.readdirSync(pluginDir).filter(file => file.endsWith('.js'));
    
    files.forEach(file => {
        try {
            const pluginPath = path.join(pluginDir, file);
            delete require.cache[require.resolve(pluginPath)];
            const plugin = require(pluginPath);
            
            if (plugin.type === 'slash' && plugin.name) {
                slashPlugins.set(plugin.name, plugin);
            }
        } catch (error) {
            console.error(`Failed to load slash plugin ${file}:`, error);
        }
    });
}

async function processSlashCommand(interaction) {
    if (!interaction.isChatInputCommand()) return;
    
    const commandName = interaction.commandName;
    const plugin = slashPlugins.get(commandName);
    
    if (!plugin) {
        await interaction.reply({ content: 'Unknown command.', flags: EPHEMERAL });
        return;
    }

    const userId = interaction.user.id;
    const guildId = interaction.guild?.id;

    try {
        if (guildId) {
            const rateLimit = await checkRateLimit(userId, guildId, commandName);
            if (!rateLimit.allowed) {
                await interaction.reply({ 
                    content: `Rate limited. Try again in ${Math.ceil(rateLimit.resetIn / 1000)} seconds.`,
                    flags: EPHEMERAL
                });
                await insertAuditLog(guildId, userId, AUDIT_ACTIONS.RATE_LIMITED, { command: commandName });
                return;
            }

            if (plugin.permission) {
                const hasPermission = await checkCommandPermission(userId, guildId, plugin.permission);
                if (!hasPermission) {
                    await interaction.reply({ 
                        content: 'You do not have permission to use this command.',
                        flags: EPHEMERAL
                    });
                    await insertAuditLog(guildId, userId, AUDIT_ACTIONS.PERMISSION_DENIED, { command: commandName });
                    return;
                }
            }
        }

        await plugin.execute(interaction);

        if (guildId) {
            await insertAuditLog(guildId, userId, AUDIT_ACTIONS.COMMAND_EXECUTED, { 
                command: commandName,
                options: interaction.options.data 
            });
        }

    } catch (error) {
        console.error(`Slash command ${commandName} error:`, error);

        if (guildId) {
            await insertAuditLog(guildId, userId, AUDIT_ACTIONS.ERROR_OCCURRED, { 
                command: commandName, 
                error: error.message 
            });
        }

        if (plugin.handleError) {
            await plugin.handleError(interaction, error);
        } else {
            const content = 'An error occurred while processing your command.';

            if (interaction.deferred || interaction.replied) {
                await interaction.editReply({ content, flags: EPHEMERAL });
            } else {
                await interaction.reply({ content, flags: EPHEMERAL });
            }
        }
    }
}

function getSlashCommandData() {
    return Array.from(slashPlugins.values())
        .filter(plugin => plugin.data)
        .map(plugin => plugin.data);
}

function reloadSlashPlugins() {
    slashPlugins.clear();
    loadSlashPlugins();
    console.log(`Loaded ${slashPlugins.size} slash command plugins`);
}

loadSlashPlugins();

module.exports = {
    processSlashCommand,
    getSlashCommandData,
    reloadSlashPlugins,
    getLoadedPlugins: () => Array.from(slashPlugins.keys())
};
```

=== File: src\plugins\commands\ping.js (15 lines) ===

```javascript
// src/plugins/commands/ping.js - Example text command plugin
const { DISCORD_PERMISSIONS } = require('../../core/constants');

module.exports = {
    type: 'command',
    name: 'ping',
    description: 'Responds with pong and latency',
    permission: null,
    
    async execute(message, args) {
        const sent = await message.reply('Pinging...');
        const latency = sent.createdTimestamp - message.createdTimestamp;
        await sent.edit(`Pong! Latency: ${latency}ms`);
    }
};
```

=== File: src\plugins\interactions\button.js (24 lines) ===

```javascript
const { EPHEMERAL } = require("../../core/constants");

// src/plugins/interactions/button.js - Example interaction plugin
module.exports = {
    type: 'interaction',
    name: 'button_handler',
    
    filter(interaction) {
        return interaction.isButton() && interaction.customId.startsWith('example_');
    },
    
    async execute(interaction) {
        const action = interaction.customId.split('_')[1];
        
        switch(action) {
            case 'confirm':
                await interaction.reply({ content: 'Confirmed!', flags: EPHEMERAL });
                break;
            case 'cancel':
                await interaction.reply({ content: 'Cancelled!', flags: EPHEMERAL });
                break;
        }
    }
};
```

=== File: src\plugins\messages\welcome.js (14 lines) ===

```javascript
// src/plugins/messages/welcome.js - Example message plugin
module.exports = {
    type: 'message',
    name: 'welcome',
    description: 'Welcomes new members',
    
    filter(message) {
        return message.type === 7; // GUILD_MEMBER_JOIN
    },
    
    async execute(message) {
        await message.channel.send(`Welcome ${message.author}!`);
    }
};
```

=== File: src\plugins\slash\info.js (20 lines) ===

```javascript
const { SlashCommandBuilder } = require('discord.js');
const { EPHEMERAL } = require('../../core/constants');

module.exports = {
    type: 'slash',
    name: 'info',
    data: new SlashCommandBuilder()
        .setName('info')
        .setDescription('Get bot information'),
    
    async execute(interaction) {
        const uptime = process.uptime();
        const memory = process.memoryUsage().heapUsed / 1024 / 1024;
        
        await interaction.reply({
            content: `Bot Uptime: ${Math.floor(uptime / 60)}m ${Math.floor(uptime % 60)}s\nMemory: ${memory.toFixed(2)}MB`,
            flags: EPHEMERAL
        });
    }
};
```

=== File: src\security\permissions.js (110 lines) ===

```javascript
const { DISCORD_PERMISSIONS } = require('../core/constants');
const { select, insert } = require('../data');
const { DATABASE_TABLES } = require('../core/constants');

function hasPermission(userPermissions, requiredPermission) {
    if (!Array.isArray(userPermissions)) return false;
    if (!requiredPermission) return true;
    
    if (userPermissions.includes(DISCORD_PERMISSIONS.ADMINISTRATOR)) {
        return true;
    }
    
    return userPermissions.includes(requiredPermission);
}

function hasAnyPermission(userPermissions, requiredPermissions) {
    if (!Array.isArray(userPermissions) || !Array.isArray(requiredPermissions)) return false;
    
    if (userPermissions.includes(DISCORD_PERMISSIONS.ADMINISTRATOR)) {
        return true;
    }
    
    return requiredPermissions.some(permission => userPermissions.includes(permission));
}

function hasAllPermissions(userPermissions, requiredPermissions) {
    if (!Array.isArray(userPermissions) || !Array.isArray(requiredPermissions)) return false;
    
    if (userPermissions.includes(DISCORD_PERMISSIONS.ADMINISTRATOR)) {
        return true;
    }
    
    return requiredPermissions.every(permission => userPermissions.includes(permission));
}

function checkRoleHierarchy(userRoles, targetRole) {
    if (!Array.isArray(userRoles) || !targetRole) return false;
    
    const highestUserRole = Math.max(...userRoles.map(role => role.position || 0));
    const targetPosition = targetRole.position || 0;
    
    return highestUserRole > targetPosition;
}

async function getUserPermissions(userId, guildId) {
    try {
        const user = await select(DATABASE_TABLES.USERS, { user_id: userId, guild_id: guildId });
        
        if (!user) {
            return [];
        }
        
        return JSON.parse(user.permissions || '[]');
    } catch (error) {
        console.error('Error getting user permissions:', error);
        return [];
    }
}

async function setUserPermissions(userId, guildId, permissions) {
    try {
        const userData = {
            user_id: userId,
            guild_id: guildId,
            permissions: JSON.stringify(permissions),
            data: JSON.stringify({})
        };
        
        await insert(DATABASE_TABLES.USERS, userData);
        return true;
    } catch (error) {
        console.error('Error setting user permissions:', error);
        return false;
    }
}

function validateBotPermissions(botMember, requiredPermissions) {
    if (!botMember || !Array.isArray(requiredPermissions)) return false;
    
    const botPermissions = botMember.permissions.toArray();
    
    if (botPermissions.includes(DISCORD_PERMISSIONS.ADMINISTRATOR)) {
        return true;
    }
    
    return requiredPermissions.every(permission => botPermissions.includes(permission));
}

async function checkCommandPermission(userId, guildId, requiredPermission) {
    if (!requiredPermission) return true;
    
    try {
        const userPermissions = await getUserPermissions(userId, guildId);
        return hasPermission(userPermissions, requiredPermission);
    } catch (error) {
        console.error('Error checking command permission:', error);
        return false;
    }
}

module.exports = {
    hasPermission,
    hasAnyPermission,
    hasAllPermissions,
    checkRoleHierarchy,
    getUserPermissions,
    setUserPermissions,
    validateBotPermissions,
    checkCommandPermission
};
```

=== File: src\security\ratelimit.js (143 lines) ⚠️ ===

```javascript
const config = require('../core/config');
const { select, insert, cleanupExpiredRateLimits } = require('../data');
const { DATABASE_TABLES } = require('../core/constants');

function createIdentifier(userId, guildId, command = 'global') {
    return `${guildId}:${userId}:${command}`;
}

async function checkRateLimit(userId, guildId, command = 'global') {
    try {
        const identifier = createIdentifier(userId, guildId, command);
        const now = Date.now();
        
        const existing = await select(DATABASE_TABLES.RATE_LIMITS, { identifier });
        
        if (!existing) {
            await insert(DATABASE_TABLES.RATE_LIMITS, {
                identifier,
                count: 1,
                reset_time: now + config.security.rateLimitWindow
            });
            return { allowed: true, remaining: config.security.rateLimitMaxRequests - 1 };
        }
        
        if (now >= existing.reset_time) {
            await insert(DATABASE_TABLES.RATE_LIMITS, {
                identifier,
                count: 1,
                reset_time: now + config.security.rateLimitWindow
            });
            return { allowed: true, remaining: config.security.rateLimitMaxRequests - 1 };
        }
        
        if (existing.count >= config.security.rateLimitMaxRequests) {
            const resetIn = existing.reset_time - now;
            return { 
                allowed: false, 
                remaining: 0, 
                resetIn,
                resetTime: existing.reset_time 
            };
        }
        
        await insert(DATABASE_TABLES.RATE_LIMITS, {
            identifier,
            count: existing.count + 1,
            reset_time: existing.reset_time
        });
        
        return { 
            allowed: true, 
            remaining: config.security.rateLimitMaxRequests - (existing.count + 1) 
        };
        
    } catch (error) {
        console.error('Error checking rate limit:', error);
        return { allowed: true, remaining: config.security.rateLimitMaxRequests };
    }
}

async function getRemainingTime(userId, guildId, command = 'global') {
    try {
        const identifier = createIdentifier(userId, guildId, command);
        const existing = await select(DATABASE_TABLES.RATE_LIMITS, { identifier });
        
        if (!existing) return 0;
        
        const now = Date.now();
        return Math.max(0, existing.reset_time - now);
        
    } catch (error) {
        console.error('Error getting remaining time:', error);
        return 0;
    }
}

async function resetUserRateLimit(userId, guildId, command = 'global') {
    try {
        const identifier = createIdentifier(userId, guildId, command);
        await insert(DATABASE_TABLES.RATE_LIMITS, {
            identifier,
            count: 0,
            reset_time: Date.now()
        });
        return true;
    } catch (error) {
        console.error('Error resetting rate limit:', error);
        return false;
    }
}

async function getUserRateLimitInfo(userId, guildId, command = 'global') {
    try {
        const identifier = createIdentifier(userId, guildId, command);
        const existing = await select(DATABASE_TABLES.RATE_LIMITS, { identifier });
        
        if (!existing) {
            return {
                count: 0,
                remaining: config.security.rateLimitMaxRequests,
                resetTime: null,
                resetIn: 0
            };
        }
        
        const now = Date.now();
        const resetIn = Math.max(0, existing.reset_time - now);
        
        return {
            count: existing.count,
            remaining: Math.max(0, config.security.rateLimitMaxRequests - existing.count),
            resetTime: existing.reset_time,
            resetIn
        };
        
    } catch (error) {
        console.error('Error getting rate limit info:', error);
        return {
            count: 0,
            remaining: config.security.rateLimitMaxRequests,
            resetTime: null,
            resetIn: 0
        };
    }
}

async function cleanupOldRateLimits() {
    try {
        const result = await cleanupExpiredRateLimits();
        return result.changes || 0;
    } catch (error) {
        console.error('Error cleaning up rate limits:', error);
        return 0;
    }
}

module.exports = {
    checkRateLimit,
    getRemainingTime,
    resetUserRateLimit,
    getUserRateLimitInfo,
    cleanupOldRateLimits
};
```

=== File: src\utils\docs-generator.js (140 lines) ⚠️ ===

```javascript
const fs = require('fs').promises;
const path = require('path');
const ProjectAnalyzer = require('./docs/analyzer');
const ReadmeGenerator = require('./docs/readme-generator');
const DocsWriter = require('./docs/writer');

class DocsGenerator {
    constructor() {
        this.projectRoot = path.resolve(__dirname, '../..');
        this.docsPath = path.join(this.projectRoot, 'docs');
        this.analyzer = new ProjectAnalyzer(this.projectRoot);
        this.readmeGenerator = new ReadmeGenerator();
        this.writer = new DocsWriter(this.projectRoot, this.docsPath);
    }

    async generate() {
        console.log('Analyzing project structure...');
        const projectData = await this.analyzer.analyze();
        
        console.log('Generating documentation...');
        const readme = this.readmeGenerator.generate(projectData);
        const architecture = this.generateArchitectureDocs(projectData);
        const api = this.generateApiDocs();
        
        await this.writer.writeAll({
            readme,
            architecture,
            api
        });
        
        console.log('Documentation generated successfully');
    }

generateArchitectureDocs(projectData) {
        const config = this.getDocConfig();
        
        let content = `# Architecture Overview\n\n`;
        
        if (config.includeSections.modules) {
            content += `## Module Dependencies\n\n`;
            content += Array.from(projectData.modules.entries()).map(([path, module]) => 
                `### ${path}\n- **Purpose**: ${module.description}\n- **Exports**: ${module.exports.join(', ')}\n- **Dependencies**: ${module.dependencies.join(', ')}\n`
            ).join('\n');
            content += '\n\n';
        }
        
        if (config.includeSections.performance) {
            content += config.sections.performance + '\n\n';
        }
        
        if (config.includeSections.plugins) {
            content += config.sections.plugins + '\n\n';
        }
        
        if (config.includeSections.benchmarks) {
            content += config.sections.benchmarks + '\n\n';
        }
        
        if (config.includeSections.stress) {
            content += config.sections.stress;
        }
        
        return content;
    }

    getDocConfig() {
        return {
            includeSections: {
                modules: true,
                performance: true,
                plugins: true,
                benchmarks: true,
                stress: true
            },
            sections: {
                performance: `## Performance Characteristics

All modules are designed for production performance:
- Database operations under 10ms
- Memory usage optimized
- Concurrent operation support
- Graceful error handling`,
                plugins: `## Plugin System Architecture

The plugin system uses runtime discovery:
1. Scan plugin directories on startup
2. Load modules matching plugin interface
3. Register with appropriate handlers
4. Apply security and rate limiting
5. Isolate errors per plugin`
            }
        };
    }

    generateApiDocs() {
        return `# API Reference

## Authentication

All API endpoints require authentication via Bearer token:

\`\`\`
Authorization: Bearer <API_TOKEN>
\`\`\`

## Rate Limiting

API endpoints are rate limited to 100 requests per 15 minutes per IP.

## Error Responses

All errors follow consistent format:
\`\`\`json
{ "error": "Error description" }
\`\`\`

## Endpoints

### System Information
- \`GET /health\` - System health check
- \`GET /api/stats\` - Plugin and system statistics

### Server Management  
- \`GET /api/servers\` - List all servers
- \`GET /api/servers/:id/config\` - Get server configuration
- \`PUT /api/servers/:id/config\` - Update server configuration

### Audit and Monitoring
- \`GET /api/servers/:id/audit\` - Query audit logs
- \`GET /api/servers/:id/stats\` - Server-specific statistics

Query parameters for audit logs:
- \`limit\`: Number of records (default: 50)
- \`action\`: Filter by action type
- \`userId\`: Filter by user ID
`;
    }
}

module.exports = DocsGenerator;
```

=== File: src\utils\logger.js (87 lines) ===

```javascript
// Centralized logging
const fs = require('fs').promises;
const path = require('path');
const config = require('../core/config');

let logFile = null;
let logRotationSize = 0;

function getLogFilePath() {
    const date = new Date().toISOString().split('T')[0];
    return path.join('./logs', `audit-${date}.log`);
}

async function initializeLogging() {
    const logDir = path.dirname(getLogFilePath());
    return fs.mkdir(logDir, { recursive: true }).catch(() => {});
}

async function write(level, message, data = {}) {
    try {
        const timestamp = new Date().toISOString();
        const logEntry = JSON.stringify({
            timestamp,
            level,
            message,
            data
        }) + '\n';
        
        const currentLogFile = getLogFilePath();
        
        if (logFile !== currentLogFile) {
            logFile = currentLogFile;
            logRotationSize = 0;
        }
        
        await fs.appendFile(logFile, logEntry);
        logRotationSize += logEntry.length;
        
        if (logRotationSize > config.logging.maxFileSize) {
            await rotateLogFile();
        }
        
    } catch (error) {
        console.error('Failed to write to log:', error);
    }
}

async function rotateLogFile() {
    try {
        const timestamp = Date.now();
        const rotatedFile = logFile.replace('.log', `-${timestamp}.log`);
        await fs.rename(logFile, rotatedFile);
        logRotationSize = 0;
        
        await cleanupOldLogs();
        
    } catch (error) {
        console.error('Log rotation failed:', error);
    }
}

async function cleanupOldLogs() {
    try {
        const logDir = path.dirname(logFile);
        const files = await fs.readdir(logDir);
        const logFiles = files.filter(file => file.startsWith('audit-') && file.endsWith('.log'));
        
        if (logFiles.length > config.logging.maxFiles) {
            const sortedFiles = logFiles.sort();
            const filesToDelete = sortedFiles.slice(0, logFiles.length - config.logging.maxFiles);
            
            for (const file of filesToDelete) {
                await fs.unlink(path.join(logDir, file));
            }
        }
    } catch (error) {
        console.error('Log cleanup failed:', error);
    }
}

initializeLogging();

module.exports = {
    write,
    rotateLogFile,
    cleanupOldLogs
};
```

=== File: src\utils\docs\analyzer.js (66 lines) ===

```javascript
const fs = require('fs').promises;
const path = require('path');
const FileScanner = require('./file-scanner');
const ModuleParser = require('./module-parser');

class ProjectAnalyzer {
    constructor(projectRoot) {
        this.projectRoot = projectRoot;
        this.srcPath = path.join(projectRoot, 'src');
        this.scanner = new FileScanner();
        this.parser = new ModuleParser();
        this.modules = new Map();
        this.packageInfo = null;
        this.configOptions = [];
    }

    async analyze() {
        await this.scanModules();
        await this.analyzePackageJson();
        await this.analyzeConfig();
        
        return {
            modules: this.modules,
            packageInfo: this.packageInfo,
            configOptions: this.configOptions
        };
    }

    async scanModules() {
        const files = await this.scanner.scanDirectory(this.srcPath);
        
        for (const file of files) {
            const module = await this.parser.parseFile(file.fullPath, file.relativePath);
            this.modules.set(file.relativePath, module);
        }
    }

    async analyzePackageJson() {
        const packagePath = path.join(this.projectRoot, 'package.json');
        const content = await fs.readFile(packagePath, 'utf8');
        const pkg = JSON.parse(content);
        
        this.packageInfo = {
            name: pkg.name,
            version: pkg.version,
            description: pkg.description,
            dependencies: Object.keys(pkg.dependencies || {}),
            devDependencies: Object.keys(pkg.devDependencies || {})
        };
    }

    async analyzeConfig() {
        const envPath = path.join(this.projectRoot, '.env.template');
        const content = await fs.readFile(envPath, 'utf8');
        
        this.configOptions = content
            .split('\n')
            .filter(line => line.includes('=') && !line.startsWith('#'))
            .map(line => {
                const [key, value] = line.split('=');
                return { key: key.trim(), example: value.trim() };
            });
    }
}

module.exports = ProjectAnalyzer;
```

=== File: src\utils\docs\ast-parser.js (100 lines) ===

```javascript
const fs = require('fs').promises;

let parser = null;

function initializeParser() {
    if (parser !== null) return parser;
    
    try {
        const { parse } = require('@babel/parser');
        parser = { parse, available: true };
        return parser;
    } catch (error) {
        parser = { available: false };
        return parser;
    }
}

class ASTParser {
    constructor() {
        this.parser = initializeParser();
    }

    async parseFile(filePath) {
        if (!this.parser.available) {
            return null;
        }

        try {
            const content = await fs.readFile(filePath, 'utf8');
            const ast = this.parser.parse(content, {
                sourceType: 'module',
                allowImportExportEverywhere: true,
                allowReturnOutsideFunction: true
            });

            return {
                exports: this.extractExports(ast),
                dependencies: this.extractDependencies(ast)
            };
        } catch (error) {
            return null;
        }
    }

    extractExports(ast) {
        const exports = [];
        
        for (const node of ast.body) {
            if (node.type === 'ExpressionStatement' && 
                node.expression?.type === 'AssignmentExpression' &&
                node.expression.left?.type === 'MemberExpression' &&
                node.expression.left.object?.name === 'module' &&
                node.expression.left.property?.name === 'exports') {
                
                if (node.expression.right.type === 'ObjectExpression') {
                    for (const prop of node.expression.right.properties) {
                        if (prop.key?.name) {
                            exports.push(prop.key.name);
                        }
                    }
                } else if (node.expression.right.type === 'Identifier') {
                    exports.push(node.expression.right.name);
                }
            }
        }
        
        return exports;
    }

    extractDependencies(ast) {
        const deps = new Set();
        
        const traverse = (node) => {
            if (node.type === 'CallExpression' && 
                node.callee?.name === 'require' &&
                node.arguments?.[0]?.type === 'StringLiteral') {
                
                const dep = node.arguments[0].value;
                if (!dep.startsWith('.')) {
                    deps.add(dep);
                }
            }
            
            for (const key in node) {
                if (typeof node[key] === 'object' && node[key] !== null) {
                    if (Array.isArray(node[key])) {
                        node[key].forEach(traverse);
                    } else {
                        traverse(node[key]);
                    }
                }
            }
        };
        
        ast.body.forEach(traverse);
        return Array.from(deps);
    }
}

module.exports = ASTParser;
```

=== File: src\utils\docs\file-scanner.js (40 lines) ===

```javascript
const fs = require('fs').promises;
const path = require('path');

class FileScanner {
    async scanDirectory(dir, prefix = '') {
        const files = [];
        const entries = await fs.readdir(dir, { withFileTypes: true });
        
        for (const entry of entries) {
            const fullPath = path.join(dir, entry.name);
            const relativePath = path.join(prefix, entry.name);
            
            if (entry.isDirectory()) {
                const subFiles = await this.scanDirectory(fullPath, relativePath);
                files.push(...subFiles);
            } else if (entry.name.endsWith('.js')) {
                files.push({
                    fullPath,
                    relativePath,
                    name: entry.name
                });
            }
        }
        
        return files;
    }

    async getFileStats(filePath) {
        const stats = await fs.stat(filePath);
        const content = await fs.readFile(filePath, 'utf8');
        
        return {
            size: stats.size,
            lineCount: content.split('\n').length,
            modifiedTime: stats.mtime
        };
    }
}

module.exports = FileScanner;
```

=== File: src\utils\docs\module-parser.js (110 lines) ===

```javascript
const fs = require('fs').promises;
const ASTParser = require('./ast-parser');

class ModuleParser {
    constructor() {
        this.astParser = new ASTParser();
    }

    async parseFile(filePath, relativePath) {
        const content = await fs.readFile(filePath, 'utf8');
        
        const astResult = await this.astParser.parseFile(filePath);
        
        if (astResult) {
            return {
                path: relativePath,
                exports: astResult.exports,
                dependencies: astResult.dependencies,
                lineCount: content.split('\n').length,
                description: this.getDescription(relativePath),
                parserUsed: 'AST'
            };
        } else {
            return {
                path: relativePath,
                exports: this.extractExports(content),
                dependencies: this.extractDependencies(content),
                lineCount: content.split('\n').length,
                description: this.getDescription(relativePath),
                parserUsed: 'regex'
            };
        }
    }

    extractExports(content) {
        const exports = [];
        const match = content.match(/module\.exports\s*=\s*{([^{}]*(?:{[^{}]*}[^{}]*)*)}/);
        
        if (match) {
            const objectContent = match[1];
            const properties = objectContent
                .split(',')
                .map(prop => {
                    const colonIndex = prop.indexOf(':');
                    if (colonIndex === -1) return prop.trim();
                    return prop.slice(0, colonIndex).trim();
                })
                .map(prop => prop.replace(/['"]/g, ''))
                .filter(prop => prop && !prop.startsWith('//') && /^[a-zA-Z_$][\w$]*$/.test(prop));
            
            exports.push(...properties);
        } else {
            const singleMatch = content.match(/module\.exports\s*=\s*(\w+)/);
            if (singleMatch) {
                exports.push(singleMatch[1]);
            }
        }
        
        return exports;
    }

    extractDependencies(content) {
        const deps = new Set();
        const requireRegex = /require\(['"]([^'"]+)['"]\)/g;
        let match;
        
        while ((match = requireRegex.exec(content)) !== null) {
            const dep = match[1];
            if (!dep.startsWith('.')) {
                deps.add(dep);
            }
        }
        
        return Array.from(deps);
    }

    getDescription(relativePath) {
        const descriptions = {
            'core/config.js': 'Environment configuration management with validation',
            'core/constants.js': 'Application constants and enums',
            'core/client.js': 'Discord client initialization and setup',
            'core/shutdown.js': 'Graceful shutdown handling',
            'data/database.js': 'SQLite connection management',
            'data/operations.js': 'Generic database CRUD operations',
            'data/helpers.js': 'Database helper functions',
            'data/index.js': 'Database module exports',
            'security/permissions.js': 'Role-based permission validation',
            'security/ratelimit.js': 'Rate limiting with database storage',
            'handlers/message.js': 'Plugin-based message processing',
            'handlers/slash.js': 'Slash command handling with plugins',
            'handlers/interaction.js': 'Discord interaction processing',
            'handlers/command.js': 'Event handler registration and management',
            'handlers/audit.js': 'Audit logging and monitoring',
            'api/server.js': 'REST API server setup',
            'api/routes.js': 'API endpoint definitions',
            'api/middleware.js': 'API middleware and authentication',
            'utils/logger.js': 'File logging with rotation',
            'utils/docs-generator.js': 'Documentation generation orchestrator',
            'utils/docs/analyzer.js': 'Project structure analysis',
            'utils/docs/file-scanner.js': 'File system scanning utilities',
            'utils/docs/module-parser.js': 'Module metadata extraction',
            'utils/docs/readme-generator.js': 'README.md content generation',
            'utils/docs/writer.js': 'Documentation file writing'
        };
        
        return descriptions[relativePath] || 'Module functionality';
    }
}

module.exports = ModuleParser;
```

=== File: src\utils\docs\readme-generator.js (150 lines) ⚠️ ===

```javascript
class ReadmeGenerator {
    generate(projectData) {
        const { packageInfo, configOptions, modules } = projectData;
        return `# ${packageInfo.name}

${packageInfo.description}

A production-ready Discord bot template with plugin-based architecture, comprehensive security, and REST API management interface.

## Features

- **Plugin System**: Auto-discovery for commands, slash commands, interactions, and message handlers
- **Security**: Role-based permissions with database-backed rate limiting
- **Database**: SQLite with migration system and audit trails
- **API**: REST endpoints for external management and monitoring
- **Monitoring**: Performance benchmarking and comprehensive logging
- **Architecture**: Modular design following DRY/KISS principles

## Quick Start

\`\`\`bash
# Clone and install dependencies
npm install

# Configure environment
cp .env.template .env
# Edit .env with your bot token and settings

# Run the bot
npm start

# Development mode with hot reload
npm run dev

# Run performance benchmarks
npm test

# Generate documentation
npm run docs
\`\`\`

## Configuration

Edit \`.env\` file with the following options:

${configOptions.map(opt => `- **${opt.key}**: ${opt.example}`).join('\n')}

## Project Structure

\`\`\`
${this.generateStructure(modules)}
\`\`\`

## Plugin Development

### Command Plugin Example

\`\`\`javascript
// src/plugins/commands/hello.js
module.exports = {
    type: 'command',
    name: 'hello',
    description: 'Greet users',
    permission: null,

    async execute(message, args) {
        await message.reply(\`Hello \${message.author.username}!\`);
    }
};
\`\`\`

### Slash Command Plugin Example

\`\`\`javascript
// src/plugins/slash/ping.js
const { SlashCommandBuilder } = require('discord.js');

module.exports = {
    type: 'slash',
    name: 'ping',
    data: new SlashCommandBuilder()
        .setName('ping')
        .setDescription('Check bot latency'),

    async execute(interaction) {
        const ping = interaction.client.ws.ping;
        await interaction.reply(\`Pong! \${ping}ms\`);
    }
};
\`\`\`

## API Endpoints

The REST API provides external access to bot management:

- \`GET /health\` - System health check
- \`GET /api/stats\` - Plugin and system statistics
- \`GET /api/servers\` - List managed servers
- \`GET /api/servers/:id/config\` - Server configuration
- \`PUT /api/servers/:id/config\` - Update server config
- \`GET /api/servers/:id/audit\` - Audit logs

Authentication required via \`Authorization: Bearer <API_TOKEN>\` header.

## Database Management

The bot uses SQLite for data persistence. Manual database access:

\`\`\`bash
# Open database
sqlite3 ./data/bot.db

# View tables
.tables

# Query audit logs
SELECT * FROM audit_logs ORDER BY timestamp DESC LIMIT 10;

# Export data
.dump > backup.sql
\`\`\`

## Performance

Benchmark results show optimal performance:
- Configuration loading: < 1ms
- Database operations: < 10ms
- Permission checks: < 2ms
- Plugin loading: < 1ms

Run \`npm test\` to benchmark your environment.

## License

MIT License - see LICENSE file for details.
`;
    }
    generateStructure(modules) {
        const structure = [];
        const sorted = Array.from(modules.keys()).sort();
        sorted.forEach(modulePath => {
            const module = modules.get(modulePath);
            const indent = '  '.repeat((modulePath.match(/\//g) || []).length);
            const basename = modulePath.split('/').pop();
            structure.push(`${indent}${basename} (${module.lineCount} lines)`);
        });
        return structure.join('\n');
    }
}
module.exports = ReadmeGenerator;
```

=== File: src\utils\docs\writer.js (48 lines) ===

```javascript
const fs = require('fs').promises;
const path = require('path');

class DocsWriter {
    constructor(projectRoot, docsPath) {
        this.projectRoot = projectRoot;
        this.docsPath = docsPath;
    }

    async writeAll(docs) {
        await this.ensureDocsDirectory();
        
        await this.writeReadme(docs.readme);
        await this.writeArchitecture(docs.architecture);
        await this.writeApi(docs.api);
        
        console.log('\nDocumentation generated:');
        console.log('- README.md');
        console.log('- docs/architecture.md');
        console.log('- docs/api.md');
    }

    async ensureDocsDirectory() {
        await fs.mkdir(this.docsPath, { recursive: true });
    }

    async writeReadme(content) {
        const readmePath = path.join(this.projectRoot, 'README.md');
        await fs.writeFile(readmePath, content);
    }

    async writeArchitecture(content) {
        const archPath = path.join(this.docsPath, 'architecture.md');
        await fs.writeFile(archPath, content);
    }

    async writeApi(content) {
        const apiPath = path.join(this.docsPath, 'api.md');
        await fs.writeFile(apiPath, content);
    }

    async writeFile(filename, content) {
        const filePath = path.join(this.docsPath, filename);
        await fs.writeFile(filePath, content);
    }
}

module.exports = DocsWriter;
```

=== File: tests\benchmark.js (138 lines) ===

```javascript
const { performance } = require('perf_hooks');
const fs = require('fs').promises;
const path = require('path');
const { PATH_BASELINE, PATH_OUTPUT } = require('./result-paths');

class BenchmarkFramework {
    constructor(outputPath = PATH_OUTPUT) {
        this.results = {};
        this.baselines = {};
        this.outputPath = outputPath;
        this.baselinePath = PATH_BASELINE;
    }

    async loadBaselines() {
        try {
            const data = await fs.readFile(this.baselinePath, 'utf8');
            this.baselines = JSON.parse(data);
        } catch {
            this.baselines = {};
        }
    }

    async measureTime(fn, iterations = 1000) {
        const measurements = [];
        const sampleCount = 10;
        
        for (let i = 0; i < sampleCount; i++) {
            const start = performance.now();
            for (let j = 0; j < iterations; j++) {
                await fn();
            }
            measurements.push((performance.now() - start) / iterations);
        }
        
        measurements.sort((a, b) => a - b);
        return measurements[Math.floor(measurements.length / 2)];
    }

    measureMemory() {
        if (global.gc) global.gc();
        const usage = process.memoryUsage();
        return Math.round(usage.heapUsed / 1024 / 1024 * 100) / 100;
    }

    async testComponent(name, testFn, iterations = 1000) {
        if (['audit_logging', 'docs_generation'].includes(name)) {
            iterations = 50;
        }
        console.log(`Testing ${name}...`);
        
        const memoryBefore = this.measureMemory();
        let status = 'pass';
        let totalTime = 0;
        
        try {
            totalTime = await this.measureTime(testFn, iterations);
        } catch (err) {
            status = 'fail';
            console.log(`${name}: FAIL - ${err.message}`);
        }
        
        const memoryAfter = this.measureMemory();
        
        this.results[name] = {
            speed_ms: Math.round(totalTime * 100) / 100,
            memory_mb: memoryAfter,
            memory_delta_mb: Math.round((memoryAfter - memoryBefore) * 100) / 100,
            status: status,
            timestamp: new Date().toISOString()
        };
        
        this.checkRegression(name);
        console.log(`${name}: ${status} (${this.results[name].speed_ms}ms)`);
    }

    checkRegression(componentName) {
        const baseline = this.baselines[componentName];
        const current = this.results[componentName];
        
        if (!baseline) return;
        
        const speedDifference = current.speed_ms - baseline.speed_ms;
        const memoryDifference = current.memory_mb - baseline.memory_mb;
        
        current.baseline_comparison = {
            speed_change_ms: Math.round(speedDifference * 100) / 100,
            memory_change_mb: Math.round(memoryDifference * 100) / 100,
            baseline_speed_ms: baseline.speed_ms,
            baseline_memory_mb: baseline.memory_mb
        };
        
        if (speedDifference > 5) {
            console.warn(`⚠️ ${componentName}: Speed regression (+${speedDifference.toFixed(2)}ms)`);
        }
        if (memoryDifference > 10) {
            console.warn(`⚠️ ${componentName}: Memory regression (+${memoryDifference.toFixed(2)}MB)`);
        }
    }

    async saveResults() {
        let existingResults = {};
        try {
            const data = await fs.readFile(this.outputPath, 'utf8');
            existingResults = JSON.parse(data);
        } catch {
            // File doesn't exist or invalid JSON, start fresh
        }

        const mergedResults = { ...existingResults, ...this.results };
        
        await fs.mkdir(path.dirname(this.outputPath), { recursive: true });
        await fs.writeFile(this.outputPath, JSON.stringify(mergedResults, null, 2));
        console.log(`Results saved to ${this.outputPath}`);
    }

    async updateBaseline() {
        await fs.mkdir(path.dirname(this.baselinePath), { recursive: true });
        await fs.writeFile(this.baselinePath, JSON.stringify(this.results, null, 2));
        console.log('Baseline updated');
    }

    printSummary() {
        const components = Object.keys(this.results);
        const passed = components.filter(name => this.results[name].status === 'pass').length;
        const failed = components.length - passed;
        
        console.log(`\nTested: ${components.length}, Passed: ${passed}, Failed: ${failed}`);
        
        components.forEach(name => {
            const result = this.results[name];
            if (result.status === 'pass') {
                console.log(`${name}: ${result.speed_ms}ms, ${result.memory_per_op_mb || 0}MB`);
            }
        });
    }
}

module.exports = BenchmarkFramework;
```

=== File: tests\check-regressions.js (117 lines) ===

```javascript
const fs = require('fs').promises;
const { PATH_OUTPUT, PATH_BASELINE, PATH_PR_BASELINE } = require('./result-paths');

const SPEED_REGRESSION_THRESHOLD_MS = 5;
const MEMORY_REGRESSION_THRESHOLD_MB = 10;
const SPEED_IMPROVEMENT_THRESHOLD_MS = 2;
const MEMORY_IMPROVEMENT_THRESHOLD_MB = 5;

const SKIP_COMPONENTS = ['audit_logging', 'docs_generation'];

async function checkRegressions() {
    const resultsPath = PATH_OUTPUT;
    const isCI = process.env.CI === 'true';
    const baselinePath = isCI ? PATH_PR_BASELINE : PATH_BASELINE;

    let results, baseline;

    try {
        results = JSON.parse(await fs.readFile(resultsPath, 'utf8'));
    } catch (error) {
        console.error('Failed to read results:', error.message);
        process.exit(1);
    }

    try {
        baseline = JSON.parse(await fs.readFile(baselinePath, 'utf8'));
    } catch {
        if (isCI && process.env.GITHUB_REF === 'refs/heads/main') {
            console.log('Main branch: No baseline exists, will be created by workflow');
            process.exit(0);
        }
        if (isCI && process.env.GITHUB_REF !== 'refs/heads/main') {
            console.error('No baseline found for PR comparison. Run benchmarks on main branch first.');
            process.exit(1);
        }
        await fs.writeFile(baselinePath, JSON.stringify(results, null, 2));
        console.log(`Baseline established at ${baselinePath}`);
        process.exit(0);
    }

    const regressions = [];
    const improvements = [];

    for (const [component, result] of Object.entries(results)) {
        if (!baseline[component] || result.status !== 'pass') continue;
        if (SKIP_COMPONENTS.includes(component)) continue;

        const baselineResult = baseline[component];

        const speedChange = result.speed_ms - baselineResult.speed_ms;
        if (speedChange > SPEED_REGRESSION_THRESHOLD_MS) {
            regressions.push({
                component,
                type: 'speed',
                change: speedChange.toFixed(2),
                current: result.speed_ms,
                baseline: baselineResult.speed_ms
            });
        } else if (speedChange < -SPEED_IMPROVEMENT_THRESHOLD_MS) {
            improvements.push({
                component,
                type: 'speed',
                improvement: Math.abs(speedChange).toFixed(2)
            });
        }

        const memoryChange = result.memory_mb - baselineResult.memory_mb;
        if (memoryChange > MEMORY_REGRESSION_THRESHOLD_MB) {
            regressions.push({
                component,
                type: 'memory',
                change: memoryChange.toFixed(2),
                current: result.memory_mb,
                baseline: baselineResult.memory_mb
            });
        } else if (memoryChange < -MEMORY_IMPROVEMENT_THRESHOLD_MB) {
            improvements.push({
                component,
                type: 'memory',
                improvement: Math.abs(memoryChange).toFixed(2)
            });
        }
    }

    if (improvements.length > 0) {
        console.log('Performance improvements detected:');
        improvements.forEach(imp => {
            const unit = imp.type === 'speed' ? 'ms' : 'MB';
            console.log(`  ✓ ${imp.component}: ${imp.type} improved by ${imp.improvement}${unit}`);
        });
    }

    if (regressions.length > 0) {
        console.log('Performance regressions detected:');
        regressions.forEach(reg => {
            const unit = reg.type === 'speed' ? 'ms' : 'MB';
            console.log(`  ✗ ${reg.component}: ${reg.type} regression +${reg.change}${unit} (${reg.current} vs ${reg.baseline})`);
        });
        console.log(`\nFailed: ${regressions.length} regressions exceed thresholds`);
        console.log(`Speed threshold: ${SPEED_REGRESSION_THRESHOLD_MS}ms, Memory threshold: ${MEMORY_REGRESSION_THRESHOLD_MB}MB`);
        process.exit(1);
    }

    if (improvements.length > 0) {
        console.log('Updating baseline with improvements...');
        await fs.writeFile(baselinePath, JSON.stringify(results, null, 2));
    }

    console.log('All performance checks passed');
    process.exit(0);
}

if (require.main === module) {
    checkRegressions().catch(console.error);
}

module.exports = { checkRegressions };
```

=== File: tests\result-paths.js (19 lines) ===

```javascript
const path = require('path');

const PATH_BASELINE = path.join(__dirname, 'data', 'baseline.json');
const PATH_PR_BASELINE = path.join(__dirname, 'data', 'pr-baseline.json');
const PATH_RESULTS = path.join(__dirname, 'data', 'results.json');
const PATH_PR_RESULTS = path.join(__dirname, 'data', 'pr-results.json');
const PATH_STRESS = path.join(__dirname, 'data', 'stress-results.json');

const isCI = process.env.CI === 'true';
const PATH_OUTPUT = isCI ? PATH_PR_RESULTS : PATH_RESULTS;

module.exports = {
    PATH_BASELINE,
    PATH_PR_BASELINE,
    PATH_RESULTS,
    PATH_PR_RESULTS,
    PATH_OUTPUT,
    PATH_STRESS
}
```

=== File: tests\run-benchmarks.js (32 lines) ===

```javascript
const BenchmarkFramework = require('./benchmark.js');
const coreTests = require('./suites/core-tests');
const dataTests = require('./suites/data-tests');
const securityTests = require('./suites/security-tests');
const handlerTests = require('./suites/handler-tests');

async function runAllBenchmarks() {
    const benchmark = new BenchmarkFramework();
    await benchmark.loadBaselines();

    console.log('Starting benchmarks\n');

    await coreTests.run(benchmark);
    await dataTests.run(benchmark);
    await securityTests.run(benchmark);
    await handlerTests.run(benchmark);

    benchmark.printSummary();
    await benchmark.saveResults();

    if (process.argv.includes('--update-baseline')) {
        await benchmark.updateBaseline();
    }

    process.exit(0);
}

if (require.main === module) {
    runAllBenchmarks().catch(console.error);
}

module.exports = { runAllBenchmarks };
```

=== File: tests\run-stress-tests.js (48 lines) ===

```javascript
const StressTestFramework = require('./stress');
const { runDatabaseStressTests } = require('./stress/stress-database');
const { runSecurityStressTests } = require('./stress/stress-security');
const { runPluginStressTests } = require('./stress/stress-plugins');
const { runApiStressTests } = require('./stress/stress-api');
const { runMemoryLeakTests } = require('./stress/stress-memory');
const { validateCriticalFailures } = require('./stress/stress-validators');

async function runAllStressTests() {
    console.log('Starting stress testing suite\n');
    
    const stress = new StressTestFramework();
    
    try {
        await runDatabaseStressTests(stress);
        await runSecurityStressTests(stress);
        await runPluginStressTests(stress);
        await runApiStressTests(stress);
        await runMemoryLeakTests(stress);
        
        stress.printSummary();
        await stress.saveResults();
        
        const criticalFailures = validateCriticalFailures(stress.results);
        
        if (criticalFailures.length > 0) {
            console.log('\n⚠️  CRITICAL ISSUES DETECTED:');
            criticalFailures.forEach(([name, result]) => {
                console.log(`  ${name}: ${JSON.stringify(result, null, 2)}`);
            });
            process.exit(1);
        } else {
            console.log('\n✅ All stress tests passed');
        }
        
    } catch (error) {
        console.error('Stress testing failed:', error);
        process.exit(1);
    }
    
    process.exit(0);
}

if (require.main === module) {
    runAllStressTests().catch(console.error);
}

module.exports = { runAllStressTests };
```

=== File: tests\stress.js (108 lines) ===

```javascript
const { performance } = require('perf_hooks');
const fs = require('fs').promises;
const path = require('path');
const { PATH_STRESS } = require('./result-paths');

class StressTestFramework {
    constructor() {
        this.results = {};
        this.outputPath = PATH_STRESS
        this.isRunning = false;
    }

    async runConcurrentTest(name, testFn, concurrency, duration) {
        console.log(`Stress testing ${name} (${concurrency} concurrent, ${duration}ms)`);
        
        const results = { operations: 0, errors: 0, memoryStart: this.getMemoryUsage(), memoryPeak: 0 };
        const responseTimes = [];
        
        this.isRunning = true;
        const workers = [];
        for (let i = 0; i < concurrency; i++) {
            workers.push(this.createWorker(testFn, duration, results, responseTimes));
        }
        
        const startTime = performance.now();
        await Promise.all(workers);
        const totalTime = performance.now() - startTime;
        
        results.opsPerSecond = (results.operations / totalTime) * 1000;
        results.errorRate = (results.errors / results.operations) * 100;
        results.avgResponseTime = responseTimes.reduce((a, b) => a + b, 0) / responseTimes.length;
        results.memoryGrowth = this.getMemoryUsage() - results.memoryStart;
        
        this.results[name] = results;
        this.isRunning = false;
        
        console.log(`${name}: ${results.operations} ops, ${results.opsPerSecond.toFixed(2)} ops/sec`);
        return results;
    }

    async createWorker(testFn, duration, results, responseTimes) {
        const endTime = performance.now() + duration;
        
        while (performance.now() < endTime && this.isRunning) {
            const opStart = performance.now();
            
            try {
                await testFn();
                results.operations++;
                responseTimes.push(performance.now() - opStart);
            } catch (error) {
                results.errors++;
            }
        }
    }

    async runSustainedTest(name, testFn, duration) {
        console.log(`Sustained test ${name} (${duration}ms)`);
        
        const results = { operations: 0, errors: 0, memoryStart: this.getMemoryUsage() };
        const endTime = performance.now() + duration;
        
        while (performance.now() < endTime) {
            const opStart = performance.now();
            
            try {
                await testFn();
                results.operations++;
            } catch (error) {
                results.errors++;
            }
            
            await new Promise(resolve => setTimeout(resolve, 10));
        }
        
        results.opsPerSecond = (results.operations / duration) * 1000;
        results.errorRate = (results.errors / results.operations) * 100;
        results.memoryGrowth = this.getMemoryUsage() - results.memoryStart;
        
        this.results[name] = results;
        console.log(`${name}: ${results.operations} ops, ${results.opsPerSecond.toFixed(2)} ops/sec`);
        return results;
    }

    getMemoryUsage() {
        return Math.round(process.memoryUsage().heapUsed / 1024 / 1024 * 100) / 100;
    }

    async saveResults() {
        await fs.mkdir(path.dirname(this.outputPath), { recursive: true });
        await fs.writeFile(this.outputPath, JSON.stringify(this.results, null, 2));
        console.log(`Stress test results saved to ${this.outputPath}`);
    }

    printSummary() {
        console.log('\n=== STRESS TEST SUMMARY ===');
        
        Object.entries(this.results).forEach(([name, result]) => {
            console.log(`\n${name}:`);
            console.log(`  Operations: ${result.operations}`);
            console.log(`  Ops/sec: ${result.opsPerSecond?.toFixed(2) || 'N/A'}`);
            console.log(`  Error rate: ${result.errorRate?.toFixed(2) || 0}%`);
            console.log(`  Memory growth: ${result.memoryGrowth?.toFixed(2) || 0}MB`);
        });
    }
}

module.exports = StressTestFramework;
```

=== File: tests\data\baseline.json (197 lines) ===

```json
{
  "config_loading": {
    "speed_ms": 0.38,
    "memory_mb": 81.92,
    "memory_delta_mb": 77.14,
    "status": "pass",
    "timestamp": "2025-09-03T20:26:27.092Z",
    "baseline_comparison": {
      "speed_change_percent": 0,
      "memory_change_percent": 0.23,
      "baseline_speed_ms": 0.38,
      "baseline_memory_mb": 81.73
    }
  },
  "constants_access": {
    "speed_ms": 0.03,
    "memory_mb": 69.6,
    "memory_delta_mb": -12.33,
    "status": "pass",
    "timestamp": "2025-09-03T20:26:29.764Z",
    "baseline_comparison": {
      "speed_change_percent": 0,
      "memory_change_percent": 0.26,
      "baseline_speed_ms": 0.03,
      "baseline_memory_mb": 69.42
    }
  },
  "client_initialization": {
    "speed_ms": 0.65,
    "memory_mb": 214.05,
    "memory_delta_mb": 144.44,
    "status": "pass",
    "timestamp": "2025-09-03T20:26:37.124Z",
    "baseline_comparison": {
      "speed_change_percent": -1.52,
      "memory_change_percent": -0.34,
      "baseline_speed_ms": 0.66,
      "baseline_memory_mb": 214.78
    }
  },
  "shutdown_preparation": {
    "speed_ms": 0.03,
    "memory_mb": 204.15,
    "memory_delta_mb": -9.91,
    "status": "pass",
    "timestamp": "2025-09-03T20:26:37.769Z",
    "baseline_comparison": {
      "speed_change_percent": 0,
      "memory_change_percent": -0.41,
      "baseline_speed_ms": 0.03,
      "baseline_memory_mb": 205
    }
  },
  "real_db_init": {
    "speed_ms": 0.85,
    "memory_mb": 215.62,
    "memory_delta_mb": 11.44,
    "status": "pass",
    "timestamp": "2025-09-03T20:26:38.626Z",
    "baseline_comparison": {
      "speed_change_percent": -1.16,
      "memory_change_percent": -0.33,
      "baseline_speed_ms": 0.86,
      "baseline_memory_mb": 216.33
    }
  },
  "real_db_operations": {
    "speed_ms": 8.47,
    "memory_mb": 195.46,
    "memory_delta_mb": -20.16,
    "status": "pass",
    "timestamp": "2025-09-03T20:26:55.693Z",
    "baseline_comparison": {
      "speed_change_percent": 8.17,
      "memory_change_percent": -0.21,
      "baseline_speed_ms": 7.83,
      "baseline_memory_mb": 195.88
    }
  },
  "permission_check": {
    "speed_ms": 0,
    "memory_mb": 196.78,
    "memory_delta_mb": 1.29,
    "status": "pass",
    "timestamp": "2025-09-03T20:26:55.702Z",
    "baseline_comparison": {
      "speed_change_percent": null,
      "memory_change_percent": 0.32,
      "baseline_speed_ms": 0,
      "baseline_memory_mb": 196.15
    }
  },
  "admin_permission_check": {
    "speed_ms": 0,
    "memory_mb": 196.79,
    "memory_delta_mb": 0,
    "status": "pass",
    "timestamp": "2025-09-03T20:26:55.707Z",
    "baseline_comparison": {
      "speed_change_percent": null,
      "memory_change_percent": 0.73,
      "baseline_speed_ms": 0,
      "baseline_memory_mb": 195.36
    }
  },
  "rate_limit_check": {
    "speed_ms": 6.59,
    "memory_mb": 197.85,
    "memory_delta_mb": 1.01,
    "status": "pass",
    "timestamp": "2025-09-03T20:28:02.256Z",
    "baseline_comparison": {
      "speed_change_percent": 13.62,
      "memory_change_percent": -0.41,
      "baseline_speed_ms": 5.8,
      "baseline_memory_mb": 198.67
    }
  },
  "rate_limit_cleanup": {
    "speed_ms": 0.17,
    "memory_mb": 198.79,
    "memory_delta_mb": 0.92,
    "status": "pass",
    "timestamp": "2025-09-03T20:28:02.605Z",
    "baseline_comparison": {
      "speed_change_percent": 6.25,
      "memory_change_percent": 0.37,
      "baseline_speed_ms": 0.16,
      "baseline_memory_mb": 198.06
    }
  },
  "command_parsing": {
    "speed_ms": 0,
    "memory_mb": 204.46,
    "memory_delta_mb": 7.23,
    "status": "pass",
    "timestamp": "2025-09-03T20:28:02.678Z",
    "baseline_comparison": {
      "speed_change_percent": null,
      "memory_change_percent": -0.36,
      "baseline_speed_ms": 0,
      "baseline_memory_mb": 205.2
    }
  },
  "plugin_loading": {
    "speed_ms": 0.04,
    "memory_mb": 203.65,
    "memory_delta_mb": -0.81,
    "status": "pass",
    "timestamp": "2025-09-03T20:28:02.899Z",
    "baseline_comparison": {
      "speed_change_percent": -20,
      "memory_change_percent": -0.35,
      "baseline_speed_ms": 0.05,
      "baseline_memory_mb": 204.37
    }
  },
  "audit_logging": {
    "speed_ms": 185.89,
    "memory_mb": 203.58,
    "memory_delta_mb": -0.08,
    "status": "pass",
    "timestamp": "2025-09-03T20:29:34.578Z",
    "baseline_comparison": {
      "speed_change_percent": 11.73,
      "memory_change_percent": 0.03,
      "baseline_speed_ms": 166.37,
      "baseline_memory_mb": 203.51
    }
  },
  "api_server_lifecycle": {
    "speed_ms": 0.05,
    "memory_mb": 203.16,
    "memory_delta_mb": -0.43,
    "status": "pass",
    "timestamp": "2025-09-03T20:29:34.633Z",
    "baseline_comparison": {
      "speed_change_percent": 0,
      "memory_change_percent": 0.04,
      "baseline_speed_ms": 0.05,
      "baseline_memory_mb": 203.07
    }
  },
  "docs_generation": {
    "speed_ms": 20.81,
    "memory_mb": 200.8,
    "memory_delta_mb": -2.37,
    "status": "pass",
    "timestamp": "2025-09-03T20:29:45.401Z",
    "baseline_comparison": {
      "speed_change_percent": -0.14,
      "memory_change_percent": -1.95,
      "baseline_speed_ms": 20.84,
      "baseline_memory_mb": 204.8
    }
  }
}
```

=== File: tests\data\pr-baseline.json (197 lines) ===

```json
{
  "config_loading": {
    "speed_ms": 0.28,
    "memory_mb": 78.41,
    "memory_delta_mb": 75.02,
    "status": "pass",
    "timestamp": "2025-09-03T21:39:25.808Z",
    "baseline_comparison": {
      "speed_change_ms": -0.1,
      "memory_change_mb": -3.51,
      "baseline_speed_ms": 0.38,
      "baseline_memory_mb": 81.92
    }
  },
  "constants_access": {
    "speed_ms": 0.03,
    "memory_mb": 78.43,
    "memory_delta_mb": 0.03,
    "status": "pass",
    "timestamp": "2025-09-03T21:39:29.145Z",
    "baseline_comparison": {
      "speed_change_ms": 0,
      "memory_change_mb": 8.83,
      "baseline_speed_ms": 0.03,
      "baseline_memory_mb": 69.6
    }
  },
  "client_initialization": {
    "speed_ms": 0.33,
    "memory_mb": 249.97,
    "memory_delta_mb": 171.54,
    "status": "pass",
    "timestamp": "2025-09-03T21:39:33.021Z",
    "baseline_comparison": {
      "speed_change_ms": -0.32,
      "memory_change_mb": 35.92,
      "baseline_speed_ms": 0.65,
      "baseline_memory_mb": 214.05
    }
  },
  "shutdown_preparation": {
    "speed_ms": 0.04,
    "memory_mb": 249.87,
    "memory_delta_mb": -0.02,
    "status": "pass",
    "timestamp": "2025-09-03T21:39:34.041Z",
    "baseline_comparison": {
      "speed_change_ms": 0.01,
      "memory_change_mb": 45.72,
      "baseline_speed_ms": 0.03,
      "baseline_memory_mb": 204.15
    }
  },
  "real_db_init": {
    "speed_ms": 0.48,
    "memory_mb": 250.01,
    "memory_delta_mb": 0.15,
    "status": "pass",
    "timestamp": "2025-09-03T21:39:34.810Z",
    "baseline_comparison": {
      "speed_change_ms": -0.37,
      "memory_change_mb": 34.39,
      "baseline_speed_ms": 0.85,
      "baseline_memory_mb": 215.62
    }
  },
  "real_db_operations": {
    "speed_ms": 2.18,
    "memory_mb": 250.18,
    "memory_delta_mb": -0.06,
    "status": "pass",
    "timestamp": "2025-09-03T21:39:39.521Z",
    "baseline_comparison": {
      "speed_change_ms": -6.29,
      "memory_change_mb": 54.72,
      "baseline_speed_ms": 8.47,
      "baseline_memory_mb": 195.46
    }
  },
  "permission_check": {
    "speed_ms": 0,
    "memory_mb": 250.17,
    "memory_delta_mb": 0.01,
    "status": "pass",
    "timestamp": "2025-09-03T21:39:39.779Z",
    "baseline_comparison": {
      "speed_change_ms": 0,
      "memory_change_mb": 53.39,
      "baseline_speed_ms": 0,
      "baseline_memory_mb": 196.78
    }
  },
  "admin_permission_check": {
    "speed_ms": 0,
    "memory_mb": 250.17,
    "memory_delta_mb": 0,
    "status": "pass",
    "timestamp": "2025-09-03T21:39:40.035Z",
    "baseline_comparison": {
      "speed_change_ms": 0,
      "memory_change_mb": 53.38,
      "baseline_speed_ms": 0,
      "baseline_memory_mb": 196.79
    }
  },
  "rate_limit_check": {
    "speed_ms": 1.57,
    "memory_mb": 250.26,
    "memory_delta_mb": 0.08,
    "status": "pass",
    "timestamp": "2025-09-03T21:39:55.886Z",
    "baseline_comparison": {
      "speed_change_ms": -5.02,
      "memory_change_mb": 52.41,
      "baseline_speed_ms": 6.59,
      "baseline_memory_mb": 197.85
    }
  },
  "rate_limit_cleanup": {
    "speed_ms": 0.14,
    "memory_mb": 250.26,
    "memory_delta_mb": 0.01,
    "status": "pass",
    "timestamp": "2025-09-03T21:39:56.392Z",
    "baseline_comparison": {
      "speed_change_ms": -0.03,
      "memory_change_mb": 51.47,
      "baseline_speed_ms": 0.17,
      "baseline_memory_mb": 198.79
    }
  },
  "command_parsing": {
    "speed_ms": 0,
    "memory_mb": 250.28,
    "memory_delta_mb": 0.01,
    "status": "pass",
    "timestamp": "2025-09-03T21:39:56.691Z",
    "baseline_comparison": {
      "speed_change_ms": 0,
      "memory_change_mb": 45.82,
      "baseline_speed_ms": 0,
      "baseline_memory_mb": 204.46
    }
  },
  "plugin_loading": {
    "speed_ms": 0.01,
    "memory_mb": 250.32,
    "memory_delta_mb": 0.04,
    "status": "pass",
    "timestamp": "2025-09-03T21:39:56.980Z",
    "baseline_comparison": {
      "speed_change_ms": -0.03,
      "memory_change_mb": 46.67,
      "baseline_speed_ms": 0.04,
      "baseline_memory_mb": 203.65
    }
  },
  "audit_logging": {
    "speed_ms": 2.14,
    "memory_mb": 250.37,
    "memory_delta_mb": 0.06,
    "status": "pass",
    "timestamp": "2025-09-03T21:39:58.328Z",
    "baseline_comparison": {
      "speed_change_ms": -183.75,
      "memory_change_mb": 46.79,
      "baseline_speed_ms": 185.89,
      "baseline_memory_mb": 203.58
    }
  },
  "api_server_lifecycle": {
    "speed_ms": 0.01,
    "memory_mb": 250.38,
    "memory_delta_mb": 0.01,
    "status": "pass",
    "timestamp": "2025-09-03T21:39:58.586Z",
    "baseline_comparison": {
      "speed_change_ms": -0.04,
      "memory_change_mb": 47.22,
      "baseline_speed_ms": 0.05,
      "baseline_memory_mb": 203.16
    }
  },
  "docs_generation": {
    "speed_ms": 17.78,
    "memory_mb": 253.54,
    "memory_delta_mb": 3.16,
    "status": "pass",
    "timestamp": "2025-09-03T21:40:07.935Z",
    "baseline_comparison": {
      "speed_change_ms": -3.03,
      "memory_change_mb": 52.74,
      "baseline_speed_ms": 20.81,
      "baseline_memory_mb": 200.8
    }
  }
}
```

=== File: tests\data\pr-results.json (0 lines) ===

```json

```

=== File: tests\data\results.json (197 lines) ===

```json
{
  "config_loading": {
    "speed_ms": 0.38,
    "memory_mb": 75.23,
    "memory_delta_mb": 70.45,
    "status": "pass",
    "timestamp": "2025-09-03T20:31:17.286Z",
    "baseline_comparison": {
      "speed_change_ms": 0,
      "memory_change_mb": -6.69,
      "baseline_speed_ms": 0.38,
      "baseline_memory_mb": 81.92
    }
  },
  "constants_access": {
    "speed_ms": 0.03,
    "memory_mb": 77.51,
    "memory_delta_mb": 2.26,
    "status": "pass",
    "timestamp": "2025-09-03T20:31:19.977Z",
    "baseline_comparison": {
      "speed_change_ms": 0,
      "memory_change_mb": 7.91,
      "baseline_speed_ms": 0.03,
      "baseline_memory_mb": 69.6
    }
  },
  "client_initialization": {
    "speed_ms": 0.67,
    "memory_mb": 206.91,
    "memory_delta_mb": 129.4,
    "status": "pass",
    "timestamp": "2025-09-03T20:31:27.515Z",
    "baseline_comparison": {
      "speed_change_ms": 0.02,
      "memory_change_mb": -7.14,
      "baseline_speed_ms": 0.65,
      "baseline_memory_mb": 214.05
    }
  },
  "shutdown_preparation": {
    "speed_ms": 0.03,
    "memory_mb": 210.74,
    "memory_delta_mb": 3.81,
    "status": "pass",
    "timestamp": "2025-09-03T20:31:28.165Z",
    "baseline_comparison": {
      "speed_change_ms": 0,
      "memory_change_mb": 6.59,
      "baseline_speed_ms": 0.03,
      "baseline_memory_mb": 204.15
    }
  },
  "real_db_init": {
    "speed_ms": 0.9,
    "memory_mb": 209.21,
    "memory_delta_mb": -1.56,
    "status": "pass",
    "timestamp": "2025-09-03T20:31:29.054Z",
    "baseline_comparison": {
      "speed_change_ms": 0.05,
      "memory_change_mb": -6.41,
      "baseline_speed_ms": 0.85,
      "baseline_memory_mb": 215.62
    }
  },
  "real_db_operations": {
    "speed_ms": 8.55,
    "memory_mb": 196.16,
    "memory_delta_mb": -13.05,
    "status": "pass",
    "timestamp": "2025-09-03T20:31:46.097Z",
    "baseline_comparison": {
      "speed_change_ms": 0.08,
      "memory_change_mb": 0.7,
      "baseline_speed_ms": 8.47,
      "baseline_memory_mb": 195.46
    }
  },
  "permission_check": {
    "speed_ms": 0,
    "memory_mb": 195.38,
    "memory_delta_mb": -0.81,
    "status": "pass",
    "timestamp": "2025-09-03T20:31:46.105Z",
    "baseline_comparison": {
      "speed_change_ms": 0,
      "memory_change_mb": -1.4,
      "baseline_speed_ms": 0,
      "baseline_memory_mb": 196.78
    }
  },
  "admin_permission_check": {
    "speed_ms": 0,
    "memory_mb": 195.56,
    "memory_delta_mb": 0.18,
    "status": "pass",
    "timestamp": "2025-09-03T20:31:46.110Z",
    "baseline_comparison": {
      "speed_change_ms": 0,
      "memory_change_mb": -1.23,
      "baseline_speed_ms": 0,
      "baseline_memory_mb": 196.79
    }
  },
  "rate_limit_check": {
    "speed_ms": 6.59,
    "memory_mb": 196.71,
    "memory_delta_mb": 1.11,
    "status": "pass",
    "timestamp": "2025-09-03T20:32:53.784Z",
    "baseline_comparison": {
      "speed_change_ms": 0,
      "memory_change_mb": -1.14,
      "baseline_speed_ms": 6.59,
      "baseline_memory_mb": 197.85
    }
  },
  "rate_limit_cleanup": {
    "speed_ms": 0.2,
    "memory_mb": 197.7,
    "memory_delta_mb": 0.98,
    "status": "pass",
    "timestamp": "2025-09-03T20:32:54.184Z",
    "baseline_comparison": {
      "speed_change_ms": 0.03,
      "memory_change_mb": -1.09,
      "baseline_speed_ms": 0.17,
      "baseline_memory_mb": 198.79
    }
  },
  "command_parsing": {
    "speed_ms": 0,
    "memory_mb": 204.78,
    "memory_delta_mb": 7.07,
    "status": "pass",
    "timestamp": "2025-09-03T20:32:54.264Z",
    "baseline_comparison": {
      "speed_change_ms": 0,
      "memory_change_mb": 0.32,
      "baseline_speed_ms": 0,
      "baseline_memory_mb": 204.46
    }
  },
  "plugin_loading": {
    "speed_ms": 0.05,
    "memory_mb": 204.06,
    "memory_delta_mb": -0.72,
    "status": "pass",
    "timestamp": "2025-09-03T20:32:54.520Z",
    "baseline_comparison": {
      "speed_change_ms": 0.01,
      "memory_change_mb": 0.41,
      "baseline_speed_ms": 0.04,
      "baseline_memory_mb": 203.65
    }
  },
  "audit_logging": {
    "speed_ms": 184.05,
    "memory_mb": 202.41,
    "memory_delta_mb": -1.65,
    "status": "pass",
    "timestamp": "2025-09-03T20:34:27.066Z",
    "baseline_comparison": {
      "speed_change_ms": -1.84,
      "memory_change_mb": -1.17,
      "baseline_speed_ms": 185.89,
      "baseline_memory_mb": 203.58
    }
  },
  "api_server_lifecycle": {
    "speed_ms": 0.08,
    "memory_mb": 202.94,
    "memory_delta_mb": 0.53,
    "status": "pass",
    "timestamp": "2025-09-03T20:34:27.139Z",
    "baseline_comparison": {
      "speed_change_ms": 0.03,
      "memory_change_mb": -0.22,
      "baseline_speed_ms": 0.05,
      "baseline_memory_mb": 203.16
    }
  },
  "docs_generation": {
    "speed_ms": 24.96,
    "memory_mb": 202.86,
    "memory_delta_mb": -0.09,
    "status": "pass",
    "timestamp": "2025-09-03T20:34:40.117Z",
    "baseline_comparison": {
      "speed_change_ms": 4.15,
      "memory_change_mb": 2.06,
      "baseline_speed_ms": 20.81,
      "baseline_memory_mb": 200.8
    }
  }
}
```

=== File: tests\data\stress-results.json (97 lines) ===

```json
{
  "db_concurrent_writes": {
    "operations": 871,
    "errors": 0,
    "memoryStart": 21.08,
    "memoryPeak": 0,
    "opsPerSecond": 173.3098149327756,
    "errorRate": 0,
    "avgResponseTime": 57.646246039035546,
    "memoryGrowth": 2.360000000000003
  },
  "db_concurrent_reads": {
    "operations": 75,
    "errors": 0,
    "memoryStart": 23.44,
    "memoryPeak": 0,
    "opsPerSecond": 11.392985384470721,
    "errorRate": 0,
    "avgResponseTime": 1563.723512000001,
    "memoryGrowth": 44.07000000000001
  },
  "db_sustained_operations": {
    "operations": 399,
    "errors": 0,
    "memoryStart": 67.54,
    "opsPerSecond": 39.9,
    "errorRate": 0,
    "memoryGrowth": 8.429999999999993
  },
  "rate_limit_concurrent": {
    "operations": 391,
    "errors": 0,
    "memoryStart": 76.04,
    "memoryPeak": 0,
    "opsPerSecond": 128.76330518477474,
    "errorRate": 0,
    "avgResponseTime": 116.10876445012778,
    "memoryGrowth": -60.470000000000006
  },
  "permission_check_concurrent": {
    "operations": 6602749,
    "errors": 0,
    "memoryStart": 15.59,
    "memoryPeak": 0,
    "opsPerSecond": 3288785.1947138985,
    "errorRate": 0,
    "avgResponseTime": 0.01507224931618185,
    "memoryGrowth": 173.06
  },
  "rate_limit_boundaries": {
    "allowedCount": 10,
    "deniedCount": 10,
    "rateLimitWorking": true
  },
  "plugin_loading_concurrent": {
    "operations": 905923,
    "errors": 0,
    "memoryStart": 174.67,
    "memoryPeak": 0,
    "opsPerSecond": 452960.72996675957,
    "errorRate": 0,
    "avgResponseTime": 0.055048884066248235,
    "memoryGrowth": 43.400000000000006
  },
  "message_parsing_sustained": {
    "operations": 508,
    "errors": 0,
    "memoryStart": 218.07,
    "opsPerSecond": 63.5,
    "errorRate": 0,
    "memoryGrowth": -202.01999999999998
  },
  "api_lifecycle_concurrent": {
    "operations": 6682149,
    "errors": 0,
    "memoryStart": 16.08,
    "memoryPeak": 0,
    "opsPerSecond": 2227377.2830649717,
    "errorRate": 0,
    "avgResponseTime": 0.0021063294458101415,
    "memoryGrowth": 136.10000000000002
  },
  "memory_leak_detection": {
    "operations": 954,
    "errors": 0,
    "memoryStart": 152.19,
    "opsPerSecond": 63.6,
    "errorRate": 0,
    "memoryGrowth": -9.199999999999989
  },
  "memory_leak_analysis": {
    "initialMemory": 152.19,
    "finalMemory": 142.99,
    "potentialLeak": -9.199999999999989,
    "leakDetected": false
  }
}
```

=== File: tests\helpers\index.js (113 lines) ===

```javascript
class MockGenerator {
    static generateId() {
        return Math.random().toString().slice(2, 20);
    }

    static generateMessage(guildId, userId) {
        return {
            id: this.generateId(),
            content: `Test message ${Math.floor(Math.random() * 1000)}`,
            author: { id: userId, username: `user${userId.slice(-4)}`, bot: false },
            guild: { id: guildId },
            channel: { id: this.generateId() },
            createdTimestamp: Date.now()
        };
    }

    static generateInteraction(guildId, userId) {
        return {
            id: this.generateId(),
            user: { id: userId, username: `user${userId.slice(-4)}` },
            guild: { id: guildId },
            channel: { id: this.generateId() },
            commandName: 'test',
            options: { data: [] },
            createdTimestamp: Date.now()
        };
    }

    static generateServerData(guildId) {
        return {
            guild_id: guildId,
            config: JSON.stringify({
                prefix: '!',
                enabled: true,
                permissions: ['manage_messages']
            }),
            created_at: new Date().toISOString()
        };
    }
}

class MockDatabase {
    constructor() {
        this.servers = new Map();
        this.users = new Map();
        this.audit_logs = [];
        this.rate_limits = new Map();
    }

    async insert(table, data) {
        await new Promise(resolve => setTimeout(resolve, Math.random() * 2));
        
        switch(table) {
            case 'servers':
                this.servers.set(data.guild_id, data);
                break;
            case 'users':
                this.users.set(`${data.guild_id}_${data.user_id}`, data);
                break;
            case 'audit_logs':
                this.audit_logs.push({...data, id: Date.now()});
                break;
            case 'rate_limits':
                this.rate_limits.set(data.identifier, data);
                break;
        }
        return true;
    }

    async select(table, where = {}) {
        await new Promise(resolve => setTimeout(resolve, Math.random()));
        
        switch(table) {
            case 'servers':
                return where.guild_id ? this.servers.get(where.guild_id) : Array.from(this.servers.values());
            case 'users':
                return where.guild_id && where.user_id ? 
                    this.users.get(`${where.guild_id}_${where.user_id}`) : 
                    Array.from(this.users.values());
            case 'audit_logs':
                return this.audit_logs.filter(log => !where.guild_id || log.guild_id === where.guild_id);
            case 'rate_limits':
                return where.identifier ? this.rate_limits.get(where.identifier) : Array.from(this.rate_limits.values());
        }
        return null;
    }

    cleanup() {
        this.servers.clear();
        this.users.clear();
        this.audit_logs = [];
        this.rate_limits.clear();
    }
}

function withCleanDatabase(testFn) {
    return async function() {
        const mockDb = new MockDatabase();
        try {
            await testFn(mockDb);
        } finally {
            mockDb.cleanup();
        }
    };
}

function assertSpeedUnder(actualMs, maxMs, componentName) {
    if (actualMs > maxMs) {
        throw new Error(`${componentName} too slow: ${actualMs}ms > ${maxMs}ms`);
    }
}

module.exports = { MockGenerator, MockDatabase, withCleanDatabase, assertSpeedUnder };
```

=== File: tests\stress\stress-api.js (21 lines) ===

```javascript
const { logTestStart } = require('./stress-lifecycle');
const operations = require('./stress-operations');
const STRESS_CONFIG = require('./stress-config');

async function runApiStressTests(stress) {
    logTestStart('API');
    
    process.env.API_TOKEN = 'test_stress_token';
    process.env.API_ENABLED = 'true';
    
    const { API } = STRESS_CONFIG;
    
    await stress.runConcurrentTest(
        'api_lifecycle_concurrent',
        operations.apiLifecycle,
        API.LIFECYCLE_CONCURRENT.concurrency,
        API.LIFECYCLE_CONCURRENT.duration
    );
}

module.exports = { runApiStressTests };
```

=== File: tests\stress\stress-config.js (29 lines) ===

```javascript
const STRESS_CONFIG = Object.freeze({
    DATABASE: {
        CONCURRENT_WRITES: { concurrency: 10, duration: 5000 },
        CONCURRENT_READS: { concurrency: 20, duration: 5000 },
        SUSTAINED_OPERATIONS: { duration: 10000 }
    },
    SECURITY: {
        RATE_LIMIT_CONCURRENT: { concurrency: 15, duration: 3000 },
        PERMISSION_CHECK_CONCURRENT: { concurrency: 50, duration: 2000 },
        RATE_LIMIT_BOUNDARY_MAX: 10
    },
    PLUGIN: {
        LOADING_CONCURRENT: { concurrency: 25, duration: 2000 },
        MESSAGE_PARSING_SUSTAINED: { duration: 8000 }
    },
    API: {
        LIFECYCLE_CONCURRENT: { concurrency: 5, duration: 3000 }
    },
    MEMORY: {
        LEAK_DETECTION: { duration: 15000, arraySize: 100 }
    },
    THRESHOLDS: {
        ERROR_RATE: 5,
        MEMORY_GROWTH: 20,
        MEMORY_LEAK: 10
    }
});

module.exports = STRESS_CONFIG;
```

=== File: tests\stress\stress-database.js (33 lines) ===

```javascript
const { withDatabase, logTestStart } = require('./stress-lifecycle');
const operations = require('./stress-operations');
const STRESS_CONFIG = require('./stress-config');

async function runDatabaseStressTests(stress) {
    logTestStart('database');
    
    await withDatabase(async () => {
        const { DATABASE } = STRESS_CONFIG;
        
        await stress.runConcurrentTest(
            'db_concurrent_writes', 
            operations.dbInsert,
            DATABASE.CONCURRENT_WRITES.concurrency,
            DATABASE.CONCURRENT_WRITES.duration
        );
        
        await stress.runConcurrentTest(
            'db_concurrent_reads',
            operations.dbSelect,
            DATABASE.CONCURRENT_READS.concurrency,
            DATABASE.CONCURRENT_READS.duration
        );
        
        await stress.runSustainedTest(
            'db_sustained_operations',
            operations.dbInsertAndSelect,
            DATABASE.SUSTAINED_OPERATIONS.duration
        );
    });
}

module.exports = { runDatabaseStressTests };
```

=== File: tests\stress\stress-lifecycle.js (19 lines) ===

```javascript
const { initializeDatabase, closeDatabase } = require('../../src/data');

async function withDatabase(testFn) {
    await initializeDatabase();
    try {
        return await testFn();
    } finally {
        await closeDatabase();
    }
}

function logTestStart(name) {
    console.log(`Running ${name} stress tests...`);
}

module.exports = {
    withDatabase,
    logTestStart
};
```

=== File: tests\stress\stress-memory.js (30 lines) ===

```javascript
const { logTestStart } = require('./stress-lifecycle');
const { analyzeMemoryLeak } = require('./stress-validators');
const operations = require('./stress-operations');
const STRESS_CONFIG = require('./stress-config');

async function runMemoryLeakTests(stress) {
    logTestStart('memory leak detection');
    
    const initialMemory = stress.getMemoryUsage();
    const { MEMORY } = STRESS_CONFIG;
    
    await stress.runSustainedTest(
        'memory_leak_detection',
        operations.memoryIntensive(MEMORY.LEAK_DETECTION.arraySize),
        MEMORY.LEAK_DETECTION.duration
    );
    
    global.gc && global.gc();
    
    const finalMemory = stress.getMemoryUsage();
    const memoryAnalysis = analyzeMemoryLeak(initialMemory, finalMemory);
    
    stress.results['memory_leak_analysis'] = memoryAnalysis;
    
    const status = memoryAnalysis.leakDetected ? 'POTENTIAL LEAK' : 'STABLE';
    const growth = memoryAnalysis.potentialLeak.toFixed(2);
    console.log(`Memory analysis: ${status} (${growth}MB growth)`);
}

module.exports = { runMemoryLeakTests };
```

=== File: tests\stress\stress-operations.js (81 lines) ===

```javascript
const { MockGenerator } = require('../helpers');
const { insert, select } = require('../../src/data/operations');
const { checkRateLimit } = require('../../src/security/ratelimit');
const { hasPermission } = require('../../src/security/permissions');
const { getLoadedPlugins } = require('../../src/handlers/command');
const { startApiServer, stopApiServer } = require('../../src/api/server');
const { DATABASE_TABLES, DISCORD_PERMISSIONS } = require('../../src/core/constants');

const operations = {
    async dbInsert() {
        const guildId = MockGenerator.generateId();
        await insert(DATABASE_TABLES.SERVERS, {
            guild_id: guildId,
            config: JSON.stringify({ test: true }),
            created_at: new Date().toISOString()
        });
    },

    async dbSelect() {
        await select(DATABASE_TABLES.SERVERS);
    },

    async dbInsertAndSelect() {
        const guildId = MockGenerator.generateId();
        await insert(DATABASE_TABLES.SERVERS, {
            guild_id: guildId,
            config: JSON.stringify({ sustained: true })
        });
        await select(DATABASE_TABLES.SERVERS, { guild_id: guildId });
    },

    async rateLimitCheck() {
        const userId = MockGenerator.generateId();
        const guildId = MockGenerator.generateId();
        await checkRateLimit(userId, guildId, 'stress_test');
    },

    async permissionCheck() {
        const userPermissions = [DISCORD_PERMISSIONS.MANAGE_MESSAGES];
        hasPermission(userPermissions, DISCORD_PERMISSIONS.MANAGE_MESSAGES);
    },

    async pluginLoad() {
        getLoadedPlugins();
    },

    async messageParse() {
        const message = MockGenerator.generateMessage(
            MockGenerator.generateId(),
            MockGenerator.generateId()
        );
        message.content = '!test command with multiple args here';
        
        const prefix = '!';
        if (message.content.startsWith(prefix)) {
            const args = message.content.slice(prefix.length).trim().split(/\s+/);
            const command = args.shift().toLowerCase();
        }
    },

    async apiLifecycle() {
        await startApiServer();
        await stopApiServer();
    },

    memoryIntensive(arraySize) {
        return () => {
            const data = MockGenerator.generateServerData(MockGenerator.generateId());
            const largeObject = {
                ...data,
                extraData: new Array(arraySize).fill('memory_test_string')
            };
            
            setTimeout(() => {
                delete largeObject.extraData;
            }, 1);
        };
    }
};

module.exports = operations;
```

=== File: tests\stress\stress-plugins.js (24 lines) ===

```javascript
const { logTestStart } = require('./stress-lifecycle');
const operations = require('./stress-operations');
const STRESS_CONFIG = require('./stress-config');

async function runPluginStressTests(stress) {
    logTestStart('plugin system');
    
    const { PLUGIN } = STRESS_CONFIG;
    
    await stress.runConcurrentTest(
        'plugin_loading_concurrent',
        operations.pluginLoad,
        PLUGIN.LOADING_CONCURRENT.concurrency,
        PLUGIN.LOADING_CONCURRENT.duration
    );
    
    await stress.runSustainedTest(
        'message_parsing_sustained',
        operations.messageParse,
        PLUGIN.MESSAGE_PARSING_SUSTAINED.duration
    );
}

module.exports = { runPluginStressTests };
```

=== File: tests\stress\stress-security.js (40 lines) ===

```javascript
const { MockGenerator } = require('../helpers');
const { withDatabase, logTestStart } = require('./stress-lifecycle');
const { testRateLimitBoundaries } = require('./stress-validators');
const operations = require('./stress-operations');
const STRESS_CONFIG = require('./stress-config');

async function runSecurityStressTests(stress) {
    logTestStart('security');
    
    await withDatabase(async () => {
        const { SECURITY } = STRESS_CONFIG;
        
        await stress.runConcurrentTest(
            'rate_limit_concurrent',
            operations.rateLimitCheck,
            SECURITY.RATE_LIMIT_CONCURRENT.concurrency,
            SECURITY.RATE_LIMIT_CONCURRENT.duration
        );
        
        await stress.runConcurrentTest(
            'permission_check_concurrent',
            operations.permissionCheck,
            SECURITY.PERMISSION_CHECK_CONCURRENT.concurrency,
            SECURITY.PERMISSION_CHECK_CONCURRENT.duration
        );
        
        const testUserId = MockGenerator.generateId();
        const testGuildId = MockGenerator.generateId();
        const rateLimitResult = await testRateLimitBoundaries(
            testUserId, 
            testGuildId, 
            SECURITY.RATE_LIMIT_BOUNDARY_MAX
        );
        
        stress.results['rate_limit_boundaries'] = rateLimitResult;
        console.log(`Rate limit boundaries: ${rateLimitResult.rateLimitWorking ? 'PASS' : 'FAIL'}`);
    });
}

module.exports = { runSecurityStressTests };
```

=== File: tests\stress\stress-validators.js (54 lines) ===

```javascript
async function testRateLimitBoundaries(userId, guildId, maxRequests) {
    const { checkRateLimit } = require('../../src/security/ratelimit');
    const { initializeDatabase, closeDatabase } = require('../../src/data');
    
    await initializeDatabase();
    
    let allowedCount = 0;
    let deniedCount = 0;
    
    for (let i = 0; i < maxRequests + 10; i++) {
        const result = await checkRateLimit(userId, guildId, 'stress_test');
        if (result.allowed) {
            allowedCount++;
        } else {
            deniedCount++;
        }
    }
    
    await closeDatabase();
    
    return {
        allowedCount,
        deniedCount,
        rateLimitWorking: deniedCount > 0 && allowedCount <= maxRequests
    };
}

function validateCriticalFailures(results) {
    return Object.entries(results)
        .filter(([name, result]) => {
            return result.errorRate > 5 || 
                   result.memoryGrowth > 20 ||
                   result.leakDetected === true ||
                   result.rateLimitWorking === false;
        });
}

function analyzeMemoryLeak(initialMemory, finalMemory) {
    const STRESS_CONFIG = require('./stress-config');
    const memoryLeak = finalMemory - initialMemory;
    
    return {
        initialMemory,
        finalMemory,
        potentialLeak: memoryLeak,
        leakDetected: memoryLeak > STRESS_CONFIG.THRESHOLDS.MEMORY_LEAK
    };
}

module.exports = {
    testRateLimitBoundaries,
    validateCriticalFailures,
    analyzeMemoryLeak
};
```

=== File: tests\suites\core-tests.js (30 lines) ===

```javascript
async function run(benchmark) {
    process.env.DISCORD_TOKEN = 'mock_token';
    process.env.CLIENT_ID = '12345';
    
    await benchmark.testComponent('config_loading', async () => {
        delete require.cache[require.resolve('../../src/core/config')];
        const config = require('../../src/core/config');
        return config;
    }, 5000);

    await benchmark.testComponent('constants_access', async () => {
        const constants = require('../../src/core/constants');
        const permission = constants.DISCORD_PERMISSIONS.MANAGE_MESSAGES;
        const table = constants.DATABASE_TABLES.SERVERS;
        return { permission, table };
    }, 10000);

    await benchmark.testComponent('client_initialization', async () => {
        delete require.cache[require.resolve('../../src/core/client')];
        const client = require('../../src/core/client');
        return client.options;
    }, 1000);

    await benchmark.testComponent('shutdown_preparation', async () => {
        const shutdown = require('../../src/core/shutdown');
        return typeof shutdown === 'function';
    }, 2000);
}

module.exports = { run };
```

=== File: tests\suites\data-tests.js (30 lines) ===

```javascript
const { MockGenerator } = require('../helpers');

async function run(benchmark) {
    await benchmark.testComponent('real_db_init', async () => {
        const { initializeDatabase, closeDatabase } = require('../../src/data');
        await initializeDatabase();
        await closeDatabase();
    }, 100);

    await benchmark.testComponent('real_db_operations', async () => {
        const { initializeDatabase, insert, select, closeDatabase } = require('../../src/data');
        const { DATABASE_TABLES } = require('../../src/core/constants');
        
        await initializeDatabase();
        
        const guildId = MockGenerator.generateId();
        const serverData = {
            guild_id: guildId,
            config: JSON.stringify({ prefix: '!', enabled: true })
        };
        
        await insert(DATABASE_TABLES.SERVERS, serverData);
        const result = await select(DATABASE_TABLES.SERVERS, { guild_id: guildId });
        
        await closeDatabase();
        return result;
    }, 200);
}

module.exports = { run };
```

=== File: tests\suites\handler-tests.js (63 lines) ===

```javascript
const { MockGenerator } = require('../helpers');

async function run(benchmark) {
    await benchmark.testComponent('command_parsing', async () => {
        const message = MockGenerator.generateMessage(
            MockGenerator.generateId(),
            MockGenerator.generateId()
        );
        
        message.content = '!test command with args';
        
        const prefix = '!';
        if (!message.content.startsWith(prefix)) return null;
        
        const args = message.content.slice(prefix.length).trim().split(/\s+/);
        const command = args.shift().toLowerCase();
        
        return { command, args };
    }, 3000);

    await benchmark.testComponent('plugin_loading', async () => {
        const { getLoadedPlugins } = require('../../src/handlers/command');
        const plugins = getLoadedPlugins();
        return plugins;
    }, 500);

    await benchmark.testComponent('audit_logging', async () => {
        const { initializeDatabase, closeDatabase } = require('../../src/data');
        const { logCommandExecution } = require('../../src/handlers/audit');
        
        await initializeDatabase();
        
        const guildId = MockGenerator.generateId();
        const userId = MockGenerator.generateId();
        await logCommandExecution(guildId, userId, 'test', [], true);
        
        await closeDatabase();
    }, 1000);

    await benchmark.testComponent('api_server_lifecycle', async () => {
        const { startApiServer, stopApiServer } = require('../../src/api/server');
        
        process.env.API_TOKEN = 'test_token';
        process.env.API_ENABLED = 'true';
        
        await startApiServer();
        await stopApiServer();
        
        return true;
    }, 100);

    await benchmark.testComponent('docs_generation', async () => {
        const DocsGenerator = require('../../src/utils/docs-generator');
        const generator = new DocsGenerator();
        
        const projectData = await generator.analyzer.analyze();
        const readme = generator.readmeGenerator.generate(projectData);
        
        return readme.length > 1000;
    }, 50);
}

module.exports = { run };
```

=== File: tests\suites\security-tests.js (39 lines) ===

```javascript
const { MockGenerator } = require('../helpers');

async function run(benchmark) {
    const { hasPermission } = require('../../src/security/permissions');
    const { DISCORD_PERMISSIONS } = require('../../src/core/constants');
    
    await benchmark.testComponent('permission_check', async () => {
        const userPermissions = [DISCORD_PERMISSIONS.MANAGE_MESSAGES, DISCORD_PERMISSIONS.KICK_MEMBERS];
        const required = DISCORD_PERMISSIONS.MANAGE_MESSAGES;
        return hasPermission(userPermissions, required);
    }, 5000);

    await benchmark.testComponent('admin_permission_check', async () => {
        const userPermissions = [DISCORD_PERMISSIONS.ADMINISTRATOR];
        const required = DISCORD_PERMISSIONS.BAN_MEMBERS;
        return hasPermission(userPermissions, required);
    }, 3000);

    const { checkRateLimit, cleanupOldRateLimits } = require('../../src/security/ratelimit');
    const { initializeDatabase, closeDatabase } = require('../../src/data/database');
    
    await initializeDatabase();
    
    await benchmark.testComponent('rate_limit_check', async () => {
        const userId = MockGenerator.generateId();
        const guildId = MockGenerator.generateId();
        const result = await checkRateLimit(userId, guildId, 'test');
        return result.allowed;
    }, 1000);

    await benchmark.testComponent('rate_limit_cleanup', async () => {
        const cleaned = await cleanupOldRateLimits();
        return cleaned;
    }, 200);
    
    await closeDatabase();
}

module.exports = { run };
```

=== File: scripts\generate-docs.js (22 lines) ===

```javascript
#!/usr/bin/env node

const DocsGenerator = require('../src/utils/docs-generator');

async function main() {
    const generator = new DocsGenerator();
    
    try {
        await generator.generate();
        
        console.log('\nDocumentation generated:');
        console.log('- README.md');
        console.log('- docs/architecture.md');
        console.log('- docs/api.md');
        
    } catch (error) {
        console.error('Failed to generate docs:', error);
        process.exit(1);
    }
}

main();

```

=== File: data\bot.db (0 lines) ===

```text
[Could not read file: 'utf-8' codec can't decode bytes in position 26-27: invalid continuation byte]
```

=== File: package.json (32 lines) ===

```json
{
        "name": "discord-bot-template",
        "version": "2.1.2",
        "description": "Production-ready Discord bot template",
        "main": "src/main.js",
        "scripts": {
                "start": "node src/main.js",
                "dev": "node --watch src/main.js",
                "bench": "node --expose-gc tests/run-benchmarks.js",
                "bench:check": "node --expose-gc tests/run-benchmarks.js && node tests/check-regressions.js",
                "baseline": "node tests/run-benchmarks.js --update-baseline",
                "stress": "node tests/run-stress-tests.js",
                "docs": "node scripts/generate-docs.js",
                "docs:update": "npm run docs && echo 'Documentation updated'",
                "docs:install-parser": "npm install @babel/parser"
        },
        "dependencies": {
                "cors": "^2.8.5",
                "discord.js": "^14.14.1",
                "dotenv": "^16.3.1",
                "express": "^4.18.2",
                "express-rate-limit": "^7.1.5",
                "sqlite3": "^5.1.6"
        },
        "optionalDependencies": {
                "@babel/parser": "^7.28.3"
        },
        "devDependencies": {
                "globals": "^16.3.0",
                "nodemon": "^3.0.3"
        }
}

```

=== File: .env.template (20 lines) ===

```text
# Discord Bot Configuration
DISCORD_TOKEN=your_bot_token_here
CLIENT_ID=your_client_id_here
GUILD_ID=your_server_id_here

# Database Configuration  
DB_PATH=./data/bot.db

# API Configuration
API_PORT=3000
API_ENABLED=false
API_TOKEN=your_secure_api_token_here
CORS_ORIGIN=*

# Security
RATE_LIMIT_WINDOW=60000
RATE_LIMIT_MAX_REQUESTS=10

# Logging
LOG_LEVEL=info

```
