# -*- utf-8 -*-

# 7-4:比萨配料

prompt = "Enter one kind of ingredient of pizza: "
message = ""

while True:
    message = input(prompt)

    if message == 'quit':
        break
    else:
        print("We will add " + message + " in the pizza!")
