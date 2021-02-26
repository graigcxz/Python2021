"""一个描述餐馆的类"""


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
