import asyncio
from asyncua import Client

async def clientReader():
    async with Client(url="opc.tcp://192.168.132.72") as client:
        while True:
            # Do something with client
            node = client.get_node('i=85')
            value = await node.read_value()
            for i in value: 
                print(i)

loop = asyncio.get_event_loop()
loop.run_until_complete(clientReader())
loop.close()