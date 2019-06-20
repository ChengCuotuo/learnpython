#-*-coding:utf-8-*-
'''
author:wudi
date:20180325
func:planegame
0.游戏背景
'''
import pygame
from sys import exit
from pygame.locals import *

# 设置游戏屏幕大小
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 600
# 初始化 pygame，使用pygame时首先加上这一句才可以用
pygame.init()
# 设置游戏界面大小、背景图片及标题
# 游戏界面像素大小
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# 游戏界面标题
pygame.display.set_caption('飞机大战')
# 背景图
background = pygame.image.load('D:/testpy/resplane/image/background.png')
# 游戏循环帧率设置
clock = pygame.time.Clock()
# 判断游戏循环退出的参数
running = True
# 游戏主循环
while running:
    # 控制游戏最大帧率为 30
    clock.tick(30)
    # 绘制背景
    screen.fill(0)
    screen.blit(background, (0, 0))#绘图方法
    # 更新屏幕
    pygame.display.update()
    # 处理游戏退出，不能删除，不然移动窗体就会死机
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
