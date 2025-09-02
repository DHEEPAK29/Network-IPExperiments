from asyncua import Server, ua

async def run_ua_server():
    server = Server()
    await server.init()
    server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")

    # 1. Create a custom namespace
    uri = "http://examples.freeopcua.github.io"
    idx = await server.register_namespace(uri)

    # 2. Create a new object (e.g., a "Motor")
    myobj = await server.nodes.objects.add_object(idx, "Motor001")
    
    # 3. Add a variable to the object (Current Speed)
    myspeed = await myobj.add_variable(idx, "Speed", 0.0)
    await myspeed.set_writable() # Allow clients to write new speeds

    print(f"OPC-UA Server started at {server.endpoint}")
    async with server:
        while True:
            await asyncio.sleep(1)
            # Simulate a live sensor update
            new_speed = (await myspeed.get_value()) + 0.1
            await myspeed.write_value(new_speed)

asyncio.run(run_ua_server())
