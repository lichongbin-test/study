#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# **第 0008 题：**一个HTML文件，找出里面的正文。

from bs4 import BeautifulSoup

def find_the_content(filepath):
    with open(filepath) as f:
        text = BeautifulSoup(f, features="html.parser")
        content = text.get_text().strip('\n')
        return content.encode('gbk', 'ignore')


if __name__ == '__main__':
    a = find_the_content(r'D:\pythonproject\study\08\test.html')
    print(a)