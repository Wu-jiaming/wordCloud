from os import path

from wordcloud import WordCloud, STOPWORDS

import numpy as np

from PIL import Image

import matplotlib.pyplot as plt

import random

import os

def grey_color_func(word, font_size, position, orientation, random_stata=None, **kwargs):

    #颜色HSL(色度、饱和度、亮度),亮度随机
    return 'hsl(0, 0%%, %d%%)' % random.randint(60, 100)

#当前文件夹所在目录

d = path.dirname(__file__)

#读取背景图片

mask = np.array(Image.open(path.join(d, 'ingram3.jpg')))

#读取一个txt文件

text = open(u'source.txt', encoding='utf-8').read()

#停用词词库

stopwords = set(STOPWORDS)
# 添加电影剧本特定的停用词
stopwords.add("int")

stopwords.add("ext")

#设置词云属性，其中第一个参数非常重要，若没有正确设置，

#将不能解析中文，出现乱码

wc = WordCloud(font_path='./fonts/simhei.ttf', max_words=2000, mask=mask,

               stopwords=stopwords, margin=10,

               #图片边缘宽度，以及颜色
               contour_width=1, contour_color='steelblue',

               random_state=2).generate(text)

default_colors = wc.to_array()

plt.title("Custom colors")

plt.imshow(wc.recolor(color_func=grey_color_func, random_state=3))

wc.to_file('001.png')

plt.axis("off")#不显示坐标尺寸

#显示生成的ciyun

plt.figure()
plt.title("Mixure colors")

plt.imshow(default_colors)

plt.axis("off")

plt.show()