# -*- coding:utf-8 -*-

# 5-10: 检查用户名

current_users = ['Tom', 'Fred', 'Brad', 'Kobe', 'Lebron']
new_users = ['James', 'Tom', 'Kobe', "Mike", 'Larry']

current_users_lower = []
for current_user in current_users:
    current_users_lower.append(current_user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("You need to enter a new user name.")
    else:
        print("You can use this name.")
