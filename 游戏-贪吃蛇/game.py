# -*- coding: utf-8 -*-
'''
data：
    start : 20190612 17:20
    end : 20190612 21:20
author：nianzuochen
function: 经典的贪吃蛇
0.生成游戏的窗体
1.初始化，出现一个长度为 2 的蓝色的蛇
2.蛇可以上下左右移动
3.碰撞检测，当到达窗体边缘或和身体重合，游戏结束
4.蛇身自动移动可以玩家可以改变它的方向
5.生成随机点
6.蛇吃到随机点身体增加
'''

import pygame
from sys import exit
from pygame.locals import *
import random

# t贪吃蛇类
#贪吃蛇的身体有很多个
class Player(pygame.sprite.Sprite):
    def __init__(self, snak_img):
        pygame.sprite.Sprite.__init__(self)
        #贪吃蛇的身体图片
        self.image = snak_img
        #存储身体位置
        self.pos = [[40, 10], [20, 10]]
        #记录身体长度
        self.len = 2
        #记录当前的移动方向 0 右 1 下 2 左 3 上
        self.direction = 0
        #游戏是否结束，碰壁或者接触自身都为结束, 0 活着  1 结束
        self.live = 0

    # 吃到随机点的处理
    def eatRandomPoint(self, newPos, randomPoint):
        # 当随机点位置和蛇头的位置重合
        # 添加一个新的蛇身，将随机点坐标添加到坐标首位置
        # 重新设置随机点的位置
        # 不会使用 pygame.sprite.collide_circle(randomPoint, self)
        # 直接采取位置坐标的计算，获取随机点的中心坐标，如果在蛇头的范围内就吃掉它
        x = randomPoint.pos[0] + 10;
        y = randomPoint.pos[1] + 10
        if ((x >= newPos[0] and x <= newPos[0] + 20) and (y >= newPos[1] and y <= newPos[1] + 20)):
            # 添加这个新节点
            player_img = pygame.image.load('img/snake.png')
            self.image.append(player_img.subsurface(pygame.Rect(0, 0, 20, 20)).convert_alpha())
            self.pos.insert(0, newPos)
            player.len += 1
            widthRange = SCREEN_WIDTH // 20 - 1
            heightRange = SCREEN_HEIGHT // 20 - 1
            position = [random.randint(1, widthRange) * 20, random.randint(1, heightRange) * 20 + 10]
            randomPoint.pos = position
            return False
        #print(str(newPos[0]) + " " + str(newPos[1]) + " " + str(x) + " " + str(y))
        return True


    #上下左右移动还需要烤考虑到当前的移动方法，比如，当前想上移动，move_down就无效
    #向上移动，修改坐标 pos 中的内容，就是删除最后一个，在队首添加一个节点，坐标是当前第一个的纵坐标加 20
    #新增参数 randomPoint 处理随机点
    def move_up(self, randomPoint):
        #将判断移动方向是否合法，以及修改方向的内容放置在新的方法中
        first = self.pos[0]
        newPos = [first[0], first[1] - 20]
        if (self.eatRandomPoint(newPos, randomPoint) == True):
            # 碰撞自身
            for pos in self.pos:
                if (pos == newPos):
                    self.live = 1
                    break
            # 碰壁
            if (newPos[1] < 0):
                self.live = 1
            self.pos.insert(0, newPos)
            self.pos.pop()

    #仅仅修改方向为向上
    def up(self):
        if (self.direction != 1):
            # 移动后方向已经改变
            self.direction = 3

    #向下移动，修改坐标 pos 中的内容，就是删除最后一个，在队首添加一个节点，坐标是当前第一个的纵坐标减去 20
    def move_down(self, randomPoint):
        first = self.pos[0]
        newPos = [first[0], first[1] + 20]
        #判断下一个点是否和随机点重合，重合自动添加
        # 当返回为false  表示没有迟到随机点，所以将当前的点加到队首
        if (self.eatRandomPoint(newPos, randomPoint) == True):
            # 碰撞自身
            for pos in self.pos:
                if (pos == newPos):
                    self.live = 1
                    break
            # 碰壁
            if (newPos[1] > SCREEN_HEIGHT):
                self.live = 1
            self.pos.insert(0, newPos)
            self.pos.pop()

    # 仅仅修改方向为向下
    def down(self):
        if (self.direction != 3):
            # 移动后方向已经改变
            self.direction = 1

    # 向右移动，修改坐标 pos 中的内容，就是删除最后一个，在队首添加一个节点，坐标是当前第一个的横坐标加 20
    def move_right(self, randomPoint):
        first = self.pos[0]
        newPos = [first[0] + 20, first[1]]
        if (self.eatRandomPoint(newPos, randomPoint) == True):
            # 碰撞自身
            for pos in self.pos:
                if (pos == newPos):
                    self.live = 1
                    break
            # 碰壁
            if (newPos[0] > SCREEN_WIDTH):
                self.live = 1
            self.pos.insert(0, newPos)
            self.pos.pop()

    # 仅仅修改方向为向右
    def right(self):
        if (self.direction != 2):
            # 移动后方向已经改变
            self.direction = 0

    # 向左移动，修改坐标 pos 中的内容，就是删除最后一个，在队首添加一个节点，坐标是当前第一个的横坐标减去 20
    def move_left(self, randomPoint):
        first = self.pos[0]
        newPos = [first[0] - 20, first[1]]
        if (self.eatRandomPoint(newPos, randomPoint) == True):
            # 碰撞自身
            for pos in self.pos:
                if (pos == newPos):
                    self.live = 1
                    break
            # 碰壁
            if (newPos[0] < 0):
                self.live = 1
            self.pos.insert(0, newPos)
            self.pos.pop()

    # 仅仅修改方向为向左
    def left(self):
        if (self.direction != 0):
            # 移动后方向已经改变
            self.direction = 2

