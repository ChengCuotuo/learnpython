#!user/bin/python
#-*-coding:utf-8-*-
'''
编写人：王春雷
功能：自然语言处理
自然语言的歧义性和多义性提高了自然语言处理的困难性
需要：知识库，规则
应用：关键字提取，生成文章摘要

自然语言处理:
    哈工大的语言技术平台：Language Technology Platform，LTP
    python的jieba库
'''
import jieba
s=u'我想和女朋友一起去北京故宫博物馆参观和闲逛'
cut = jieba.cut(s)
print ('[Output]')
print (cut) #这句是错误的，每个分词需要连接符，下面一句话是正确的
print (','.join(cut)) #使用逗号连接分词
