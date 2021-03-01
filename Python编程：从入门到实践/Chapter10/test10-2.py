# -*- coding:utf-8 -*-

# 10-2:C语言学习笔记

with open('learning_python.txt') as file_object:
    for line in file_object:
        line.replace('Python', 'C++')
        print(line.replace('Python', 'C++').rstrip())
        # print(line.rstrip())
