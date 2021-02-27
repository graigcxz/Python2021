# -*- coding:utf-8 -*-

class Employee:
    """一个描述雇员的类"""

    def __init__(self, first_name, last_name, salary):
        """初始化属性"""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, salary_raise=5000):
        """给员工加薪"""
        self.salary += salary_raise
        return  self.salary
