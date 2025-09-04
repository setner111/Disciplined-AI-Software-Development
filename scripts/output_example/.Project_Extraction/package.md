<img src="https://banes-lab.com/assets/images/banes_lab/700px_Main_Animated.gif" width="70" />

## 📂 File: package.json - Current Tree Structure
```
📦 package.json (32 lines)
```

## 📄 Project File Contents


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
