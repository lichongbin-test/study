#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# **第 0009 题：**使用 Python 生成类似于图中的字母验证码图片。

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

# 随机字母：
def rnd_char():
    return chr(random.randint(65, 90))

# 随机颜色1：
def rnd_color1():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2：
def rnd_color2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


if __name__ == '__main__':
    width = 60 * 4
    height = 60
    image = Image.new('RGB', (width, height), (255, 255, 255))
    # 创建Font对象：
    font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 36)
    # 创建Draw对象：
    draw = ImageDraw.Draw(image)
    # 填充每个像素：
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rnd_color1())
    # 输出文字：
    for t in range(4):
        draw.text((60 * t + 10, 10), rnd_char(), font=font, fill=rnd_color2())
    # 模糊：
    image = image.filter(ImageFilter.BLUR)
    image.save(r'D:\pythonproject\study\10\test.jpg', 'jpeg')
