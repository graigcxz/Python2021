# -*- coding:utf-8 -*-

# 9-1:餐馆

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


restaurant = Restaurant('魏家凉皮', '陕西小吃')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
