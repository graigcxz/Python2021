# -*- coding:utf-8 -*-

# 8-8:用户的专辑

def make_album(singer_name, album_name, number_of_songs=''):
    """打印专辑信息"""
    if number_of_songs:
        album = {
            'name': album_name,
            'singer': singer_name,
            'number of songs': number_of_songs,
        }
    else:
        album = {
            'name': album_name,
            'singer': singer_name,
        }

    return album


while True:
    print("Enter your favorite album's information.")
    print("(Enter 'q' at any time to quit)")

    singer = input("Enter the singer name: ")
    if singer == 'q':
        break

    name = input("Enter the album name: ")
    if name == 'q':
        break

    number = input("Enter the number of the songs: ")
    # temp = int(number)
    if number == 'q':
        break

    final_album = make_album(singer, name, number)
    print(final_album)
    print('\n')
