# -*- coding:utf-8 -*-

# 8-11:不变的魔术师


def make_great(names):
    """在名字中增加’The Great’字样"""
    new_names = []
    while names:
        current_name = names.pop()
        new_name = 'The Great ' + current_name
        new_names.append(new_name)

    return new_names


def show_magicians(names):
    """打印名字"""
    for name in names:
        print(name)


magicians = ['Johnson', 'Lebron', 'Kobe', 'Jordan']
great_magicians = make_great(magicians[:])
print('great magicians:')
show_magicians(great_magicians)
print('magicians: ')
show_magicians(magicians)
