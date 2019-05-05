#!user/bin/python
#-*-coding:utf-8-*-
'''
编写人：王春雷
时间：2019.9.13
功能：电脑猜数字游戏
'''

import random;

while True:
    max = int(input('输入让计算机猜的数字的上限：'));
    num = int(input('输入要猜的数字：'))
    count = int(0)
    guess_max = max
    guess_min = int(1)
    while True:
        if num >= 0 and num <= max:
            guess = (guess_max + guess_min) // 2
            if guess > num:
                print('%d猜大了' %guess)
                guess_max = guess;
            elif guess < num:
                print('%d猜小了' %guess)
                guess_min = guess;
            else:
                print('恭喜猜对了，一共猜了 %d 次' %count)
                break;
        count = count + 1

