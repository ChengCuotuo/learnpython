#!user/bin/python
#-*-coding:utf-8-*-
'''
自然语言处理
实现的功能有：
    1.文件的读取；2.使用jieba分词；3.用分词结果画出词云；4.用分词结果画柱状图；5.用分词结果画饼状图
'''
import jieba                            #jiea库用于分词
import jieba.posseg as pseg             #词性标注也叫词类标注。POS tagging是part-of-speech tagging的缩写
from collections import Counter         #统计
from  wordcloud import WordCloud        #画词云
from matplotlib import pyplot as plt    #matplotlib在python中一般会与numpy同时出现
import numpy as np                      #解决数据的可视化问题
from PIL import Image                   #导入图片处理库，可以使用指定的png格式的图片显示词云
from pyecharts import Bar               #画柱状图
from pyecharts import Pie               #画饼状图

#读取水浒传中的内容将它分词
with open(u'水浒传.txt', 'r', encoding='utf-8') as fr:     #只读模式将水浒传按照utf-8的编码方式读出
    article = fr.read();

#进行简单分词，用出现次数最多的100个词语画词云，使用指定的png格式的图片生成词云
jieba.load_userdict('userdic.txt')                      #导入自己的分词标准，自定义词典，这里主要针对的是下面的地名分词异常
words = jieba.cut(article)
wordlist = list(words)

#处理背景图片
image1 = Image.open("1.png")                            #打开图片
image2 = np.array(image1)                               #将图片变成矩阵
#绘制词云
listStr="/".join(wordlist)                              #使用/连接
wc=WordCloud(background_color="white",                  #背景色
             mask=image2,                               #确定使用的矩阵
             max_words=100,                             #最多词数
             font_path="C:\Windows\Fonts\simfang.ttf",  #字体路径
             max_font_size=50,                          #字体的最大值
             random_state=30,                           #随机状况
             margin=2)                                  #词距离
wc.generate(listStr)                                    #对listStr生成词云
plt.figure("wc")                                        #生成图形案例
wc.to_file("wc1.png")                                   #保存为图片
plt.imshow(wc)                                          #显示图片函数
plt.axis("off")                                         #关闭坐标系
plt.show()                                              #显示

'''
清洗数据：
    将读到的词，重新按照词性进行分词
    把words中每一行中的词语长度大于1的连同词性写入 psegshuihu.txt中
    将这些结果存储到santiwords_withAttr中用于其他处理
'''
words = pseg .cut(article)    #将读取到的内容按照词性进行分词
santiwords_withAttr = []      #用来记录按词性划分之后的words内容

with open('psegshuihu.txt', 'w', encoding='utf-8') as  fw:
    for wp in words:
        if len(wp.word) > 1:
            fw.write(wp.word)
            fw.write(wp.flag)
            fw.write("\n")
            santiwords_withAttr.append((wp.word, wp.flag))  #把读到的词内容和词性当作一个元组存储


'''
画柱状图：
    统计分词结果中的人名（词性为nr表示人名）
    将出现次数最多的前十个人名 写入文件pername.txt
    用出现次数最多的前十个人名画柱状图
'''
#依次处理santiwords_withAttr中数据，如果词性是人名就将它的人名和出现次数记录到prename中
pername = [x[0] for x in santiwords_withAttr if x[1]=="nr"]
listName = []                                           #记录所有的姓名
listNameCount = []                                      #对应记录姓名出现的次数，用来生成柱状图
#print(pername)
c = Counter(pername).most_common(10)                     #统计人名出现次数最多的前十个
with open('pername.txt', 'w') as fw:
    for x in c:
        fw.write("{0},{1}\n".format(x[0], x[1]))        #格式化输入
        listName.append(x[0])
        listNameCount.append(x[1])

#print(c)
bar = Bar('pername', 'pernamecounter')                      #定义横纵坐标
bar.add('',listName, listNameCount, lenged_txt_color='blue')#对应横纵坐标把人名和次数绘制柱状图
bar.render("pername.html")                                  #将绘制完成的柱状图保存为pername.html格式

'''
画饼状图：
    统计分词结果中的地名（词性为ns表示地名）
    将出现次数最多的前十个地名 写入文件perpostion.txt
    用出现次数最多的前十个地名画饼状图
    
说明：
    地点查询如下：很明显里面的有的并不是地名，需要使用自定义词典，将里面的词性重新定义
    第23行已经做出了处理
    此博客中有词性分类：https://www.cnblogs.com/tomato0906/articles/5600348.html
[('哥哥', 734), ('山寨', 291), ('东京', 236), ('下山', 230), ('上山', 230),
 ('朝廷', 188), ('西门庆', 176), ('上马', 146), ('大汉', 133), ('济州', 126)]
'''
perpostion = [x[0] for x in santiwords_withAttr if x[1]=="ns"]
listPosition = []                                    #记录所有的地址名
listPositionCount = []                               #对应记录地址名出现的次数
#print(pername)
s = Counter(perpostion).most_common(10)
with open('perpostion.txt', 'w') as fw:
    for x in s:
        fw.write("{0},{1}\n".format(x[0], x[1]))
        listPosition.append(x[0])
        listPositionCount.append(x[1])
#print(s)
pie=Pie('pie')                                         #初始化饼状图对象
pie.add('',listPosition, listPositionCount)            #添加饼状图每个扇区需要的名称和数值信息
pie.render('prepie.html')                              #将饼状图保存为prepie.html文件