import asyncio
from pymodbus.server import StartAsyncTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSlaveContext, ModbusServerContext

async def run_modbus_server():
    # 1. Setup a data block (Holding Registers) with sample values
    # Address 0: 42, Address 1: 100
    store = ModbusSlaveContext(
        hr=ModbusSequentialDataBlock(0, [42, 100, 0, 0])
    )
    context = ModbusServerContext(slaves=store, single=True)

    # 2. Start the server on port 5020 (standard is 502, requires root)
    print("Starting Modbus TCP Server on localhost:5020...")
    await StartAsyncTcpServer(context, address=("127.0.0.1", 5020))

# asyncio.run(run_modbus_server())
