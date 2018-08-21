from os import path

from wordcloud import WordCloud, STOPWORDS

import numpy as np

from PIL import Image

import matplotlib.pyplot as plt

import random

import os

#生成一张词云颜色是由灰色往白色随机
def grey_color_func(word, font_size, position, orientation, random_stata=None, **kwargs):

    #颜色HSL(色度、饱和度、亮度),亮度随机
    return 'hsl(0, 0%%, %d%%)' % random.randint(60, 100)

#当前文件夹所在目录

d = path.dirname(__file__)

#读取背景图片
#根据文档说明，遮罩图片的白色部分将被视作透明，只在非白色部分区域作图。找到黑色背景素材图。
mask = np.array(Image.open(path.join(d, 'ingram3.jpg')))

#读取一个txt文件

text = open('source.txt', encoding='utf-8').read()

#停用词词库

stopwords = set(STOPWORDS)
# 添加电影剧本特定的停用词
stopwords.add("int")

stopwords.add("ext")

#设置词云属性，其中第一个参数非常重要，若没有正确设置，

#将不能解析中文，出现乱码
#从文本生成词云图
wc = WordCloud(font_path='./fonts/simhei.ttf', max_words=2000, mask=mask,

               stopwords=stopwords, margin=10,

               #图片边缘宽度，以及颜色
               contour_width=1, contour_color='steelblue',

               random_state=2).generate(text)
#以numpy矩阵的格式返回词云图
default_colors = wc.to_array()

plt.title("Custom colors")
#重新上色
#random_state:随机种子，整型或None
plt.imshow(wc.recolor(color_func=grey_color_func, random_state=None))

#保存图片
wc.to_file('001.png')

plt.axis("off")#不显示坐标尺寸

#显示生成的ciyun
#画图
plt.figure()
plt.title("Mixure colors")

plt.imshow(default_colors)

plt.axis("off")

plt.show()