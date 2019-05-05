'''
author:春雷
date:20190415
1.游戏背景
2.添加玩家的飞机
3.自由移动
4.发射子弹
'''

import  pygame
from sys import exit
from pygame.locals import *
import random

#游戏的玩家飞机类
class Player(pygame.sprite.Sprite):
    def __init__(self, plane_img, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = plane_img
        #rect 属性表示
        self.rect=pygame.Rect(0, 0, 100, 120)
        #左上角位置
        self.rect.topleft=init_pos
        #图片的坐标
        self.img_index=0
        #移动的速度
        self.speed = 8
	#子弹集合
        self.bullets = pygame.sprite.Group()
		
    #移动的操作函数
    #向上运动
    def moveUp(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        else:
            self.rect.top -= self.speed

    # 向下运动
    def moveDown(self):
        if self.rect.top >= SCREEN_HEIGHT - self.rect.height:
            self.rect.top = SCREEN_HEIGHT - self.rect.height
        else:
            self.rect.top += self.speed
    #向左运动
    def moveLeft(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        else :
            self.rect.left -= self.speed
    #向右运动
    def moveRight(self):
        if self.rect.left >= SCREEN_WIDTH - self.rect.width:
            self.rect.left = SCREEN_WIDTH - self.rect.width
        else:
            self.rect.left += self.speed
    #子弹移动
    def shoot (self, bullet_img):
        bullet = Bullet(bullet_img, self.rect.midtop)
        self.bullets.add(bullet)

#敌机类
class Enemy(pygame.sprite.Sprite):
    def __init__(self,plane_img, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = plane_img
        self.rect=pygame.Rect(0, 0, 100, 120)
        self.rect.topleft=init_pos
        self.speed = 8
    def move(self):
        self.rect.top += self.speed            

#子弹类
#初始位置和飞机的位置是相同的
class Bullet(pygame.sprite.Sprite):
    #初始化类，子弹的图片，子弹的位置
    def __init__ (self, bullet_img, init_pos):
	#初始化精灵
        pygame.sprite.Sprite.__init__(self)
        #图片
        self.image = bullet_img
        #大小
        self.rect = self.image.get_rect()
        #初始位置，矩形框的中间的底部，正好是飞机的头部中间位置
        self.rect.midbottom = init_pos
        #子弹的速度
        self.speed = 10
	#子弹的移动
    def move (self):
        self.rect.top -= self.speed
		
		

#设置游戏屏幕的大小
SCREEN_WIDTH=480
SCREEN_HEIGHT=600
#初始化 pygame
pygame.init()
#设置游戏页面的大小和背景图片及标题
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT));
#游戏界面标题
pygame.display.set_caption('飞机大战');
#背景图
background = pygame.image.load("resplane/image/background.png");
#玩家飞机图片
player_img1 = pygame.image.load("resplane/image/player1.png")
player_img2 = pygame.image.load("resplane/image/player2.png");

#存放图片的列表
plane_img=[]
#将图片设置大小之后再添加
plane_img.append(player_img1.subsurface(pygame.Rect(0, 0, 100, 120)).convert_alpha())
plane_img.append(player_img2.subsurface(pygame.Rect(0, 0, 100, 120)).convert_alpha())

#载入子弹对象
b_img = pygame.image.load("resplane/image/playerbullet.png")
#设置子弹的初始大小
bullet_rect = pygame.Rect(0, 0, 20, 25)
#将子弹的图片进行切割
bullet_img = b_img.subsurface(bullet_rect)

#载入敌机的图片
e_img = pygame.image.load("resplane/image/eplane1.png")
#设置敌机图片的大小
enemy_rect = pygame.Rect(0, 0, 50, 34)
enemy1_img = e_img.subsurface(enemy_rect)
enemies1 = pygame.sprite.Group()
#敌机出现的频率
enemy_frequency = 0

#飞机的初始位置
player_pos=[150, 450]
#实例化玩家
player=Player(plane_img, player_pos)
#让飞机动起来
shoot_frequency = 0
#游戏循环帧数设置
clock = pygame.time.Clock();
#判断游戏循环退出的参数
running = True
#游戏的主循环
while running:
    #控制游戏最大帧率为20
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

    #对每个子弹进行处理
    for bulllet in player.bullets:
        bulllet.move()

        #溢出屏幕的子弹统统删除掉
        if bulllet.rect.bottom < 0 :
            player.bullets.remove(bulllet)

    #显示子弹
    player.bullets.draw(screen)

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

    #空格键发射子弹
    if key_pressed[K_SPACE]:
        player.shoot(bullet_img)
    
    #生成敌机
    if enemy_frequency % 20 == 0:
        enemy1_pos=[random.randint(0,SCREEN_WIDTH-enemy_rect.width),0]
        enemy1=Enemy(enemy1_img,enemy1_pos)
        enemies1.add(enemy1)

    enemy_frequency += 1

    if enemy_frequency >= 100:
        enemy_frequency=0

    #分别处理每个敌机
    for enemy in enemies1:
        enemy.move()
        if enemy.rect.top<0:
            enemies1.remove(enemy)

    #显示敌机
    enemies1.draw(screen)

    #更新屏幕
    pygame.display.update()

    #处理游戏退出，
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()