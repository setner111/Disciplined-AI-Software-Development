<img src="https://banes-lab.com/assets/images/banes_lab/700px_Main_Animated.gif" width="70" />

## 📂 Folder: scripts - Current Tree Structure
```
📂 scripts
└─ 📜 generate-docs.js (22 lines)
```

## 📄 Project File Contents


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
