#!user/bin/python
#-*-coding:utf-8-*-
'''
编写人：王春雷
时间：2019.9.13
功能：lambda,map表示映射
'''

L = [1,2,3,4,4]
print(list(map(lambda x : x + 10, L)))
print(L)