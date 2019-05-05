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
import random
t = turtle.Pen()
turtle.bgcolor('black')
t.color('white')
t.fillcolor('yellow')

t.speed(0)

t.penup()
t.goto(-400, 300)
t.write(u'星空')
for a in range(12):
    t.penup()
    t.goto(random.randint(-400, 300), random.randint(-400, 300))
    t.pendown()
    t.begin_fill()
    for x in range(1, 19):
        t.forward(30)
        if x % 2 == 0:
            t.left(175)
        else:
            t.left(225)
    t.end_fill()

x = input(u'按任意键继续')