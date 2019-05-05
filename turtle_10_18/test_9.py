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
t.speed(0)

for x in range(1000):
    # t.forward( 2 * x)
    # t.left(91)
    t.circle(x)
    t.left(45)

x = input(u'按任意键结束')