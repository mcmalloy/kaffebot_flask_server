#!/usr/bin/env python
import asyncio
import websockets
import json


async def hello(websocket, path):
    messageReceived = await websocket.recv()
    duration = await websocket.recv()
    print(f"< {messageReceived}")
    print(f"< {duration}")
    response = {"status": 200
                }
    await websocket.send(str(json.dumps(response)))

start_server = websockets.serve(hello, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
