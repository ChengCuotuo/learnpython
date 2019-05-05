#!user/bin/python
#-*-coding:utf-8-*-
'''
编写人：王春雷
功能：类，类方法的第一个变量必须是self
构造函数是__init__()
__表示private，并不是严格的私有，有方法可以获取
_表示protected
__xxx__表示系统定义的特殊成员
特殊：可以动态的给类和对象增加成员
'''

class Ball:
    def setName(self, name):
        self.name = name
        #为什么使用self？因为你长大了知道该使用那个参数
    def kick(self):
        print('我叫 %s, 该死的谁踢我' %self.name)

a = Ball()
a.setName('球A')
b = Ball()
b.setName('球B')
c=Ball()
c.setName('土豆')
a.kick()
c.kick()

