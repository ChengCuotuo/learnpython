#encouing:utf-8
'''
author:mo
date:20190415
功能：打飞机小游戏
'''

import pygame
from sys import exit
from pygame.locals import *

#玩家飞机类
class Player(pygame.sprite.Sprite):
    def __init__(self,plane_img, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = plane_img
        self.rect = pygame.Rect(0,0,100,120)#飞机大小
        self.rect.topleft = init_pos
        self.img_index = 0
        self.speed = 8 #飞机移动速度

        #子弹的集合，作为一组
        self.bullets = pygame.sprite.Group()#群主


    #向上运动
    def moveUp(self):

        if self.rect.top <= 0:
            #到上边界时
            self.rect.top = 0
        else :
            self.rect.top -= self.speed

    #向下运动
    def moveDown(self):

        if self.rect.top >= SCREEN_HEIGHT - self.rect.height:
            #到下边界时
            self.rect.top = SCREEN_HEIGHT - self.rect.height
        else :
            self.rect.top += self.speed

    # 向左运动
    def moveLeft(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        else:
            self.rect.left -= self.speed

    # 向右运动
    def moveRight(self):
        if self.rect.left >= SCREEN_WIDTH - self.rect.width:
            self.rect.left = SCREEN_WIDTH - self.rect.width
        else:
            self.rect.left += self.speed

    def shoot(self,bullet_img):
        bullet = Bullet(bullet_img,self.rect.midtop)
        self.bullets.add(bullet)


#敌机类
class Enemy(pygame.sprite.Sprite):
    def __init__(self,plane_img, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect()
        self.rect.midbottom = init_pos
        self.speed = 5
    def move(self):
        self.rect.top += self.speed

        


#设置飞机子弹类,子弹类
class Bullet(pygame.sprite.Sprite):
    def __init__(self,bullet_img,init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.midbottom = init_pos
        self.speed = 10

    #子弹上升
    def move(self):
        self.rect.top -= self.speed



#设置游戏屏幕大小
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 600

#初始化Pygame
pygame.init()

#设置游戏界面大小背景图片及标题
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#设置游戏界面标题
# pygame.display.set_mode("飞机大战")
pygame.display.set_caption('飞机大战')

#背景图
background = pygame.image.load('resplane/image/background.png')

#玩家飞机图片
player_img1 = pygame.image.load('resplane/image/player1.png')
player_img2 = pygame.image.load('resplane/image/player1.png')

#子弹图片
b_img = pygame.image.load("resplane/image/playerbullet.png")

#设置子弹大小
bullet_rect = pygame.Rect(0,0,20,25)
bullet_img = b_img.subsurface(bullet_rect)


player_img = []
player_img.append(player_img1.subsurface(pygame.Rect(0,0,100,120)).convert_alpha())
player_img.append(player_img2.subsurface(pygame.Rect(0,0,100,120)).convert_alpha())
player_pos = [200,500]#飞机初始位置

player = Player(player_img,player_pos)#实例化
shoot_frequency = 0
#游戏循环帧率设置
clock = pygame.time.Clock()

#游戏主循环
while True:
    #控制游戏最大帧率为30
    clock.tick(20)
    #绘制背景
    screen.fill(0)
    screen.blit(background, (0,0))#绘制方法

    #绘制玩家飞机
    screen.blit(player.image[player.img_index],player.rect)
    player.img_index = shoot_frequency//8
    shoot_frequency += 1
    if shoot_frequency >= 15:
        shoot_frequency = 0

    #生成子弹
    #if shoot_frequency%15 == 0:#循环15次生成子弹
        #player.shoot(bullet_img)

    # shoot_frequency += 1
    # if shoot_frequency >= 15:
    #     shoot_frequency = 0

    #对每个子弹进行处理
    for bulllet in player.bullets:
        bulllet.move()

        #溢出屏幕的子弹统统删除掉
        if bulllet.rect.bottom < 0 :
            player.bullets.remove(bulllet)

    #显示子弹
    player.bullets.draw(screen)
    pygame.display.update()


    #更新屏幕
    pygame.display.update()

    #获取键盘点击事件
    key_pressed = pygame.key.get_pressed()
    #向上
    if key_pressed[K_UP]:
        player.moveUp()
    #向下
    if key_pressed[K_DOWN]:
        player.moveDown()

    #向左
    if key_pressed[K_LEFT]:
        player.moveLeft()

    #向右
    if key_pressed[K_RIGHT]:
        player.moveRight()

    if key_pressed[K_SPACE]:
        player.shoot(bullet_img)

    
    #处理游戏退出，
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()













