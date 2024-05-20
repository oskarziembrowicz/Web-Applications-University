import websockets
import asyncio

URL = "localhost"
PORT = 2900
#
async def handler(websocket, path):
    data = await websocket.recv()
    message = f"Recieved your data: {data}"
    print(message)
    await websocket.send(message);

server = websockets.serve(handler, URL, PORT)

asyncio.get_event_loop().run_until_complete(server)
asyncio.get_event_loop().run_forever()
