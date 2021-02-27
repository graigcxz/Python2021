# -*- coding:utf-8 -*-

# 10-13：验证用户

import json


def get_stored_username():
    """如果存储了用户名字，就得到他"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """提示用户输入用户名"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def verify_user(username, new_username):
    """验证用户，是否是上次运行程序的用户"""
    if new_username == username:
        return True
    else:
        return False


def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        new_username = input("Please enter your username: ")
        flag = verify_user(username, new_username)
        while not flag:
            print("You are not allow to login!")
            another_try = input("Please enter the right username('q' to quit): ")
            flag = verify_user(username, another_try)
        print("Welcome back, " + username + '!')
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + '!')


greet_user()
