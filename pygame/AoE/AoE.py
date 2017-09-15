import random
import pygame
import os
import time
import math



#initialize pygame
pygame.init()
background = pygame.image.load("background.png")
size = background.get_size()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Age of Empires :  Popeye returns")
clock = pygame.time.Clock()

def refresh():
    pygame.display.flip()
    screen.blit(background,(0,0))

#load image with all 8 directions 0-up 2-right
class MOB():
    def __init__(self):
        self.images = []
        for i in range(0,4):
            self.images.append(pygame.image.load("caballo" + str(i) + ".png"))
        self.index = 0
        self.image = self.images[self.index]
        self.pos = [size[0]/2,size[1]/2]
        self.speed = 1
        self.steps = 0
        self.direction = [0,1]
        

    def draw(self):
        screen.blit(self.image,self.pos)

    def setdirection(self, direction):
        diference = [direction[0] - self.pos[0], direction[1] - self.pos[1]]
        distance = math.sqrt(diference[0]**2 + diference[1]**2)
        if abs(diference[0]) > abs(diference[1]):
            if diference[0] > 0:
                self.index = 1
            else:
                self.index = 3        
        elif abs(diference[0]) < abs(diference[1]):
            if diference[1] > 0:
                self.index = 2
            else:
                self.index = 0
        self.image = self.images[self.index]
        self.direction[0] = (diference[0]/(distance/self.speed))
        self.direction[1] = (diference[1]/(distance/self.speed))
        self.steps = (distance/self.speed)

    def move(self):
        if self.steps > 0:
            self.pos[0] += self.direction[0]
            self.pos[1] += self.direction[1]
            self.steps -= 1
        self.draw()

    
def readmouse(player):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:  #1-left, 2-wheel, 3-right
             player.setdirection(pygame.mouse.get_pos())
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
                    
def game():
    refresh()
    caballo = MOB()
    caballo.draw()
    refresh()
    while True:
        clock.tick(60)
        readmouse(caballo)
        caballo.move()
        refresh()


    


#main script
game()
            
            
            

    
