#!user/bin/python
#-*-coding:utf-8-*-
'''
编写人：王春雷
时间：2019.9.13
功能：列表过滤
'''

def justOne(list_a):
   new_list = []
   list1=list_a
   for item in list1:
       if item not in new_list:
           new_list.append(item)

   return new_list


list_a = ['aa','bb','cc','ss', 'dd', 'ff','aa','aa', 'bb', 'c']

list_b = list(justOne(list_a))
print(list_b)

list_b = list(set(list_a))
print(list_b)