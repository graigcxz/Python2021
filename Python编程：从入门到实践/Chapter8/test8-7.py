# -*- coding:utf-8 -*-

# 8-7:专辑

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


print(make_album('周杰伦', '叶惠美'))
print(make_album('周杰伦', '七里香', '12'))
print(make_album('langlang', 'piano'))
