import numpy as np
import random, sys
import pgzrun
class Brick(Actor):
    def react(self):
        if np.abs(mario.center[1]+mario.size[1]/2-self.center[1]+self.size[1]/2)<15: # z gory
            mario.vy = 0
            mario.bottom = self.top
        elif np.abs(mario.center[1]-mario.size[1]/2-self.center[1]-self.size[1]/2)<15: # z dolu
            mario.vy = 0
            mario.top = self.bottom
        elif np.abs(mario.center[0]+mario.size[0]/2-self.center[0]+self.size[0]/2)<15: # z prawej
            moveall(6)
        elif np.abs(mario.center[0]-mario.size[0]/2-self.center[0]-self.size[0]/2)<15: # z lewej
            moveall(-6)
    def move(self):
        pass
 
class Coin(Actor):
    def react(self):
        if mario.colliderect(self):
            #sounds.coin.play()
            objs.remove(self)
            mario.points=mario.points+1
    def move(self):
        pass
 
class Block(Actor):
    def react(self):
        if np.abs(mario.center[1]+mario.size[1]/2-self.center[1]+self.size[1]/2)<15: # z gory
            mario.vy = 0
            mario.bottom = self.top
        elif np.abs(mario.center[1]-mario.size[1]/2-self.center[1]-self.size[1]/2)<15: # z dolu
            mario.vy = 0
            mario.top = self.bottom
            animate(self, pos=(self.center[0], -10000))
        elif np.abs(mario.center[0]+mario.size[0]/2-self.center[0]+self.size[0]/2)<15: # z prawej
            moveall(6)
        elif np.abs(mario.center[0]-mario.size[0]/2-self.center[0]-self.size[0]/2)<15: # z lewej
            moveall(-6)
    def move(self):
        pass
 
class Mushroom(Actor):
    def react(self):
        if self.colliderect(mario):
            mario.small=False
            objs.remove(self)
    def move(self):
        for obj in objs:
            if obj!=self and self.colliderect(obj) and not obj.image in ["bush.png","brick.png","hill.png"]:
                self.dir=-self.dir
 
        self.x=self.x+self.dir
 
        uy=self.vy
        self.vy=self.vy+2000.0*0.015
        self.y=self.y+(uy+self.vy)*0.5*0.015
 
        for obj in objs:
            if self.colliderect(obj) and np.abs(self.center[1]+self.size[1]/2-obj.center[1]+obj.size[1]/2)<15:
                self.vy = 0
                self.bottom = obj.top
 
class Question(Actor):
    def react(self):
        if np.abs(mario.center[1]+mario.size[1]/2-self.center[1]+self.size[1]/2)<15: # z gory
            mario.vy = 0
            mario.bottom = self.top
        elif np.abs(mario.center[1]-mario.size[1]/2-self.center[1]-self.size[1]/2)<15: # z dolu
            mario.vy = 0
            mario.top = self.bottom
            if self.image=="question.png":
                self.image = "question2.png"
                objs.append(Mushroom("mushroom.png",(self.center[0],self.center[1]-50)))
                objs[-1].dir=1
                objs[-1].vy=0
                animate(objs[-1],pos=(self.center[0],self.center[1]-objs[-1].size[1]+2))
        elif np.abs(mario.center[0]+mario.size[0]/2-self.center[0]+self.size[0]/2)<15: # z prawej
            moveall(6)
        elif np.abs(mario.center[0]-mario.size[0]/2-self.center[0]-self.size[0]/2)<15: # z lewej
            moveall(-6)
    def move(self):
        pass
 
class Cloud(Actor):
    def react(self):
        pass
    def move(self):
        self.x=(self.x-1)%7000
 
class Monster(Actor):
    def react(self):
        if np.abs(mario.center[1]+mario.size[1]/2-self.center[1]+self.size[1]/2)<15: # z gory
            mario.vy = 0
            mario.bottom = self.top
            animate(self, pos=(self.right+50, HEIGHT+50))
        elif np.abs(mario.center[1]-mario.size[1]/2-self.center[1]-self.size[1]/2)<15: # z dolu
            mario.vy = 0
            mario.top = self.bottom
        elif np.abs(mario.center[0]+mario.size[0]/2-self.center[0]+self.size[0]/2)<15: # z prawej
            if mario.small:
                mario.dead = True
                newgame()
            else:
                animate(self, pos=(self.right+50, HEIGHT+50))
                mario.small=True
        elif np.abs(mario.center[0]-mario.size[0]/2-self.center[0]-self.size[0]/2)<15: # z lewej
            if mario.small:
                mario.dead = True
                newgame()
            else:
                animate(self, pos=(self.right+50, HEIGHT+50))
                mario.small=True
 
    def move(self):
        for obj in objs:
            if obj!=self and self.colliderect(obj) and not obj.image in ["bush.png","brick.png","hill.png"]:
                self.dir=-self.dir
 
        if self.dir==1 and self.image in ["turtle.png","turtleleft.png"]:
            self.image = "turtle.png"
        elif self.dir==-1 and self.image in ["turtle.png","turtleleft.png"]:
            self.image = "turtleleft.png"
 
        self.x=self.x+self.dir
 
