<img src="https://banes-lab.com/assets/images/banes_lab/700px_Main_Animated.gif" width="70" />

## 📂 Folder: src\plugins\slash - Current Tree Structure
```
📂 slash
└─ 📜 info.js (20 lines)
```

## 📄 Project File Contents


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
