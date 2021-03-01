# -*- coding:utf-8 -*-

# 9-14：骰子

from random import randint


class Die:
    """模拟骰子的类"""

    def __init__(self, sides=6, count=10):
        """初始化属性"""
        self.sides = sides
        self.count = count

    def roll_die(self):
        """投骰子"""
        for i in range(1, self.count):
            side = randint(1, self.sides)
            print(side)


print("This is a die of 6 sides:")
die_6 = Die()
die_6.roll_die()

print("This is a die of 10 sides:")
die_10 = Die()
die_10.sides = 10
die_10.roll_die()

print("This is a die of 20 sides:")
die_20 = Die(20)
die_20.roll_die()
