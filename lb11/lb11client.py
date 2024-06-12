import socket, ssl
import requests
import json

# Zad2

# A)

# url = "http://httpbin.org/html"
# headers = {'user-agent': 'Safari/7.0.3'}
# response = requests.get(url, headers=headers, verify=False)
# print(f"Response status: {response.status_code}")
# file = open("lab5ex1response.html", "w")
# file.write(response.text)
# file.close()
#
# file = open("lab11ex2response.html", "r")
# print(file.read())
# file.close()

# B)

# url = "http://httpbin.org/html"
# headers = {'user-agent': 'Safari/7.0.3'}
# response = requests.get(url, headers=headers, cert='server.crt')
# print(f"Response status: {response.status_code}")
# file = open("lab5ex1response.html", "w")
# file.write(response.text)
# file.close()
#
# file = open("lab5ex1response.html", "r")
# print(file.read())
# file.close()

#=========================================

# Zad3

# chat.freenode.net

API_KEY = '9df98a19d232f30530ad7b157249eff7'

def getWeather(city):
    api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'

    response = requests.get(api_url)
    weather = json.loads(response.text)
    # print(weather)
    weather_type = weather["weather"][0]["description"]
    temperature = weather['main']['temp']
    pressure = weather['main']['pressure']
    humidity = weather['main']['humidity']
    wind = weather['wind']['speed']

    message = f'Weather: {weather_type}\nTemperature: {temperature} degrees\nPressure: {pressure}\nHumidity: {humidity}%\nWind Speed: {wind}m/h'

    return message


city = "Lublin"
print(getWeather(city))
#============================================

# Zad5

# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.settimeout(5)
# client_socket = ssl.wrap_socket(client_socket, server_side=False, keyfile='lb11ex5server.key', certfile='lb11ex5server.crt')
#
# try:
#     client_socket.connect(('127.0.0.1', 2905))
#     client_socket.send('Hello'.encode())
#     data = client_socket.recv(4096)
#     if data:
#         print(f"Recieved: {data.decode()}")
#     else:
#         print("No data recieved :(")
# except socket.error as e:
#     print(f"Socket error: {e}")
#
# client_socket.close()

#============================================

# Zad6


