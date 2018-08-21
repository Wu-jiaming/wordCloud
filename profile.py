from os import path
from PIL import Image#打开图片
import numpy as np#用矩阵加载图片数据
import matplotlib.pyplot as plt#画图
from wordcloud import WordCloud,STOPWORDS
import random

#获取当前根目录
pwd = path.dirname(__file__)
txt_path = path.join(pwd, 'bigdata.txt')
#读取数据源文件
text = open(txt_path, encoding='utf-8').read()

image_path = path.join(pwd, 'huge.jpg')
#image打开图片
image_open = Image.open(image_path)
#使用numpy加载图片矩阵信息
alice_mask = np.array(image_open)

#排除文本种的单词，譬如said
stopwords = STOPWORDS.add("said")

wc = WordCloud(
            #background_color = "white",
                random_state=1，#随机上色1号随机种子
               max_words = 1000,
               mask = alice_mask,#词云再图片显示的区域
               stopwords = stopwords
               )
wc = wc.generate(text)#生成词云

save_path = path.join(pwd, "profile.png")
wc.to_file(save_path)

#生成一张黑色背景，词云为彩色的图片

#灰色到白色过度颜色随机
def gray_color_func(word, font_size, position, orientation, random_stata=None, **kwargs):
    #颜色HSL(色度、饱和度、亮度),亮度随机
    return 'hsl(0, 0%%, %d%%)' % random.randint(60, 100)

#展示图片
plt.imshow(wc)
plt.axis("off")

#又画一张图
plt.figure()
#灰色
wc_gray = wc.recolor(color_func = gray_color_func, random_state=None)
plt.imshow(wc_gray)
plt.axis("off")

#画一张图
plt.figure()
plt.imshow(alice_mask, cmap=plt.cm.gray)
plt.axis("off")
plt.show()
