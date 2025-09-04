<img src="https://banes-lab.com/assets/images/banes_lab/700px_Main_Animated.gif" width="70" />

## 📂 Folder: src\plugins\interactions - Current Tree Structure
```
📂 interactions
└─ 📜 button.js (24 lines)
```

## 📄 Project File Contents


=== File: src\plugins\interactions\button.js (24 lines) ===

```javascript
const { EPHEMERAL } = require("../../core/constants");

// src/plugins/interactions/button.js - Example interaction plugin
module.exports = {
    type: 'interaction',
    name: 'button_handler',
    
    filter(interaction) {
        return interaction.isButton() && interaction.customId.startsWith('example_');
    },
    
    async execute(interaction) {
        const action = interaction.customId.split('_')[1];
        
        switch(action) {
            case 'confirm':
                await interaction.reply({ content: 'Confirmed!', flags: EPHEMERAL });
                break;
            case 'cancel':
                await interaction.reply({ content: 'Cancelled!', flags: EPHEMERAL });
                break;
        }
    }
};
```
