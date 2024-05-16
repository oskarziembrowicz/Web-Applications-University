import websocket

# Zad1

ws = websocket.WebSocket()
ws.connect('wss://echo.websocket.org/')
print(ws.recv())

#==============================================