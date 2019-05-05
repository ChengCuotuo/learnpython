#!user/bin/python
#-*-coding:utf-8-*-
'''
编写人：王春雷
时间：2019.9.13
功能：八边形
1.生成一个面板
2.画图
'''

import turtle

t = turtle.Pen()
edge = int(input(u'输入多边形的边数：'))
#degree = 180 - ((edge - 2) * 180 / 8)
degree = 360.0 / edge

for a in range(edge):
    t.forward(45)
    t.left(degree)
