 # -*- coding: utf-8 -*-
'''
author:wudi
date:20180101
func:planegame
0.游戏背景框架1.出现玩家飞机2.玩家自由移动3.出现NPC4.玩家接到NPC会消失5.计分6.出现不同的NPC角色
'''
import pygame
from sys import exit
from pygame.locals import *
import random

# 玩家飞机类
class Playgamer(pygame.sprite.Sprite):
    def __init__(self, plane_img,init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = plane_img                                # 用来存储玩家图片
        self.rect = pygame.Rect(0, 0, 100, 120) 
        self.rect.topleft = init_pos
        self.speed = 8                                  # 初始化玩家速度，这里是一个确定的值
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
            
#NPC类，初始化，第一个参数是NPC图片，第二个是NPC被接住摧毁动画图片，第三个是NPC的位置
class Candy(pygame.sprite.Sprite):
    def __init__(self, candy_img, init_pos):
       pygame.sprite.Sprite.__init__(self)
       self.image = candy_img
       self.rect = self.image.get_rect()
       self.rect.topleft = init_pos
       self.speed = random.randint(1,5)
    # NPC移动，边界判断及删除在游戏主循环里处理
    def move(self):
        self.rect.top += self.speed
        
# 分数类
class Score():
    def __init__(self):
        self.score=0
        self.score_font = pygame.font.Font(None, 36)#字体，字号        
    # 加分
    def AddScore(self,es):
        self.score=self.score+es
    #返回分数
    def ShowScore(self):
        self.score_text=self.score_font.render(str(self.score), True, (255, 0, 0))#字体颜色
        return self.score_text
    
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
#NPC图片列表
e_img1=pygame.image.load('resplane/image/batman1.png')
e_img2=pygame.image.load('resplane/image/cap1.png')
e_img3=pygame.image.load('resplane/image/sman1.png')
eimgs=[]
eimgs.append(e_img1)
eimgs.append(e_img2)
eimgs.append(e_img3)
enemy_rect = pygame.Rect(0, 0, 30, 30)
#存储NPC，管理多个对象，因为是多个NPC
enemies1 = pygame.sprite.Group()
# 初始化NPC移动频率
enemy_frequency = 0
#实例化玩家
player = Playgamer(player_img, player_pos)
# 实例化分数
gamescore=Score()
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
    # 生成NPC，需要控制生成频率
    if enemy_frequency % 50 == 0:
        enemy1_pos = [random.randint(0, SCREEN_WIDTH - enemy_rect.width), 0]
        enemy1 = Candy(eimgs[random.randint(0,2)], enemy1_pos)#实例化NPC
        enemies1.add(enemy1)
    enemy_frequency += 1
    if enemy_frequency >= 100:
        enemy_frequency = 0
    #对生成的每个NPC做处理
    for enemy in enemies1:
        #移动NPC
        enemy.move()       
        #移动出屏幕后删除NPC    
        if enemy.rect.top < 0:
            enemies1.remove(enemy) 
    # NPC被玩家效果处理
    # 将被接住的NPC对象添加到击毁Group 中，用来渲染击毁动画
    if pygame.sprite.spritecollide(player,enemies1,True):
        gamescore.AddScore(100)#接住NPC加分100
    # 在屏幕上绘制得分
    screen.blit(gamescore.ShowScore(), [10,10])
    # 显示NPC
    enemies1.draw(screen)
    # 更新屏幕
    pygame.display.update()
    # 获取键盘事件（上下左右按键）
    key_pressed = pygame.key.get_pressed()
    # 处理键盘事件（移动飞机的位置）
    if key_pressed[K_a] or key_pressed[K_LEFT]:
        player.moveLeft()
    if key_pressed[K_d] or key_pressed[K_RIGHT]:
        player.moveRight()
    # 处理游戏退出事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()#如果是退出的话，先退出pygame模块，再退出游戏
            exit()
