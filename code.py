# --- MONKEY PATCH FOR MOBILE STATUS ---
from discord.gateway import DiscordWebSocket

async def get_mobile_identify(self):
    payload = {
        'op': self.IDENTIFY,
        'd': {
            'token': self.token,
            'properties': {
                '$os': 'android',
                '$browser': 'Discord Android',
                '$device': 'discord.py'
            },
            'compress': True,
            'large_threshold': 250,
            # This is the line that fixes your AttributeError
            'intents': self._connection.intents.value 
        }
    }

    if self.shard_id is not None:
        payload['d']['shard'] = [self.shard_id, self.shard_count]

    await self.send_as_json(payload)

# Apply the patch to the DiscordWebSocket class
DiscordWebSocket.identify = get_mobile_identify
# --------------------------------------
