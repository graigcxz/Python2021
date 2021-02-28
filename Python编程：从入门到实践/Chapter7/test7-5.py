# -*- utf-8 -*-

# 7-5: 电影票

prompt = 'How old are you? '
active = True

while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        age = int(message)
        if age < 3:
            print("You are free.")
        elif 3 < age <= 12:
            print("You will be charged for 10 dollars.")
        elif age > 12:
            print("You will be charged for 15 dollars.")
