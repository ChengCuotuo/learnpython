#!user/bin/python
#-*-coding:utf-8-*-
'''
编写人：王春雷
功能：类，类方法的第一个变量必须是self
'''

class Car :
    def infor(self):
        print('Hello world')

car = Car();
car.infor();