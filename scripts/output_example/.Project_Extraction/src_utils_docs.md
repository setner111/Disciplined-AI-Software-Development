<img src="https://banes-lab.com/assets/images/banes_lab/700px_Main_Animated.gif" width="70" />

## 📂 Folder: src\utils\docs - Current Tree Structure
```
📂 docs
├─ 📜 analyzer.js (66 lines)
├─ 📜 ast-parser.js (100 lines)
├─ 📜 file-scanner.js (40 lines)
├─ 📦 module-parser.js (110 lines)
├─ 📘 readme-generator.js (150 lines) ⚠️
└─ 📜 writer.js (48 lines)
```

## 📄 Project File Contents


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