# 随机点对象
class RandomPoint(pygame.sprite.Sprite):
    def __init__(self, point_img, init_pos):
        #随机点的图片
        self.img = point_img
        #出现的位置，是一个随机的横纵坐标
        self.pos = init_pos
        #当前点是否存在 0 表示存在 1 表示不存在
        self.exist = 0

# 设置游戏屏幕大小
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
# 初始化 pygame，使用pygame时首先加上这一句才可以用
pygame.init()
# 设置游戏界面大小、背景图片及标题
# 游戏界面像素大小
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# 游戏界面标题
pygame.display.set_caption('贪吃蛇')
# 背景图
background = pygame.image.load('img/background.png')

#玩家贪吃蛇的身体图片
player_img=pygame.image.load('img/snake.png')
#存储贪吃蛇的身体可以设置成动画，也就是图片的交替显示
snake_img =[]
#添加图片，并限制其大小，其实是进行切割
snake_img.append(player_img.subsurface(pygame.Rect(0, 0, 20, 20)).convert_alpha())
snake_img.append(player_img.subsurface(pygame.Rect(0, 0, 20, 20)).convert_alpha())

#实例化玩家贪吃蛇
player = Player(snake_img)
#贪吃蛇身体的移动频率
snake_frquency = 0

#随机点
point_img = pygame.image.load('img/point.png')
#随机点
#这里的随机点有问题，贪吃蛇移动的位置也就是横纵坐标一定都是 20 的倍数，但是生成的随机点并没有在这写横纵表格中
#position = [random.randint(0,SCREEN_WIDTH - 20), random.randint(0,SCREEN_HEIGHT - 20)]
# 将指定的屏幕分为横纵宽度都为 20 的网格，然后在确定随机点的位置
widthRange = SCREEN_WIDTH // 20 - 1
heightRange = SCREEN_HEIGHT // 20 - 1
position = [random.randint(1,widthRange) * 20, random.randint(1, heightRange) * 20 + 10]

#实例化随机点对象
randomPoint = RandomPoint(point_img, position)

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

    # 绘制玩家贪吃蛇
    # 按照现在的移动方向自动移动贪吃车
    for i in range(0, player.len):
        screen.blit(player.image[i], player.pos[i])

    #如果随机点没有被吃掉，就显示它
    #if (randomPoint.exist == 0):
    # 取消判断，改为吃到就直接生成新的，不在此方法内生成
    screen.blit(randomPoint.img, randomPoint.pos)

    #设置贪吃蛇的移动频率
    # 贪吃蛇在移动过程中接触到随机点，也就是吃到随机点的时候需要将随机点添加到贪吃蛇的队首
    # 将随机点对象传给移动，当吃到随机点的时候还需要重新生成随机点
    if (snake_frquency % 5 == 0):
        direction = player.direction;
        if (direction == 0):
            player.move_right(randomPoint)
        elif (direction == 1):
            player.move_down(randomPoint)
        elif (direction == 2):
            player.move_left(randomPoint)
        elif (direction == 3):
            player.move_up(randomPoint)

    if (snake_frquency == 50):
        snake_frquency = 0;

    snake_frquency += 1
    # 更新屏幕
    pygame.display.update()

    # 获取键盘事件（上下左右按键）
    key_pressed = pygame.key.get_pressed()
    # 处理键盘事件（移动飞机的位置）
    #新问题：这里不应该是移动飞机，而是单纯的修改方向，移动的事情已经是自动的了
    if key_pressed[K_w] or key_pressed[K_UP]:
        player.up()
    if key_pressed[K_s] or key_pressed[K_DOWN]:
        player.down()
    if key_pressed[K_a] or key_pressed[K_LEFT]:
        player.left()
    if key_pressed[K_d] or key_pressed[K_RIGHT]:
        player.right()

    if(player.live == 1):
        print('游戏结束，接触')
        running = False
    # 处理游戏退出，不能删除，不然移动窗体就会死机
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()