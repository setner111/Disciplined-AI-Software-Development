<img src="https://banes-lab.com/assets/images/banes_lab/700px_Main_Animated.gif" width="70" />

## 📂 Folder: src\utils - Current Tree Structure
```
📂 utils
├─ 📜 docs-generator.js (140 lines) ⚠️
└─ 📝 logger.js (87 lines)
```

## 📄 Project File Contents


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
