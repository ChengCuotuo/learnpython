#!user/bin/python
#-*-coding:utf-8-*-
'''
编写人：王春雷
时间：2019.9.13
功能：正方形
1.生成一个面板
2.画图
'''

import turtle
t = turtle.Pen()

for x in range(4):
    t.forward(100)
    t.left(90)

x=input(u'按任意键结束')