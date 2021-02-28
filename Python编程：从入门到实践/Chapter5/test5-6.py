# -*- coding: utf-8 -*-

# 5-6: 人生的不同阶段

age = int(input("Enter your age:"))

if age < 2:
    print("你是一个婴儿。")
elif 2 <= age < 4:
    print("你在蹒跚学步。")
elif 4 <= age < 13:
    print("你是一个儿童")
elif 13 <= age < 20:
    print("你是一个青少年。")
elif 20 <= age < 65:
    print("你是一个成年人。")
else:
    print("你是一个老年人。")
