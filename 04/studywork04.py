#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#**第 0004 题：**任一个英文的纯文本文件，统计其中的单词出现的个数。

import re

def statistics(file_path):
    f = open(file_path, 'r').read()
    #words = re.findall(r'[\w\-\_\.\']+',f)
    words = re.findall(r'[a-zA-Z0-9]+', f)
    print(len(words))
    return 0

if __name__ == '__main__':
    file_path = 'D:\\pythonproject\\study\\04\\test.txt'
    statistics(file_path)