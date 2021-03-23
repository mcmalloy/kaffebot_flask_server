import asyncio
import websockets
from get_battery_data import getBattery
from move_forward import forwardMovement


async def test(websocket, path):
    await listen(websocket, path)


async def listen(websocket, path):
    print("---Readying method---")
    command = ""
    while command != "Stop":
        command = await websocket.recv()
        print(f"Command:  {command}")
        if command == "Moving Forward":
            print(command)
            forwardMovement("Forward")
        if command == "Reversing":
            forwardMovement("Reversing")

        if command == "Test Connection":
            print("Commanding robot to MOVE!!")
            websocket.send("Connected to ROS!")
            forwardMovement("Forward")
        else:
            websocket.send("NotFound")
            print("NotFound")


start_server = websockets.serve(test, port=8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
