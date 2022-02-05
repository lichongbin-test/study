#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# **第 0003 题：**将 0001 题生成的 200 个激活码（或者优惠券）保存到 **Redis** 非关系型数据库中。

import redis


def store_redis(filepath: str, keyname: str):
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    f = open(filepath, 'rb')
    i = 0
    for line in f.readlines():
        code = line.strip()  # 用strip把\n去掉
        r.hset(keyname, i, code)
        # r.set(i, code)
        i += 1


if __name__ == '__main__':
    store_redis(r'D:\pythonproject\study\01\Running_resul.txt', 'study')
