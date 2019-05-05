#!user/bin/python
#-*-coding:utf-8-*-
'''
编写人：王春雷
时间：2019.9.13
功能：面积
'''

import math

def circleArea(r):
    if isinstance(r, (int, float)):
        return r * r * math.pi
    else :
        print('数据类型错误')

area_circle = circleArea(1.5)
print('半径为1.5的圆的面积是: ', end='')
print(area_circle)

def triangleArea(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a * b / 2
    else :
        print('数据类型错误')

area_triangle = triangleArea(3, 4)
print('地为3，高为4的三角形的面积是: ', end='')
print(area_triangle)