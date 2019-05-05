#!/usr/bin/python
# -*-coding:utf-8-*-
'''
编写人：王春雷
功能：从.txt中读取，分词，统计单词出现的频率
结果写入新的临时文件中。
'''

file = open("sentences.txt", "r").read() #读取文件
file = file.lower()  # 排除大小写干扰，全部小写

# 分词
strip_str = '?.(),:";->=\'\\+'#文档中需要忽略的内容
for ch in strip_str:
    file = file.replace(ch, ' ')#将所有的非字母字符用空格替换

counts = {}#计数

words = file.split()  # 将文本全部分割为单词
for word in words: #读取每个单词
    if word in counts:  #记录中如果有就把统计数加1
        counts[word] = counts[word] + 1
    elif word not in counts:  # 没有的话就把新的单词加入，统计数为1
        counts[word] = 1

items = list(counts.items())
items1 = sorted(items, key=lambda x: x[1], reverse=True)  # 按照词频降序处理

word_frequency = open('word_frequency.txt', 'w', encoding='utf-8')#临时文件

for i in items1:
    word_frequency.write('{0}:\t{1}\n'.format(i[0], i[1]))

word_frequency.close()