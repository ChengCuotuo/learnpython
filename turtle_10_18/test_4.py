#!user/bin/python
#-*-coding:utf-8-*-
'''
编写人：王春雷
时间：2019.9.13
功能：八边形
1.生成一个面板
2.画图
设置turtle画图的速度，t.speed(0)
fastest : 0  fast : 10 normal : 6 slow : 3  slowest : 1
t.Turtle().screen().delay(0)没有延迟
'''

import turtle
t = turtle.Pen();
t.speed(0)
for a in range(100):
    for b in range(3):
        t.forward(100)
        t.left(120)
    t.left(3.6)
x = input(u'按任意键结束')