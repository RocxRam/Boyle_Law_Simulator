import pygame
import random
from settings import *
import math

class Molecule:
    def __init__(self,x,y,temp):
        self.x=x
        self.y=y
        v=math.sqrt(temp)/3.5
        self.vx=random.uniform(-v,v)
        self.vy=random.uniform(-v,v)
        self.radius=5
        self.hot=int(temp/1001*255)

    def move(self,piston_y):
        self.x+=self.vx
        self.y+=self.vy
        if self.x-self.radius<=CHAMBER_X:
            self.x=CHAMBER_X+self.radius
            self.vx*=-1
        if self.x+self.radius>=CHAMBER_X+CHAMBER_WIDTH:
            self.x=CHAMBER_X+CHAMBER_WIDTH-self.radius
            self.vx*=-1
        if self.y-self.radius<=piston_y+PISTON_HEIGHT:
            self.y=piston_y+self.radius+PISTON_HEIGHT+1
            self.vy*=-1
        if self.y+self.radius>=CHAMBER_Y+CHAMBER_HEIGHT:
            self.y=CHAMBER_Y+CHAMBER_HEIGHT-self.radius-1
            self.vy*=-1
            
    def set_temperature(self,temp,old_temp):
        v=math.sqrt(temp)/3.5
        magnitude=(self.vx**2+self.vy**2)**0.5
        if magnitude==0:
            magnitude=1
        self.vx=self.vx/magnitude*v
        self.vy=self.vy/magnitude*v
        self.hot=int(temp/1001*255)

    def collide(self,other):
        dx=self.x-other.x
        dy=self.y-other.y
        dist=(dx**2+dy**2)**0.5
        if dist<=self.radius+other.radius:
            self.vx,other.vx=other.vx,self.vx
            self.vy,other.vy=other.vy,self.vy
    
    def draw(self,screen):
        pygame.draw.circle(screen,(self.hot,50+self.hot*100/255,255-self.hot),(int(self.x),int(self.y)),self.radius)

