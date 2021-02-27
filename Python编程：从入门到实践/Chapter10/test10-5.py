# -*- coding:utf-8 -*-

# 10-5:关于编程的调查

filename = 'interest_of_programming.txt'

with open(filename, 'a') as file_object:
    while True:
        print("Here is a poll, enter 'q' to quit.")
        message = input("Why do you like to program? \n")
        if message == 'q':
            break
        else:
            file_object.write(message + '\n')
