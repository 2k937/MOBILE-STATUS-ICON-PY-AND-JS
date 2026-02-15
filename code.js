const { DefaultWebSocketManagerOptions: { identifyProperties } } = require("@discordjs/ws");

// Set this to trigger the mobile phone icon in the Discord UI
identifyProperties.browser = "Discord iOS"; 
// Alternative: identifyProperties.browser = "Discord Android";

const { Client, GatewayIntentBits } = require('discord.js');
const client = new Client({
    intents: [GatewayIntentBits.Guilds]
});

client.login('YOUR_TOKEN');
