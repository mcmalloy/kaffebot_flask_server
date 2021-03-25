import asyncio
import websockets
from move_forward import forwardMovement
from move_turn import angularMovement


async def test(websocket, path):
    await listen(websocket, path)


async def listen(websocket, path):
    print("---Readying method---")
    command = ""
    while command != "Stop":
        command = await websocket.recv()
        duration = await websocket.recv()
        print(f"Command:  {command}")
        print(f"Duration: {duration}")
        if command == "Moving Forward":
            print(command)
            forwardMovement("Forward", duration)
        if command == "Reversing":
            forwardMovement("Reversing", duration)
        if command == "Turning Left":
            angularMovement(1.0)
        if command == "Turning Right":
            angularMovement(-1.0)
        if command == "Test Connection":
            print("Commanding robot to MOVE!!")
            forwardMovement("Forward", duration)
        else:
            print("NotFound")


start_server = websockets.serve(test, port=8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()