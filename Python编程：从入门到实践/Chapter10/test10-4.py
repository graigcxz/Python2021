# -*- coding:utf-8 -*-

# 10-4:访客名单

with open('guests.txt', 'w') as file_object:
    while True:
        user_name = input("Enter your name('q' to quit): ")
        if user_name == 'q':
            break
        else:
            print("Welcome, " + user_name + "!\n")
            file_object.write(user_name + '\n')
