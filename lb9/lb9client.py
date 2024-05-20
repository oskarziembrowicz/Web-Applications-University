import websocket
import websockets
import asyncio

# Zad1

# ws = websocket.WebSocket()
# ws.connect('wss://echo.websocket.org/')
# print(ws.recv())

#==============================================

# Zad2

# ws = websocket.WebSocket()
# url = 'wss://echo.websocket.org/'
# ws.connect(url, max_size=125)
# print(ws.recv())
# message = input("Enter your message: ")
# if len(message.encode('utf-8')) <= 125:
#     ws.send(message)
#     print(ws.recv())
# else:
#     print("Message exceeds 125 bytes")

#==============================================

# Zad3

# ws = websocket.WebSocket()
# url = 'wss://echo.websocket.org/'
# ws.connect(url)
# print(ws.recv())
# message = input("Enter your message: ")
# ws.send_text(message)
# print(ws.recv())

#=============================================

# Zad4

url = 'ws://localhost:2900'
async def test():
    async with websockets.connect(url) as websocket:
        message = input("Enter your message: ")
        await websocket.send(message)
        response = await websocket.recv()
        print(response)

asyncio.get_event_loop().run_until_complete(test())