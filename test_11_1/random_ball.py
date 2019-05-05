from tkinter import *
import time
import random

# 生成小球类
class ball:
    def __init__(self, canvas, color):
        self.speed = random.randint(2, 8)#随机的速度

        self.canvas = canvas
        a = random.randint(10, 30)#随机的大小
        self.id = canvas.create_oval(20, 20, a+20, a+20, fill=color)

        x = random.randint(0, self.canvas.winfo_width())#随机的位置
        y = random.randint(0, self.canvas.winfo_height())

        self.canvas.move(self.id, x, y)#随即位置

        self.x=-1 * self.speed
        self.y=-1 * self.speed
        self.canvas_height=self.canvas.winfo_height()#获取窗口高度
        self.canvas_width=self.canvas.winfo_width()#获取窗体宽度

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        post=self.canvas.coords(self.id)#x1,y1,x2,y2
        if post[0]<=0:self.x=self.speed
        if post[1]<=0:self.y=self.speed
        if post[2]>=self.canvas_width:self.x=-1 * self.speed
        if post[3]>=self.canvas_height:self.y=-1 * self.speed

# 生成游戏背景窗体
tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=800, height=600, bd=0, highlightthickness=0)
canvas.pack()
tk.update()  # 刷新

# 小球实例化
ball_1 = ball(canvas, 'green')
ball_2 = ball(canvas, 'red')
ball_3 = ball(canvas, 'blue')
while True:
    ball_1.draw()
    ball_2.draw()
    ball_3.draw()
    tk.update_idletasks()#刷新的幕布
    tk.update()
    time.sleep(0.01)