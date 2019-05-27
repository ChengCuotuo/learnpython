# -*- coding: utf-8 -*-
'''
author:wudi
date:20181231
func:0.游戏背景框架1.出现玩家角色
'''
import pygame
from sys import exit
from pygame.locals import *

# 玩家类
class Playgamer(pygame.sprite.Sprite):
    def __init__(self, plane_img,init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = plane_img                                
        self.rect = pygame.Rect(0, 0, 190, 200) 
        self.rect.topleft = init_pos
        
# 设置游戏屏幕大小
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 700
# 初始化 pygame，必须放在最前面
pygame.init()
# 设置游戏界面大小、背景图片及标题
# 游戏界面像素大小
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# 游戏界面标题
pygame.display.set_caption('接花游戏')
# 背景图
background = pygame.image.load('resplane/image/bg4.jpg').convert()
# 设置玩家图片
player_img=pygame.image.load('resplane/image/spiderman1.png')
player_pos = [200, 500]
#实例化玩家飞机
player = Playgamer(player_img, player_pos)
# 游戏循环帧率设置
clock = pygame.time.Clock()
# 判断游戏循环退出的参数
running = True
# 游戏主循环
while running:
    # 控制游戏最大帧率为 60
    clock.tick(60)
    # 绘制背景
    screen.fill(0)
    screen.blit(background, (0, 0))
    # 绘制玩家
    screen.blit(player.image, player.rect)
    # 更新屏幕
    pygame.display.update()
    # 处理游戏退出事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()#如果是退出的话，先退出pygame模块，再退出游戏
            exit()
