# -*- coding:utf-8 -*-

import unittest

from employee import Employee


class TestSalaryRaise(unittest.TestCase):
    """针对Employee类的测试"""

    def setUp(self):
        """
        创建两个薪资涨幅和答案，供测试方法使用
        """
        self.employee = Employee('chang', 'xinzhuo', 10000)

    def test_give_default_raise(self):
        """测试默认涨薪"""
        raising = self.employee.give_raise()
        self.assertEqual(raising, 15000)

    def test_give_custom_raise(self):
        """测试自定义涨薪"""
        self.salary_raise1 = 10000
        raising = self.employee.give_raise(self.salary_raise1)
        self.assertEqual(raising, 20000)


unittest.main()
