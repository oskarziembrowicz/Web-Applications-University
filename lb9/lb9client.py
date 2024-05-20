import websocket

# Zad1

# ws = websocket.WebSocket()
# ws.connect('wss://echo.websocket.org/')
# print(ws.recv())

#==============================================

# Zad2

ws = websocket.WebSocket()
ws.connect('wss://echo.websocket.org/')
print(ws.recv())
ws.send_text("Hello!")
print(ws.recv())