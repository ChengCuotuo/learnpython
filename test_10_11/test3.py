#!user/bin/python
#-*-coding:utf-8-*-
'''
编写人：王春雷
时间：2019.9.13
功能：接收任意多的参数
'''

def demo(*para):
    avg = sum(para) / len(para)
    g = [i  for i in para if i > avg]#返回列表
    return (avg,)+ tuple(g)#返回平均值和g的元组，其中的逗号不能省

print(demo(1, 2, 3, 4))