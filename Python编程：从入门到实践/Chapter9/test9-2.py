# -*- coding:utf-8 -*-

# 9-2:三家餐馆

class Restaurant:
    """一个关于餐厅的类"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """描述餐厅基本信息"""
        print(self.restaurant_name + "'s cuisine type is " + self.cuisine_type + ".")

    def open_restaurant(self):
        """指出餐厅正在开门营业"""
        print(self.restaurant_name + " is opening.")


restaurant1 = Restaurant('魏家凉皮', '陕西小吃')
restaurant2 = Restaurant('老火大骨头', '街边菜')
restaurant3 = Restaurant('江南春', '徽菜')

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
