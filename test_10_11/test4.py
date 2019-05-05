#!user/bin/python
#-*-coding:utf-8-*-
'''
编写人：王春雷
时间：2019.9.13
功能：接收任意多的参数
'''
def upperAndLower(str):
    num = [0, 0]
    for ch in str:
        if ch.islower():
            num[0] += 1
        elif ch >= 'A' and ch <='Z':
            num[1] += 1
    return num

print(tuple(upperAndLower('aaaabbbbccccAAAA')))

