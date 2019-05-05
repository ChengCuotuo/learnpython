#!user/bin/python
#-*-coding:utf-8-*-
'''
编写人：王春雷
时间：2019.9.13
功能：自定义函数，求斐波那契数
'''

def fib(n):#定义函数名以及参数
    a, b = 0, 1
    while a < n:
        print(a, end='')
        a, b = b, a + b
        print()
    #注意缩进，函数结尾可以有return
fib(1000)#函数调用