#!user/bin/python
#-*-coding:utf-8-*-
'''
编写人：王春雷
时间：2019.9.13
功能：if-else
'''

while True:
    num = int(input(u"输入孔子的年龄:"))
    if num >= 0:
        if  num <= 15:
            print("玩泥巴")
        elif num <= 30:
            print(u"专心致志学习")
        elif num <= 40:
            print("能够自理")
        elif num <= 50:
            print("不为外界事物所迷惑")
        elif num <= 60:
            print("懂得了天命")
        elif num <= 70:
            print("能听得进不同的意见")
        elif num <= 73:
            print("随心所欲，而不超出规矩")
        else :
            print("已经去世")
    else :
        print('输入年龄错误')
