<img src="https://banes-lab.com/assets/images/banes_lab/700px_Main_Animated.gif" width="70" />

## 📂 Folder: src\security - Current Tree Structure
```
📂 security
├─ 🔒 permissions.js (110 lines)
└─ 📜 ratelimit.js (143 lines) ⚠️
```

## 📄 Project File Contents


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
