#!user/bin/python
#-*-coding:utf-8-*-
'''
编写人：王春雷
时间：2019.9.13
功能：自定义函数
'''

def myAbs(n):
    if not isinstance(n, int):
        return -1
    else:
        if n > 0:
            return n
        else:
            return -n

a =input('输入一个数字:')
print(myAbs(a))