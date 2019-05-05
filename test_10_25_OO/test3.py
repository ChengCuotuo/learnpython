#!user/bin/python
#-*-coding:utf-8-*-
'''
编写人：王春雷
功能：类，类方法的第一个变量必须是self
可以动态的添加变量，这个类中根本就没有定义color变量，但是在初始化的时候可以直接生成
'''

class Car:
    price=10000
    def __init__(self, c):
        self.color=c
    def print(self):
        print('颜色：%s, 价格：%s' %(self.color, self.price))

car1  = Car('Red')
car2 = Car('Blue')
car1.print()
car2.print()