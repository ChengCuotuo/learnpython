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
#设置画笔的颜色
t.pencolor('red')
#笔落在面板上，可以画图
t.pendown()
#设置填充颜色
t.fillcolor('blue')
#开始填充
t.begin_fill()
for i in range(3):
    t.forward(200)
    t.right(90)
#结束填充，期间画的内容被填充指定颜色
t.end_fill()
#画笔抬起
t.penup()
#将画笔转到指定位置
t.goto(100, -100)
t.write(u'软件16学习Python学习')
t.goto(500, 500)
x = input(u'按任意键继续')