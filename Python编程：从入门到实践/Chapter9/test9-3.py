# -*- coding:utf-8 -*-

# 9-2:用户

class User:
    """一个关于用户的类"""

    def __init__(self, first_name, last_name):
        """初始化属性"""
        self.first_name = first_name
        self.last_name = last_name

    def describe(self):
        """打印用户信息摘要"""
        print("This user's name is " + self.first_name.title() + ' ' + self.last_name.title() + '.')

    def greet_user(self):
        """向用户发出个性化的问候"""
        print("Hi, " + self.first_name.title() + ' ' + self.last_name.title() + '!')


user1 = User('li', 'lei')
user2 = User('wang', 'meimei')

user1.describe()
user1.greet_user()

user2.describe()
user2.greet_user()