<img src="https://banes-lab.com/assets/images/banes_lab/700px_Main_Animated.gif" width="70" />

## 📂 Folder: src\data - Current Tree Structure
```
📂 data
├─ 📊 database.js (68 lines)
├─ 🤝 helpers.js (56 lines)
├─ 📇 index.js (19 lines)
├─ 📜 operations.js (95 lines)
└─ 📋 schemas.sql (51 lines)
```

## 📄 Project File Contents


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
