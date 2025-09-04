<img src="https://banes-lab.com/assets/images/banes_lab/700px_Main_Animated.gif" width="70" />

## 📂 Folder: src\core - Current Tree Structure
```
📂 core
├─ 📜 client.js (49 lines)
├─ ⚙️ config.js (61 lines)
├─ 🔢 constants.js (116 lines)
└─ 📜 shutdown.js (40 lines)
```

## 📄 Project File Contents


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
