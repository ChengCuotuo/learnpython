import jieba
from collections import Counter
from wordcloud import WordCloud
from matplotlib import pyplot as plt
from PIL import Image
import numpy as np
import jieba.posseg as pseg
from pyecharts import Bar

# 读取文件
article = open('水浒传.txt','r',encoding='utf-8').read()

# 分词 词性
jieba.load_userdict('userdic.txt') #导入自己的分词标准，自定义词典
words = jieba.cut(article)
wordlist = list(words)

wordcixing = pseg.cut(article)
santiwords_withAttr = []
with open("psegshuihu.txt", "w", encoding="utf-8") as fw:
    for wp in wordcixing:
        if len(wp.word) > 1:
            fw.write(wp.word)
            fw.write(wp.flag)
            fw.write("\n")
            santiwords_withAttr.append((wp.word, wp.flag))

# 统计人名
'''
pername = [x[0] for x in santiwords_withAttr if x[1]=="nr"]
#print(pername)
c = Counter(pername).most_common(10)
with open('pername.txt', 'w') as fw:
    for x in c:
        fw.write("{0},{1}\n".format(x[0], x[1]))
print(c)
bar = Bar('pername', 'pernamecounter')
bar.add('',c[0], c[1],lenged_txt_color='blue')
bar.render("pername.html")
'''
# 统计地名
perpostion = [x[0] for x in santiwords_withAttr if x[1]=="ns"]
#print(pername)
s = Counter(perpostion).most_common(10)
with open('perpostion.txt', 'w') as fw:
    for x in s:
        fw.write("{0},{1}\n".format(x[0], x[1]))

print(s)