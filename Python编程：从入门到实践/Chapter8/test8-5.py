# -*- coding:utf-8 -*-

# 8-5:城市

def describe_city(city_name, country_name='China'):
    """显示城市所属的国家"""
    print(city_name.title() + ' is in ' + country_name.title() + '.')


describe_city('shanghai')
describe_city('beijing')
describe_city('Reykjavik', 'iceland')
