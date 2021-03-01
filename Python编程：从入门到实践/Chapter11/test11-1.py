# -*- coding:utf-8 -*-

import unittest

from city_functions import print_city_country


class PrintTestCase(unittest.TestCase):
    """测试city_functions.py"""

    def test__city_country(self):
        """能正确打印吗"""
        message = print_city_country('santiago', 'chile')
        self.assertEqual(message, 'Santiago, Chile')


unittest.main()
