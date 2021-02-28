# -*- coding:utf-8 -*-

# 8-13：用户简介

def build_profile(first, last, **user_info):
    """创建一个字典，包含我们知道的关于用户的一切"""
    profile = {'first_name': first, 'last_name': last}
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('chang', 'Shinzo',
                             lacation="xi'an",
                             age='32')

print(user_profile)
