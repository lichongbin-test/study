#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# **第 0009 题：**一个HTML文件，找出里面的链接。

from bs4 import BeautifulSoup

def find_the_link(filepath):
    links = []
    with open(filepath) as f:
        text = f.read()
        bs = BeautifulSoup(text, features="html.parser")
        for i in bs.find_all('a'):
            links.append(i['href'])
    return links


if __name__ == '__main__':
    a = find_the_link(r'D:\pythonproject\study\08\test.html')
    print(a)