# -*- coding:utf-8 -*-

# 8-12：三明治

def sandwich_ingredients(*ingredients):
    """对三明治添加一系列食材"""
    for ingredient in ingredients:
        print("ADDING: " + ingredient)

    print("Your sandwich contains: ")
    print(ingredients)


sandwich_ingredients('tomato', 'banana')
sandwich_ingredients('tomato', 'banana', 'apple')
sandwich_ingredients('tomato', 'banana', 'orange', 'beef')
