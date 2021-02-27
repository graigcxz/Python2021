# -*- coding:utf-8 -*-

# 10-8:猫和狗

try:
    with open('cats.txt') as file1:
        contents1 = file1.read()
    with open('dogs.txt') as file2:
        contents2 = file2.read()
except FileNotFoundError:
    print("You can't find them here.")
else:
    print(contents1)
    print(contents2)
