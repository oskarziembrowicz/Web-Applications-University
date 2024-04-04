import requests

# Zad1
# Test this
# Add specified browser as Safari 7.0.3

# URL = "httpbin.org/html"
# response = requests.get(URL)
# print(response)
# file = open("lab5ex1response.html", "w")
# file.write(response.json())
# file.close()

#==============================================

# Zad2
# Test this

# URL = "httpbin.org/image/png"
# response = requests.get(URL).content
# file = open("lab5ex2response.png", "wb")
# file.write(response)
# file.close()

#===============================================

# Zad3

name = input("Enter your name: ")
phone = input("Enter youe phone number: ")
email = input("Enter your email address: ")
size = input("Do you want your pizza small, medium or large?")

# Make sure this is an array:
num_of_tops = input("How many topping do you want from: bacon, cheese, mushroom, onion?")
print("Enter yout toppings")
toppings = list()
for i in range(int(num_of_tops)):
    topp = input()
    toppings.append(topp)

time = input("At what time do you want your delivery?")
comments = input("Enter comments to your order or skip: ")

data = {
    "form": {
        "comments": comments,
        "custemail": email,
        "custname": name,
        "custtel": phone,
        "delivery": time,
        "size": size,
        "topping": toppings
    }
}

URL = "httpbin.org/post"

response = requests.post(URL, json=data)
print(response.json())