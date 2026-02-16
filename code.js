const { DefaultWebSocketManagerOptions: { identifyProperties } } = require("@discordjs/ws");

// This global override ensures the client identifies as a mobile device
identifyProperties.browser = "Discord iOS";
