#!user/bin/python
#-*-coding:utf-8-*-
'''
编写人：王春雷
时间：2019.9.13
功能：蜂巢
'''
# 'fastest': 0
# 'fast': 10
# 'normal': 6
# 'slow': 3
# 'slowest: 1

import turtle

def hexagon(size):
    for i in range(6):
        turtle.forward(size)
        turtle.left(60)
def honeyhexagon(size):
    turtle.speed(0)
    for i in range(6):
        hexagon(size)
        turtle.forward(size)
        turtle.right(60)

honeyhexagon(80)
a = input()