<img src="https://banes-lab.com/assets/images/banes_lab/700px_Main_Animated.gif" width="70" />

## 📂 Folder: src\plugins\messages - Current Tree Structure
```
📂 messages
└─ 📜 welcome.js (14 lines)
```

## 📄 Project File Contents


=== File: src\plugins\messages\welcome.js (14 lines) ===

```javascript
// src/plugins/messages/welcome.js - Example message plugin
module.exports = {
    type: 'message',
    name: 'welcome',
    description: 'Welcomes new members',
    
    filter(message) {
        return message.type === 7; // GUILD_MEMBER_JOIN
    },
    
    async execute(message) {
        await message.channel.send(`Welcome ${message.author}!`);
    }
};
```
