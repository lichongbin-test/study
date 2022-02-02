#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# 第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果
'''
1.坐标（0，0）表示左上角，整个图片类似镶嵌在坐标的第四象限；img.size是一个二位数组，依次为图片的宽和高。
2.在图片上添加内容时注意对应内容也会占位置，所以不能当作点即pixel来看待，实际处理时需要考虑添加对象的size，这就对应代码中右上角坐标position的获取。
3.ImageFont的获取有很多方法，其中较简单的方法是从truetype中获取，对应font存放的位置一般是/usr/share/fonts/...
4.windows下试用相对路径可能会出现资源无法打开的报错，可以试用绝对路径。123456789
'''

from PIL import Image,ImageDraw,ImageFont

def add_num(picPath,num):
    img = Image.open(picPath)
    xSize, ySize = img.size
    fontsize = ySize // 6
    position = xSize - fontsize - 75
    myfont = ImageFont.truetype('D:\\pythonproject\\study\\00\\YouSheBiaoTiHei-2.ttf',fontsize)
    ImageDraw.Draw(img).text((position,0), str(num), font=myfont, fill='red')
    img.save('D:\\pythonproject\\study\\00\\icon_with_num.jpg')

if __name__ == '__main__':
    picPath = 'D:\\pythonproject\\study\\00\\heidan.jpg'
    num = 99
    add_num(picPath,num)