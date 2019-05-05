#!user/bin/python
#-*-coding:utf-8-*-
'''
编写人：王春雷
时间：2019.9.13
功能：map中的split（），数值交换
'''

x=input('Input two number:')
a,b=map(int, x.split())#第一个参数，表示将划分出来的内容按照指定的数据类型进行转换
if a > b :
    a, b = b, a#序列解包，交换两个变量的值
print(a, b)

