#!user/bin/python
#-*-coding:utf-8-*-
'''
编写人：王春雷
时间：2019.9.13
功能：计算器
'''

def add(n1, n2):
    return n1 + n2;

def substract(n1, n2):
    return n1 - n2;

def multiply(n1, n2):
    return n1 * n2;

def divide(n1, n2):
    if n2 != 0:
        return n1 / n2;

def calculate(n1, ch, n2):
    if ch == '+':
        return add(n1, n2)
    elif ch=='-':
        return substract(n1, n2)
    elif ch=='*':
        return multiply(n1, n2)
    elif ch=='/':
        divide(n1, n2)

num1 = int(input('输入第一个数字：'))
ch = input('输入运算符：')
num2 = int(input('输入第二个数字：'))

print(calculate(num1, ch, num2))
