#!user/bin/python
#-*-coding:utf-8-*-
'''
编写人：王春雷
时间：2019.9.13
功能：练习题
'''
cast=['cleese','palin', 'joines','idle']
print(cast)
print(len(cast))
print(cast[1])
cast.append('gilliam')
print(cast)
cast.pop()
print(cast)
cast.remove('cleese')
print(cast)
cast.insert(0,'cleese')
print(cast)

list=list('abcdbcbcebedbbdef')
print(list.count('b'))
list.extend('mm')#是将参数看作是一个列表添加到末尾
print(list)
list.append('mm')#是将参数看作是一个元素添加到末尾
print(list)
list.insert(0,'dd')#插入的也是一个元素
print(list)
list.reverse()#逆置
print(list)
list.sort()
print(list)
