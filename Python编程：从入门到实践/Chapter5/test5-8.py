# -*- coding: utf-8 -*-

# 5-8: 以特殊方式跟管理员打招呼

names = ['Tom', 'Fred', 'Brad', 'Kobe', 'Lebron']

for name in names:
    if name == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + name + ', thank you for logging in again')
