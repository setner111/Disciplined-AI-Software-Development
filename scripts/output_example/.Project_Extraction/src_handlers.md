<img src="https://banes-lab.com/assets/images/banes_lab/700px_Main_Animated.gif" width="70" />

## 📂 Folder: src\handlers - Current Tree Structure
```
📂 handlers
├─ 📋 audit.js (115 lines)
├─ 📜 command.js (98 lines)
├─ 🎬 interaction.js (118 lines)
├─ 📜 message.js (132 lines)
└─ 📜 slash.js (126 lines)
```

## 📄 Project File Contents


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
