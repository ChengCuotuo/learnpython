#!user/bin/python
#-*-coding:utf-8-*-
'''
编写人：王春雷
时间：2019.9.13
功能：lambda
'''

f = lambda x, y, z : x + y + z
print(f(1, 2, 3))

g = lambda x, y = 2, z = 3: x + y + z
print(g(1))

print(g(2, z = 4, y = 4))