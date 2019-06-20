# -*- coding: utf-8 -*-
'''
author:wudi
date:20180425
func:planegame
0.游戏背景框架
1.出现玩家飞机，只是载入图片，不会动
2.玩家飞机自由移动，用事件监测键盘左右上下键
3.出现子弹，载入图片，不断向上移动
4.出现敌机，载入图片，不断向下移动
5.子弹碰到敌机会爆炸，碰撞检测
6.计算击毁敌机得分，分数出现在左上角
'''
import pygame
from sys import exit
from pygame.locals import *
import random

# 玩家飞机类
class Player(pygame.sprite.Sprite):
    def __init__(self, plane_img,init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = plane_img                          # 用来存储玩家飞机图片的列表
        self.rect = pygame.Rect(0, 0, 100, 120) 
        self.rect.topleft = init_pos
        self.img_index = 0                              # 玩家飞机图片索引
        self.speed = 8                                  # 初始化玩家飞机速度，这里是一个确定的值
        self.bullets = pygame.sprite.Group()            # 玩家飞机所发射的子弹的集合，作为一组处理
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
    # 发射子弹，生成子弹实例，然后编为一组
    def shoot(self, bullet_img):
        bullet = Bullet(bullet_img, self.rect.midtop)
        self.bullets.add(bullet)
            
# 子弹类
class Bullet(pygame.sprite.Sprite):
    def __init__(self, bullet_img, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.midbottom = init_pos#子弹的位置
        self.speed = 10#子弹的速度
    def move(self):
        self.rect.top -= self.speed

# 敌机类，跟子弹类有些类似
class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_img, enemy_down_imgs, init_pos):
       pygame.sprite.Sprite.__init__(self)
       self.image = enemy_img
       self.rect = self.image.get_rect()
       self.rect.topleft = init_pos
       self.down_imgs = enemy_down_imgs
       self.speed = 2
       self.down_index = 0
    # 敌机移动，边界判断及删除在游戏主循环里处理
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
        
# 主程序开始了        
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
# 子弹图片
b_img=pygame.image.load('D:/testpy/resplane/image/playerbullet.png')
bullet_rect = pygame.Rect(0, 0, 20, 25)
bullet_img = b_img.subsurface(bullet_rect)
# 敌机不同状态的图片列表，多张图片展示为动画效果
e_img1=pygame.image.load('D:/testpy/resplane/image/eplane1.png')
e_img2=pygame.image.load('D:/testpy/resplane/image/eplane2.png')
e_img3=pygame.image.load('D:/testpy/resplane/image/eplane3.png')
e_img4=pygame.image.load('D:/testpy/resplane/image/eplane4.png')
enemy_rect = pygame.Rect(0, 0, 50, 34)
enemy1_img = e_img1.subsurface(enemy_rect)
enemy_down_imgs = []#这是敌机爆炸效果动画
enemy_down_imgs.append(e_img1.subsurface(enemy_rect))
enemy_down_imgs.append(e_img2.subsurface(enemy_rect))
enemy_down_imgs.append(e_img3.subsurface(enemy_rect))
enemy_down_imgs.append(e_img4.subsurface(enemy_rect))
#存储敌机，管理多个对象，因为是多个敌机
enemies1 = pygame.sprite.Group()
# 存储被击毁的敌机，用来渲染击毁动画
enemies_down = pygame.sprite.Group()
# 初始化射击及敌机移动频率
shoot_frequency = 0
enemy_frequency = 0
# 实例化玩家飞机
player = Player(plane_img, player_pos)
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
    # 绘制玩家飞机
    screen.blit(player.image[player.img_index], player.rect)
    # 更换图片索引使飞机有动画效果
    player.img_index = shoot_frequency // 8 
    # 生成子弹，每循环15次，生成一个子弹
    if shoot_frequency % 15 == 0:
        player.shoot(bullet_img)
    shoot_frequency += 1
    if shoot_frequency >= 15:
        shoot_frequency = 0
    # 对每个子弹做处理
    for bullet in player.bullets:
        # 以固定速度移动子弹
        bullet.move()
        # 移动出屏幕后删除子弹
        if bullet.rect.bottom < 0:
            player.bullets.remove(bullet)   
    # 显示子弹
    player.bullets.draw(screen)   
    # 生成敌机，需要控制生成频率
    if enemy_frequency % 50 == 0:
        enemy1_pos = [random.randint(0, SCREEN_WIDTH - enemy_rect.width), 0]
        enemy1 = Enemy(enemy1_img, enemy_down_imgs, enemy1_pos)
        enemies1.add(enemy1)
    enemy_frequency += 1
    if enemy_frequency >= 100:
        enemy_frequency = 0
    #对生成的每个敌机做处理
    for enemy in enemies1:
        #移动敌机
        enemy.move()       
        #移动出屏幕后删除飞机    
        if enemy.rect.top < 0:
            enemies1.remove(enemy) 
    # 敌机被子弹击中效果处理
    # 将被击中的敌机对象添加到击毁敌机 Group 中，用来渲染击毁动画
    enemies1_down = pygame.sprite.groupcollide(enemies1, player.bullets, 1, 1)#检查两组精灵是否碰撞
    for enemy_down in enemies1_down:
        enemies_down.add(enemy_down)
    # 敌机被子弹击中效果显示
    for enemy_down in enemies_down:
        if enemy_down.down_index > 7:
            enemies_down.remove(enemy_down)
            gamescore.AddScore(100)#击中敌机加分100
            continue
        screen.blit(enemy_down.down_imgs[enemy_down.down_index // 4], enemy_down.rect)
        enemy_down.down_index += 1
    # 显示敌机
    enemies1.draw(screen)
    # 在屏幕上绘制得分
    screen.blit(gamescore.ShowScore(), [10,10])
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
