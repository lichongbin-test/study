#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#**第 0001 题：**做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用**生成激活码**（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？

import random, string

def random_str(filename, num, length):
    f = open(filename, 'w')
    for i in range(num):
        chars = string.ascii_letters + string.digits
        s = [random.choice(chars) for i in range(length)]
        f.write(''.join(s) + '\n')
    f.close()

if __name__ == '__main__':
    filename = "D:\\pythonproject\\study\\01\\Running_resul.txt"
    num = 100
    length = 9
    random_str(filename, num, length)