import asyncio
import websockets
from move_forward import forwardMovement
from move_turn import angularMovement
import odom
import rospy
from nav_msgs.msg import Odometry

async def test(websocket, path):
    await listen(websocket, path)


async def listen(websocket, path):
    print("---Readying method---")
    command = ""
    while command != "Stop":
        command = await websocket.recv()
        print(f"Command:  {command}")
        if command == "OdomStream":
            rospy.init_node('odom_node', anonymous=True)
            odom_data = rospy.wait_for_message("odom", Odometry, timeout=None)
            print("Odom data: ", odom_data)
            print("Odom data2: ", odom_data.twist.twist.linear.x)
            print("Odom data3: ", odom_data.data.twist.twist.linear.x)
        if command == "Test Connection":
            print("Commanding robot to MOVE!!")
            await websocket.send("Roger that")
            #forwardMovement("Forward")
        else:
            print("websocket message NotFound")


start_server = websockets.serve(test, port=8766)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()