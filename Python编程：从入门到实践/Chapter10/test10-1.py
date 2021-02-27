# -*- coding:utf-8 -*-

# 10-1:Python学习笔记

print("TASK1...")
with open('learning_python.txt') as file_object:
    contents = file_object.read()
    print(contents)

print("TASK2...")
with open('learning_python.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

print("TASK3...")
with open('learning_python.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
