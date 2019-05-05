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
t.speed(0)
# t.circle(100, extent=None, steps=None)
# t.circle(100, extent=None, steps=5)
# t.circle(100, steps=50)

for a in range(100):
    t.circle(50, extent=None, steps=None)
    t.left(3.6)

x = input(u'按任意键继续')