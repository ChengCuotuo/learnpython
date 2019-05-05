#!user/bin/python
#-*-coding:utf-8-*-
'''
编写人：王春雷
时间：2019.9.13
功能：猜拳游戏
'''
import random;

print('游戏开始，请输入：')
while  True:
    a = int(input(u'输入石头（0）， 剪刀（1）， 布（2）:'));
    if a != 0 and a != 1 and a != 2:
        print('非法输入，请重新输入:')
    else :
        b = random.randint(0, 3);
        if a == b:
            print('平局，电脑输出：%d' %b);
        elif((a == 0 and b == 1) or (a == 1 and b == 2) or (a == 2 and b == 0)):
            print('你赢了，电脑输出：%d' %b)
        else:
            print('你输了，电脑输出：%d' %b)

    con = int(input('是否继续，0否，1是：'))
    if con == 0:
        print('拜拜')
        break;
