#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# *第 0005 题：**你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。

import os
import glob
from PIL import Image


def thumbnail_pic(path):
    a = glob.glob('**/*.jpg')  # './pic/*.jpg'的方式可以只提取指定路径下的文件
    # print(a)
    for x in a:
        filepath, filename = os.path.split(x)
        # print(filepath)
        # print(filename)
        im = Image.open(x)
        im.thumbnail((640, 400))
        print(im.format, im.size, im.mode)
        # im.save(name, 'JPEG', path='D:\\pythonproject\\study\\05\\out')
        im.save(path + '/out/' + filename)
    print('Done!')


if __name__ == '__main__':
    path = '.'
    thumbnail_pic(path)
