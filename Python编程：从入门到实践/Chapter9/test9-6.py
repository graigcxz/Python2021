# -*- utf-8 -*-

# 9-6：冰激淋小店

class Restaurant:
    """一个关于餐厅的类"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """描述餐厅基本信息"""
        print(self.restaurant_name + "'s cuisine type is " + self.cuisine_type + ".")

    def open_restaurant(self):
        """指出餐厅正在开门营业"""
        print(self.restaurant_name + " is opening.")

    def set_number_served(self, number):
        """设置就餐人数"""
        self.number_served = number

    def increment_number_served(self, numbers):
        """将人数增加指定的量"""
        self.number_served += numbers


class IceCreamStand(Restaurant):
    """一个冰激淋小店的类"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化父类的属性"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def show_icecream(self):
        """显示冰激淋种类"""
        for flavor in self.flavors:
            print("Here is icecream of " + flavor + " flavor.")


icecream_stand = IceCreamStand('Diary Queen', 'IceCream')
icecream_stand.flavors = ['chocolate', 'coco', 'milk']
icecream_stand.describe_restaurant()
icecream_stand.open_restaurant()
icecream_stand.show_icecream()

