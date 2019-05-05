#!user/bin/python
#-*-coding:utf-8-*-
'''
编写人：王春雷
时间：2019.9.13
功能：猜数字游戏
'''

import random;
while True:
    a = int(random.randint(0, 100))
    count = int(0);
    while True:
        b = int(input('请输入你猜的数字：'))
        if a < b:
            print('你猜的数字大了')
        elif a > b:
            print('你猜的数字小了')
        else :
            print('恭喜你，猜对了,一共猜了 %d 次'% (count))
            break;
        count = count + 1
    judge = int(input('是否继续(0否，1是)'))
    if judge == 0:
        print('谢谢参与')
        break;