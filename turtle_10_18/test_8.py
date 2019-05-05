#!user/bin/python
#-*-coding:utf-8-*-
'''
编写人：王春雷
时间：2019.9.13
功能：红色的五角星
1.生成一个面板
2.画图
'''

import turtle
t = turtle.Pen()
t.color('red')
t.begin_fill()

for i in range(5):
    t.forward(100)
    t.right(144)

t.end_fill()

x = input(u'按任意键结束')