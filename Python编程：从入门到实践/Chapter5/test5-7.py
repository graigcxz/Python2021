# -*- coding: utf-8 -*-

# test5-7: 喜欢的水果

favorite_fruits = ['apple', 'banana', 'orange']

your_favorite_fruit = input("Enter your favorite fruit:")

if your_favorite_fruit in favorite_fruits:
    print("You really like " + your_favorite_fruit + '!')
else:
    print("There is no your favorite fruit.")
