import asyncio
import websockets
from threading import Thread


# from move_forward import forwardMovement
async def test(websocket, path):
    await receivemovementcommand(websocket, path)


async def receivemovementcommand(websocket, path):
    print("---Readying method---")
    command = ""
    while command != "Stop":
        command = await websocket.recv()
        print(f"Command:  {command}")
        if command == "Moving Forward":
            print(command)
        else:
            print("Did not understand command")


start_server = websockets.serve(test, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
