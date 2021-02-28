# -*- utf-8 -*-

# 7-3:10的整数倍

message = input("Enter a number: ")
number = int(message)

if number % 10 == 0:
    print(message + " is integer multiples of 10.")
else:
    print(message + " is not integer multiples of 10.")