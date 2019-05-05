#!user/bin/python
#-*-coding:utf-8-*-
'''
编写人：王春雷
时间：2019.9.13
功能：x^y，也存在局部变量的状况
'''

def my_pown(x, y=2):
    #其中的y是默认参数，如果传参只有一个，y就会默认当做2处理，必须在参数的最右端
    temp = x
    if y == 0:
        return 1
    else :
        return x ** y;

print(my_pown(2, 3))
print(my_pown(3))