class Bush(Actor):
    def react(self):
        pass
    def move(self):
        pass
 
def newgame():
    mario.pos=(200,HEIGHT-120)
    mario.vy=0
    mario.time=0
    mario.dir="right"
    mario.dead=False
    mario.small=True
    mario.s="s"
    mario.points=0
    mario.win=False
 
    for i in range(len(objs)):
        objs.remove(objs[0])
    file = open(sys.path[0] + "\\level1.dat")
 
    i = 0
    for line in file:
        for j in range(len(line)):
            if line[j]=="O":
                objs.append(Brick("brick.png",(j*32,32*i)))
            elif line[j]=="B":
                objs.append(Brick("brick2.png",(j*32,32*i)))
            elif line[j]=="D":
                objs.append(Block("block.png",(j*32,32*i)))
            elif line[j]=="Q":
                objs.append(Question("question.png",(j*32,32*i)))
            elif line[j]=="c":
                objs.append(Cloud("cloud.png",(j*32,32*i)))
            elif line[j]=="h":
                objs.append(Bush("hill.png",(j*32,32*i-22)))
            elif line[j]=="b":
                objs.append(Bush("bush.png",(j*32,32*i-12)))
            elif line[j]=="E":
                objs.append(Monster("enemy1.png",(j*32,32*i)))
                objs[-1].dir = 1
            elif line[j]=="T":
                objs.append(Monster("turtle.png",(j*32,32*i)))
                objs[-1].dir = 1
            elif line[j]=="p":
                objs.append(Coin("coin.png",(j*32,32*i)))
 
        i = i + 1
 
        music.play("theme.mp3")
 
def draw():
    screen.fill((148, 146, 255))
    for obj in objs:
        obj.draw()
    mario.draw()
    screen.draw.text(str(mario.points),color="black",midtop=(WIDTH/8*7,10),fontsize=70,shadow=(0,0))
    if mario.win:
        screen.draw.text("You win!",color="black",midtop=(WIDTH/2,10),fontsize=170,shadow=(0,0))
 
def moveall(x):
    if x>0:
        if 0<=mario.x:
            mario.x=mario.x-x
        elif mario.x<0:
            mario.x=0
    else:
        if 0<=mario.x<WIDTH/2:
            mario.x=mario.x-x
        elif mario.x>WIDTH/2:
            mario.x=WIDTH/2
        elif mario.x>=WIDTH/2:
            for obj in objs:
                obj.x=obj.x+x
 
def move(dt):
    if mario.dir=="right":
        mario.image= mario.s + "mario.png"
    else:
        mario.image= mario.s + "marioleft.png"
 
    uy=mario.vy
    mario.vy=mario.vy+2000.0*dt
    mario.y=mario.y+(uy+mario.vy)*0.5*dt
 
    if keyboard.right:
        if mario.small:
            moveall(-2)
        else:
            moveall(-3)
        mario.dir="right"
        if mario.time<8:
            mario.image= mario.s + "mariomove.png"
        else:
            mario.image= mario.s + "mariomove2.png"
    if keyboard.left:
        if mario.small:
            moveall(2)
        else:
            moveall(3)
        mario.dir="left"
        if mario.time<8:
            mario.image= mario.s + "mariomoveleft.png"
        else:
            mario.image= mario.s + "mariomoveleft2.png"
 
    for obj in objs:
        if  mario.colliderect(obj):
            obj.react()
 
    if mario.vy !=0 and mario.dir=="right":
        mario.image= mario.s + "mariojump.png"
    elif mario.vy !=0 and mario.dir=="left":
        mario.image= mario.s + "mariojumpleft.png"
 
    if mario.bottom>HEIGHT:
        mario.dead = True
 
def update(dt):
    if mario.small:
        mario.s="s"
    else:
        mario.s=""
    mario.time=(mario.time+1)%16
    if not mario.win:
        move(dt)
        for obj in objs:
            obj.move()
            if obj.image=="castle.png":
                if np.abs(obj.center[0]-mario.center[0])<20:
                    mario.win=True
    if mario.dead:
        #music.pause()
        #sounds.gameover.play()
        #from pygame import time
        #mario.dead = False
        #time.wait(3000)
        newgame()
 
def on_key_down(key):
    if key==keys.SPACE and mario.vy==0:
        mario.vy=-800
 
 
HEIGHT=640
WIDTH=1024
TITLE="Mario"
 
mario=Actor("smario.png",(200,HEIGHT-120))
mario.vy=0
mario.time=0
mario.dir="right"
mario.dead=False
mario.small=True
mario.s="s"
mario.points=0
mario.win=False
objs = []
newgame()
pgzrun.go()
