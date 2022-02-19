#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# **第 0006 题：**你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。

import glob
from collections import Counter
import re


def key_words(path):
    a = glob.glob(f'{path}/*.txt')
    #print(a)
    wordlist = []
    for x in a:
        f = open(x, 'r').read()
        words = re.findall(r'[a-zA-Z0-9]+', f)
        for y in words:
            wordlist.append(y)
        #print(wordlist)
        most_num = Counter(wordlist).most_common(3)
        print(f"文件{x}中的高频词top3：", most_num)


if __name__ == '__main__':
    path = 'D:\\pythonproject\\study\\06'
    key_words(path)
