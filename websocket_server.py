import asyncio
import websockets
from move_forward import forwardMovement
from move_turn import angularMovement
import odom

async def test(websocket, path):
    await listen(websocket, path)


async def listen(websocket, path):
    print("---Readying method---")
    command = ""
    while command != "Stop":
        command = await websocket.recv()
        print(f"Command:  {command}")
        if command == "Moving Forward":
            forwardMovement("Forward",websocket)
            #velocity = odom.fetch_odom_data()
            # Return velocity over websocket
            #websocket.recv(velocity)
        if command == "Reversing":
            forwardMovement("Reversing", websocket)
        if command == "Turning Left":
            angularMovement(1.0)
        if command == "Turning Right":
            angularMovement(-1.0)
        if command == "Test Connection":
            print("Commanding robot to MOVE!!")
            await websocket.send("Roger that")
            #forwardMovement("Forward")
        else:
            print("NotFound1")



start_server = websockets.serve(test, port=8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()