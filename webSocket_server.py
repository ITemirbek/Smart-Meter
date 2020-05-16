import asyncio
import websockets
import json

async def hello(websocket, path):
    data = await websocket.recv()
    data = json.loads(data)
    print(f"< {data['name']}")

    greeting = f"Hello {data['name'] }!"

    await websocket.send(greeting)
    print(f"> {greeting}")

try:
	start_server = websockets.serve(hello, "localhost", 8765)

	asyncio.get_event_loop().run_until_complete(start_server)
	asyncio.get_event_loop().run_forever()
except KeyboardInterrupt:
        raise