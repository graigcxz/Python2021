# -*- coding:utf-8 -*-

# 9-8:权限

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


class Privilege:
    """模拟管理员的权限"""

    def __init__(self):
        """初始化权限的属性"""
        self.privileges = ['can add post', 'can delete post', 'can ban user', 'can fly']

    def show_privileges(self):
        """显示管理员的特权"""
        for privilege in self.privileges:
            print(privilege)


class Admin(User):
    """一个管理员的类"""

    def __init__(self, first_name, last_name):
        """初始化父类的属性"""
        super().__init__(first_name, last_name)
        self.privileges = Privilege()


admin = Admin('micheal', 'jordan')
admin.privileges.show_privileges()
