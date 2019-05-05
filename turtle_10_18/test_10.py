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
turtle.bgcolor('black')
t.speed(0)
colors = ['red', 'yellow', 'blue']
for x in range(250):
    t.pencolor(colors[x%3])
    t.forward(2 * x)
    t.left(120)
t.sleep(1)