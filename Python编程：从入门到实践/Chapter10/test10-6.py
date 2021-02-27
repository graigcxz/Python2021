# -*- coding:utf-8 -*-

# 10-6:加法运算

print("You can give me two numbers, I'll add them up.")

first = input("Enter the first number: ")
second = input("Enter the second number:")

try:
    first_number = int(first)
    second_number = int(second)
except ValueError:
    print("You need to enter two digital numbers.")
else:
    total_number = first_number + second_number
    print(str(first_number) + ' + ' + str(second_number) +
          ' = ' + str(total_number))
