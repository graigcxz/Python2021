# -*- coding:utf-8 -*-

# 9-9:电瓶升级

class Car:
    """模拟汽车的类"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """打印整齐的名字"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + "miles on it.")


class Battery:
    """模拟汽车电瓶的类"""

    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + " -KWh battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            car_range = 240
        elif self.battery_size == 85:
            car_range = 270

        message = "This car can go approximately " + str(car_range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        """升级电瓶容量"""

        if self.battery_size != 85:
            self.battery_size = 85


class ElectricCar(Car):
    """模拟电动车的类"""

    def __init__(self, make, model, year):
        """初始化父类的属性"""

        super().__init__(make, model, year)
        self.battery = Battery()


my_car = ElectricCar('tesla', 'model Y', 2020)
my_car.battery.get_range()

print("UPGRADING...")
my_car.battery.upgrade_battery()
my_car.battery.get_range()
