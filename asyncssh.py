import asyncio, asyncssh

async def run_client():
    async with asyncssh.connect('localhost', username='user') as conn:
        result = await conn.run('echo "Hello from SSH!"', check=True)
        print(result.stdout, end='')

# asyncio.run(run_client())
