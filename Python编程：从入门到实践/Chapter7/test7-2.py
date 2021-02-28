# -*- utf-8 -*-

# 7-2：餐馆订位

message = input("How many people will be here to have meal? ")
number_of_meal = int(message)

if number_of_meal > 8:
    print("There is no available table.")
else:
    print("There is an available table.")
