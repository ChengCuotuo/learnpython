#!user/bin/python
#-*-coding:utf-8-*-
'''
编写人：王春雷
时间：2019.9.13
功能：元组操作
'''
#元组tuple，创建之后就不能被修改
#元组是放在（）中的
#元组和列表的打印形式是不一样的
#将数组字符串变成了元组
a_str = 'abcdefg'
a_tuple=tuple(a_str)
print(a_tuple)
print(tuple('abcdefg'))
#将元元组转变成列表
a=list('abcdefg')
print(a)
b_list=[-1,-4,6,7.5,-2.3,9,-11]
print(b_list)
