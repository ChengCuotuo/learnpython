#!user/bin/python
#-*-coding:utf-8-*-
'''
编写人：王春雷
时间：2019.9.13
功能：字典
'''
#a_dict = {u'姓名：':u'王春雷',u'班级：':u'软件161',u'年龄：':23}
#print(a_dict)

keys=[u'姓名:',u'班级',u'年龄']
value=[u'王春雷',u'软件161',23]
#使用dict的zip函数可以将两个列表合并成字典
dictionary=dict(zip(keys,value))
print(dictionary)
#字典的items()方法，返回值是两两对应的组合
for item in dictionary.items():
    print(item)
#字典，在不加特殊说明的话，就直接输出它的键
for key in dictionary:
    print(key)

for key in dictionary:
    print(dictionary.get(key))