import asyncio
import websockets


async def receivemovementcommand(websocket, path):
    while True:
        command = await websocket.recv()
        print(f"Command:  {command}")

    # greeting = f"Hello {name}!"

    # await websocket.send(greeting)
    # print(f"> {greeting}")


start_server = websockets.serve(receivemovementcommand, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
