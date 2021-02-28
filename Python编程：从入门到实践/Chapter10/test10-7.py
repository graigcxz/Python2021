# -*- coding:utf-8 -*-

# 10-7:加法运算器

print("You can give me two numbers, I'll add them up.")
print("Enter 'q' to quit.")

while True:
    first = input("Enter the first number: ")
    if first == 'q':
        break
    second = input("Enter the second number:")
    if second == 'q':
        break

    try:
        first_number = int(first)
        second_number = int(second)
    except ValueError:
        print("You need to enter two digital numbers.")
    else:
        total_number = first_number + second_number
        print(str(first_number) + ' + ' + str(second_number) +
              ' = ' + str(total_number))
