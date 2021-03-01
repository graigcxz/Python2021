"""一个可以用于表示汽车的类"""


class Car:
    """模拟汽车的类"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 50

    def get_descriptive_name(self):
        """打印整齐的名字"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name

    def read_odometer(self):
        """打印当前汽车的里程数"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can not roll back.")

    def increment_odometer(self, miles):
        """将里程表增加指定的量"""
        self.odometer_reading += miles
