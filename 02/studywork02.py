#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# **第 0002 题**：将 0001 题生成的 200 个激活码（或者优惠券）保存到 **MySQL** 关系型数据库中。

import pymysql


def store_mysql(filepath: str):
    db = pymysql.connect(host="localhost", user="root", passwd="123456", db="study")
    cursor = db.cursor()

    # 判断表是否存在
    cursor.execute('show tables in study')
    tables = cursor.fetchall()
    findtables = False
    for table in tables:
        if 'code' in table:
            findtables = True
            print("the table is already exist")
    if not findtables:
        cursor.execute('''
                    CREATE TABLE code(
                    id int not null auto_increment,
                    code VARCHAR(10),
                    PRIMARY KEY (id));
        ''')
    # 逐行拉取数据写入表中
    f = open(filepath, 'rb')
    for line in f.readlines():
        coupon = line.strip()  # 用strip把\n去掉
        #也可以用coupon = line[:-1]去除\n符号
        cursor.execute("INSERT INTO code (code) VALUES (%s);", [coupon])
        # coupon会报错，格式问题，插入数据库里的数据必须要变为list，所以用[coupon]

    db.commit()
    cursor.close()
    db.close()


if __name__ == '__main__':
    store_mysql(r'D:\pythonproject\study\01\Running_resul.txt')
