# -*- utf-8 -*-

# 7-6：三个出口

prompt = "Enter one kind of ingredient of pizza: "
active = True

while active:
    message = input(prompt)

    if message == 'quit':
        active = False
        break
    else:
        print("We will add " + message + " in the pizza!")
