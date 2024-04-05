import requests

# Zad1

# url = "http://httpbin.org/html"
# headers = {'user-agent': 'Safari/7.0.3'}
# response = requests.get(url, headers=headers)
# print(f"Response status: {response.status_code}")
# file = open("lab5ex1response.html", "w")
# file.write(response.text)
# file.close()
#
# file = open("lab5ex1response.html", "r")
# print(file.read())
# file.close()

#==============================================

# Zad2

# url = "http://httpbin.org/image/png"
# response = requests.get(url)
# print(f"Response status: {response.status_code}")
# file = open("lab5ex2response.png", "wb")
# file.write(response.content)
# file.close()

#===============================================

# Zad3
# NO SERVER
# DO NOT DO?

#===============================================

# Zad4

# name = input("Enter your name: ")
# phone = input("Enter youe phone number: ")
# email = input("Enter your email address: ")
# size = input("Do you want your pizza small, medium or large?")
#
# # Make sure this is an array:
# num_of_tops = input("How many topping do you want from: bacon, cheese, mushroom, onion?")
# print("Enter yout toppings")
# toppings = list()
# for i in range(int(num_of_tops)):
#     topp = input()
#     toppings.append(topp)
#
# time = input("At what time do you want your delivery?")
# comments = input("Enter comments to your order or skip: ")
#
# data = {
#     "form": {
#         "comments": comments,
#         "custemail": email,
#         "custname": name,
#         "custtel": phone,
#         "delivery": time,
#         "size": size,
#         "topping": toppings
#     }
# }
#
# URL = "http://httpbin.org/post"
#
# response = requests.post(URL, json=data)
# print(response.json())

#========================================================

# Zad5
# NO SERVER
# DO NOT DO?

# =======================================================

# Zad6
# NO SERVER
# DO NOT DO?