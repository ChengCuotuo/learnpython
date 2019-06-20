 # -*- coding: utf-8 -*-
'''
author:wudi
date:20180325
func:planegame
0.游戏背景框架1.出现玩家飞机2.玩家飞机自由移动
'''
import pygame
from sys import exit
from pygame.locals import *

# 玩家飞机类
class Player(pygame.sprite.Sprite):
    def __init__(self, plane_img,init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = plane_img                                # 用来存储玩家飞机图片的列表
        self.rect = pygame.Rect(0, 0, 100, 120) 
        self.rect.topleft = init_pos
        self.img_index = 0                              # 玩家飞机图片索引
        self.speed = 8                                  # 初始化玩家飞机速度，这里是一个确定的值
    # 向上移动，需要判断边界
    def moveUp(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        else:
            self.rect.top -= self.speed
    # 向下移动，需要判断边界
    def moveDown(self):
        if self.rect.top >= SCREEN_HEIGHT - self.rect.height:
            self.rect.top = SCREEN_HEIGHT - self.rect.height
        else:
            self.rect.top += self.speed
    # 向左移动，需要判断边界
    def moveLeft(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        else:
            self.rect.left -= self.speed
    # 向右移动，需要判断边界        
    def moveRight(self):
        if self.rect.left >= SCREEN_WIDTH - self.rect.width:
            self.rect.left = SCREEN_WIDTH - self.rect.width
        else:
            self.rect.left += self.speed
            
# 设置游戏屏幕大小
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 700
# 初始化 pygame，必须放在最前面
pygame.init()
# 设置游戏界面大小、背景图片及标题
# 游戏界面像素大小
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# 游戏界面标题
pygame.display.set_caption('飞机大战')
# 背景图
background = pygame.image.load('D:/testpy/resplane/image/background.png').convert()
# 飞机图片集合
# 设置玩家飞机不同状态的图片列表，多张图片展示为动画效果
player_img1=pygame.image.load('D:/testpy/resplane/image/player1.png')
player_img2=pygame.image.load('D:/testpy/resplane/image/player2.png')
plane_img =[]
plane_img.append(player_img1.subsurface(pygame.Rect(0, 0, 102, 121)).convert_alpha())
plane_img.append(player_img2.subsurface(pygame.Rect(0, 0, 102, 121)).convert_alpha())
player_pos = [200, 500]
#实例化玩家飞机
player = Player(plane_img, player_pos)
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
    # 绘制玩家飞机
    screen.blit(player.image[player.img_index], player.rect)
    # 更新屏幕
    pygame.display.update()
    # 获取键盘事件（上下左右按键）
    key_pressed = pygame.key.get_pressed()
    # 处理键盘事件（移动飞机的位置）
    if key_pressed[K_w] or key_pressed[K_UP]:
        player.moveUp()
    if key_pressed[K_s] or key_pressed[K_DOWN]:
        player.moveDown()
    if key_pressed[K_a] or key_pressed[K_LEFT]:
        player.moveLeft()
    if key_pressed[K_d] or key_pressed[K_RIGHT]:
        player.moveRight()
    # 处理游戏退出事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()#如果是退出的话，先退出pygame模块，再退出游戏
            exit()
