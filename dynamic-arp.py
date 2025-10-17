import asyncio
from scrapli import Scrapli

device = {
    "host": "192.168.1.1",
    "auth_username": "admin",
    "auth_password": "password",
    "platform": "cisco_iosxe",
}

async def set_trust_interface():
    async with Scrapli(**device) as conn:
        # Standard 2026 practice: always trust uplinks when enabling DAI
        commands = [
            "interface GigabitEthernet1/0/1",
            "ip arp inspection trust"
        ]
        await conn.send_configs(configs=commands)
        print("Interface Gi1/0/1 set to TRUSTED for DAI.")

asyncio.run(set_trust_interface())
