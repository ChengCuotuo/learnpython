'''
author:wudi
date:20180114
func:1游戏背景2出现玩家角色3吃苹果4加入血条5加入僵尸6僵尸随意运动
'''
import itertools, sys, time, random, math, pygame
from pygame.locals import *

def print_text(font, x, y, text, color=(255,255,255)):
    imgText = font.render(text, True, color)
    screen = pygame.display.get_surface() 
    screen.blit(imgText, (x,y))
def reverse_direction(sprite):
    if sprite.direction == 0:
        sprite.direction = 4
    elif sprite.direction == 2:
        sprite.direction = 6
    elif sprite.direction == 4:
        sprite.direction = 0
    elif sprite.direction == 6:
        sprite.direction = 2

#计算速度和方向函数
def calc_velocity(direction, vel=2.0):
    velocity = Point(0,0)
    if direction == 0: #上
        velocity.y = -vel
    elif direction == 2: #右
        velocity.x = vel
    elif direction == 4: #下
        velocity.y = vel
    elif direction == 6: #左
        velocity.x = -vel
    return velocity

#农夫的位置类
class Point(object):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    #X property
    def getx(self): return self.__x
    def setx(self, x): self.__x = x
    x = property(getx, setx)
    #Y property
    def gety(self): return self.__y
    def sety(self, y): self.__y = y
    y = property(gety, sety)
    def __str__(self):
        return "{X:" + "{:.0f}".format(self.__x) + ",Y:" + "{:.0f}".format(self.__y) + "}"
    
#玩家角色类
class MySprite(pygame.sprite.Sprite):    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #extend the base Sprite class
        self.master_image = None
        self.frame = 0
        self.old_frame = -1
        self.frame_width = 1
        self.frame_height = 1
        self.first_frame = 0
        self.last_frame = 0
        self.columns = 1
        self.last_time = 0
        self.direction = 0
        self.velocity = Point(0.0,0.0) 
    #X property
    def _getx(self): return self.rect.x
    def _setx(self,value): self.rect.x = value
    X = property(_getx,_setx)
    #Y property
    def _gety(self): return self.rect.y
    def _sety(self,value): self.rect.y = value
    Y = property(_gety,_sety)
    #位置属性
    def _getpos(self): return self.rect.topleft
    def _setpos(self,pos): self.rect.topleft = pos
    position = property(_getpos,_setpos)
    #载入农夫行走全图
    def load(self, filename, width, height, columns):
        self.master_image = pygame.image.load(filename).convert_alpha()
        self.frame_width = width
        self.frame_height = height
        self.rect = Rect(0,0,width,height)
        self.columns = columns
        rect = self.master_image.get_rect()
        self.last_frame = (rect.width // width) * (rect.height // height) - 1
    def update(self, current_time, rate=30):
        #更新帧
        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = self.first_frame
            self.last_time = current_time
        #帧的位置
        if self.frame != self.old_frame:
            frame_x = (self.frame % self.columns) * self.frame_width
            frame_y = (self.frame // self.columns) * self.frame_height
            rect = Rect(frame_x, frame_y, self.frame_width, self.frame_height)
            self.image = self.master_image.subsurface(rect)
            self.old_frame = self.frame
    def __str__(self):
        return str(self.frame) + "," + str(self.first_frame) + "," + str(self.last_frame) + "," + str(self.frame_width) + \
               "," + str(self.frame_height) + "," + str(self.columns) + "," + str(self.rect)
    
#游戏开始，对游戏背景进行设置
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("吃苹果")
font = pygame.font.Font(None, 36)
timer = pygame.time.Clock()
#创建精灵组
player_group = pygame.sprite.Group()
food_group = pygame.sprite.Group()
zombie_group = pygame.sprite.Group()
#初始化玩家精灵组
player = MySprite()
player.load("farmer walk.png", 96, 96, 8)
player.position = 80, 80
player.direction = 4
player_group.add(player)
#初始化food精灵组
for n in range(1,21):
    food = MySprite()
    food.load("food_low.png", 35, 35, 1)
    food.position = random.randint(0,680),random.randint(0,480)
    food_group.add(food)
#初始化僵尸精灵组
zombie_image = pygame.image.load("zombie walk.png").convert_alpha()
for n in range(0, 10):
    zombie = MySprite()
    zombie.load("zombie walk.png", 96, 96, 8)
    zombie.position = random.randint(0,700), random.randint(0,500)
    zombie.direction = random.randint(0,3) * 2
    zombie_group.add(zombie)
#参数设置
player_moving = False
game_over = False
player_health = 0
#游戏开始运行
while True:
    timer.tick(30)
    ticks = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    #键盘点击事件
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]: sys.exit()
    elif keys[K_UP] or keys[K_w]:
        player.direction = 0
        player_moving = True
    elif keys[K_RIGHT] or keys[K_d]:
        player.direction = 2
        player_moving = True
    elif keys[K_DOWN] or keys[K_s]:
        player.direction = 4
        player_moving = True
    elif keys[K_LEFT] or keys[K_a]:
        player.direction = 6
        player_moving = True
    else:
        player_moving = False
    if not game_over:
        #根据角色的不同方向，使用不同的动画帧
        player.first_frame = player.direction * player.columns#定位到该行的第一个位置
        player.last_frame = player.first_frame + player.columns-1#定位到该行的最后一个位置
        if player.frame < player.first_frame:
            player.frame = player.first_frame
        if not player_moving:
            #当停止按键（即人物停止移动的时候），停止更新动画帧
            player.frame = player.first_frame = player.last_frame
        else: 
            player.velocity = calc_velocity(player.direction, 3)
            player.velocity.x *=3
            player.velocity.y *= 3
        #更新玩家精灵组
        player_group.update(ticks, 50)
        #移动玩家，碰壁后停止
        if player_moving:
            player.X += player.velocity.x
            player.Y += player.velocity.y
            if player.X < 0: player.X = 0
            elif player.X > 700: player.X = 700
            if player.Y < 0: player.Y = 0
            elif player.Y > 500: player.Y = 500
        #检测玩家是否与食物冲突，是否吃到果实
        attacker = None
        attacker = pygame.sprite.spritecollideany(player, food_group)
        if attacker != None:
            if pygame.sprite.collide_circle_ratio(0.65)(player,attacker):
                player_health +=1
                food_group.remove(attacker)
        #更新食物精灵组
        food_group.update(ticks, 50)
        if len(food_group) == 0:
            game_over = True
        #更新僵尸精灵组
        zombie_group.update(ticks, 50)
        #处理每个僵尸
        for z in zombie_group:
            z.first_frame = z.direction * z.columns
            z.last_frame = z.first_frame + z.columns-1
            if z.frame < z.first_frame:
                z.frame = z.first_frame
            z.velocity = calc_velocity(z.direction)   
            z.X += z.velocity.x
            z.Y += z.velocity.y
            if z.X < 0 or z.X > 700 or z.Y < 0 or z.Y > 500:
                reverse_direction(z)
            elif random.randint(1,100)<5:
                    temp=[0,2,4,6]
                    z.direction=temp[random.randint(0,3)]
    #清屏
    screen.fill((50,50,100))
    #绘制精灵
    player_group.draw(screen)
    food_group.draw(screen)
    zombie_group.draw(screen)
    #绘制玩家血量条
    pygame.draw.rect(screen, (50,150,50,180), Rect(300,570,player_health*5,25))
    pygame.draw.rect(screen, (100,200,100,180), Rect(300,570,100,25), 2)
    if game_over:
        print_text(font, 300, 100, "G A M E   O V E R")    
    pygame.display.update()
