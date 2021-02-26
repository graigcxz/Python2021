"""一个用来表示电动汽车的类"""

from car import Car


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
