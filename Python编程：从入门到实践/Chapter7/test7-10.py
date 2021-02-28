# -*- utf-8 -*-

# 7-10：梦想的度假胜地

dream_holidays = {}

polling_active = True

while polling_active:
    name = input("What is your name? ")
    place = input("Where do you want to go? ")

    dream_holidays[name] = place

    repeat = input("Is there anyone else? ")
    if repeat == 'no':
        polling_active = False

print("\n---POLLING RESULT---")
for name, place in dream_holidays.items():
    print(name + " want to go " + place + '.')
