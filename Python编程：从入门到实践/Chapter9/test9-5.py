# -*- coding:utf-8 -*-

# 9-5:尝试登陆次数

class User:
    """一个关于用户的类"""

    def __init__(self, first_name, last_name):
        """初始化属性"""
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe(self):
        """打印用户信息摘要"""
        print("This user's name is " + self.first_name.title() + ' ' + self.last_name.title() + '.')

    def greet_user(self):
        """向用户发出个性化的问候"""
        print("Hi, " + self.first_name.title() + ' ' + self.last_name.title() + '!')

    def increment_login_attempts(self):
        """将登陆次数增加1次"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """将登陆次数重置为0"""
        self.login_attempts = 0


user1 = User('li', 'lei')
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

print(user1.login_attempts)

user1.reset_login_attempts()
print(user1.login_attempts)