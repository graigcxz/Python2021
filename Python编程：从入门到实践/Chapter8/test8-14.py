# -*- coding:utf-8 -*-

# 8-14：汽车

def make_car(manufacturer, model, **car_info):
    """
    包含一切关于汽车的信息
    :param manufacturer:制造商
    :param model: 型号
    :param car_info: 其他信息
    :return: 一个关于汽车的字典
    """
    car_profile = {'manufacturer': manufacturer, 'model': model}
    for key, value in car_info.items():
        car_profile[key] = value

    return car_profile


car = make_car('subaru', 'outback', color='blue', two_package=True)
print(car)
