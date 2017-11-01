###
#Jhamni Young-Shinnick
#10.25.17
#RisingSun.py
#Interactive Animation w/rising Sun
###
import time

import Tkinter as tk #names TKinter to be used as tk
from Tkinter import *
root = tk.Tk() #Creates root window
canvas = tk.Canvas(root, width=1000, height=1000, borderwidth=0, highlightthickness=0, bg="white")
canvas.grid() #Fills background white and creates a larger Canvas
#format (x0, y0, x1, y1), all are poits for the circle's box
#canvas.create_oval(100,200,0,300, width=2, fill='red')

class Ball: # Class is object
    def __init__(self,color,size,x,y):
        self.color = color
        self.size = size
        self.x = x
        self.y = y
        self.xVel = 0
        self.yVel = 0
        self.xAccel = 0
        self.yAccel = 0
        global canvas
        self.sprite = canvas.create_oval(self.x,self.y,self.x + self.size,self.y + self.size, width=2, fill=self.color)
    def move(self):# moves ball
        self.xVel = self.xVel + self.xAccel
        self.yVel = self.yVel + self.yAccel
        canvas.move(self.sprite,self.xVel,self.yVel)
        self.x = self.x + self.xVel
        self.y = self.y + self.yVel
        if(self.y > 801): # if above 800 sets to 800 then flips velocity and lowers
            self.setPos(self.x,800)
            self.setVel(self.xVel,self.yVel * -0.9)
        if(self.x > 1001): # if above 1000 set to 100 and flip velocity and lower
            self.setPos(1000,self.y)
            self.setVel(self.xVel * -0.9,self.yVel)
        if(self.x < -1):
            self.setPos(0,self.y)
            self.setVel(self.xVel * -0.9,self.yVel)
    def setAccel(self, x ,y):
        self.xAccel = x
        self.yAccel = y
    def setVel(self, x ,y):
        self.xVel = x
        self.yVel = y
    def setColor(self,color):
        global canvas
        canvas.itemconfig(self.sprite, fill=color)
    def setPos(self,x,y):
        canvas.move(self.sprite,x - self.x,y - self.y)
        self.x = x
        self.y = y
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple','pink','black']

balls = []
for point in range(0,50):
    balls.append(Ball(colors[point%8],50,(point*15),800 - (point * 15)))#gives color
    balls[point].setVel(4,-30)
    balls[point].setAccel(0,1)
    balls[point].setColor(colors[point%8])
def tick():#event loop
    global ball
    for ball in balls:
        ball.move()
    time.sleep(0.015)
    canvas.after(1,tick)
tick()
root.mainloop()# Event loop