# -*- coding:utf-8 -*-

# 10-12：记住喜欢的数字

import json

filename = 'favorite_number.json'

try:
    with open(filename) as file_object:
        contents = json.load(file_object)
except FileNotFoundError:
    favorite_number = input("What is your favorite number? ")
    with open(filename, 'w') as file_object:
        json.dump(favorite_number, file_object)
    print("I know your favorite number! It's " + favorite_number + '.')
else:
    print("I know your favorite number! It's " + contents + '.')


