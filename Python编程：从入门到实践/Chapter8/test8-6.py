# -*- coding:utf-8 -*-

# 8-6:城市名

def city_country(city_name, country_name):
    """返回格式化的城市-国家字符串"""
    message = city_name.title() + ', ' + country_name.title()
    return message


while True:
    print("Enter 'q' to quit any time.")

    city = input("Enter a city name: ")
    if city == 'q':
        break

    country = input("Enter a country name: ")
    if country == 'q':
        break

    print(city_country(city, country))
    print('\n')
