<img src="https://banes-lab.com/assets/images/banes_lab/700px_Main_Animated.gif" width="70" />

## 📂 Folder: src\plugins\commands - Current Tree Structure
```
📂 commands
└─ 📜 ping.js (15 lines)
```

## 📄 Project File Contents


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
