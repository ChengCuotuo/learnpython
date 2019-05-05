#!user/bin/python
#-*-coding:utf-8-*-
'''
编写人：王春雷
功能：类，类方法的第一个变量必须是self
可以动态的添加变量，这个类中根本就没有定义color变量，但是在初始化的时候可以直接生成
'''

class Teacher:
    def __init__(self, TId, TName, TSubject):
        self.TId = TId
        self.TName = TName
        self.TSubject = TSubject

    def giveScore(self, score):
        self.score = sclre

    def print(self):
        print('工号：%s, 姓名：%s, 教授课程：%s' %( self.TId,  self.TName, self.TSubject))

class Student:
    subject = []
    def __init__(self, SId, SName, SMajor,SClass):
        self.SId = SId;
        self.SName = SName
        self.SMajor = SMajor
        self.SClass = SClass

    def addSubject(self, sName):
        self.subject.append(sName)

    def deleteSubject(self, sName):
        self.subject.remove(sName)

    def playGame(self, name):
        self.GameName = name;

    def absent(self, subject):
        self.SAbsent = subject

    def print(self):
        print('学号：%s, 姓名：%s,专业：%s ,班级：%s' % (self.SId,  self.SName, self.SMajor, self.SClass))

    def getSubject(self):
        print('%s 学习的课程有：'% self.SName, end='')
        print(self.subject)

class Instructor(Teacher):
    dormitory = []
    def __init__(self, TId, TName, TSubject):
        super().__init__(TId, TName, TSubject)
        self.Identity = '导员'
    def chaqin(self, DNum):
        self.dormitory.append(selt.DNum)

    def print(self):
        print('身份：%s '% self.Identity, end="")
        super().print()

instructor = Instructor('007', '梁伟', 'JavaEE')
student = Student('2016021191', '王春雷', '软件工程', '161')
student.addSubject('JavaEE')
student.addSubject('Python')

instructor.print()
student.print()
student.getSubject()