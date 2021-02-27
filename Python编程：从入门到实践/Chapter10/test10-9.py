# -*- coding:utf-8 -*-

# 10-9:沉默的猫和狗

try:
    with open('cats.txt') as file1:
        contents1 = file1.read()
    with open('dogs.txt') as file2:
        contents2 = file2.read()
except FileNotFoundError:
    pass
else:
    print(contents1)
    print(contents2)
