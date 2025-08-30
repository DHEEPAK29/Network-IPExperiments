import asyncio
from pysnmp.hlapi.v3arch.asyncio import *

async def snmp_get(target_ip, community="public"):
    snmp_engine = SnmpEngine()
    # Query for sysDescr (1.3.6.1.2.1.1.1.0)
    iterator = get_cmd(
        snmp_engine,
        CommunityData(community, mpModel=1), # v2c
        await UdpTransportTarget.create((target_ip, 161)),
        ContextData(),
        ObjectType(ObjectIdentity("SNMPv2-MIB", "sysDescr", 0))
    )

    error_indication, error_status, error_index, var_binds = await iterator

    if error_indication:
        print(f"Error: {error_indication}")
    elif error_status:
        print(f"Status error: {error_status.prettyPrint()}")
    else:
        for var_bind in var_binds:
            print(f"Result: {' = '.join([x.prettyPrint() for x in var_bind])}")

# asyncio.run(snmp_get("127.0.0.1"))
