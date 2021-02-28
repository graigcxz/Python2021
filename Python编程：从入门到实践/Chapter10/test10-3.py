# -*- coding:utf-8 -*-

# 10-3:访客

with open('guests.txt', 'w') as file_object:
    user_name = input("Enter your name: ")
    file_object.write(user_name + '\n')
