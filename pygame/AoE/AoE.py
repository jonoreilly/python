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

#all objects
items = []

class cursor():
    def __init__(self):
        self.size = (24,24)
        self.point = (7,7)
        self.hand = [[
            "                        ",
            "   BB                   ",
            "  BWWB                  ",
            " BWWWWB       BB        ",
            " BWWWWWB     BWWB       ",
            "  BWWWWWB   BBWWWB      ",
            "   BWWWWWB BWWBWWWB     ",
            "    BWWWWWBWWWWWWWB     ",
            "     BWWWWWBWWWWWWWB    ",
            "      BWWWWWWWWWWWWB    ",
            "       BWWWWWWWWWWWWB   ",
            "      BWBWWWWWWWWWWWB   ",
            "     BWWWBWWWWWWWWWWB   ",
            "     BWWWBBWWWWWWWWWWBB ",
            "     BWWWWWWWWWWWWWWBWWB",
            "      BWWWWWWWWWWWWBWWB ",
            "      BWWWWWWWWWWWBWWB  ",
            "       BBWWWWWWWWBWWB   ",
            "         BBBWWWWBWWB    ",
            "            BBWBWWB     ",
            "              BWWB      ",
            "              BWB       ",
            "               B        ",
            "                        "],[
            "                        ",
            "                        ",
            "                        ",
            "     BB       BB        ",
            "    BWWB     BWWB       ",
            "   BWWWWB   BBWWWB      ",
            "  BWWWWWWB BWWBWWWB     ",
            "  BWWBWWWWBWWWWWWWB     ",
            "   BBBWWWWWBWWWWWWWB    ",
            "      BWWWWWWWWWWWWB    ",
            "       BWWWWWWWWWWWWB   ",
            "      BWBWWWWWWWWWWWB   ",
            "     BWWWBWWWWWWWWWWB   ",
            "     BWWWBBWWWWWWWWWWBB ",
            "     BWWWWWWWWWWWWWWBWWB",
            "      BWWWWWWWWWWWWBWWB ",
            "      BWWWWWWWWWWWBWWB  ",
            "       BBWWWWWWWWBWWB   ",
            "         BBBWWWWBWWB    ",
            "            BBWBWWB     ",
            "              BWWB      ",
            "              BWB       ",
            "               B        ",
            "                        "]]
        
        self.sword = [[
            "          B             ",
            "         BWB            ",
            "        BWWB            ",
            "        BWWB            ",
            "        BWWB            ",
            "       BWWB    B        ",
            "       BWWB   BWB       ",
            "       BWWB   BWB       ",
            "      BWWB    BWB       ",
            "      BWWB    BWWB      ",
            "      BWWB     BWB      ",
            "     BWWB      BWB BB   ",
            "     BWWB       BBBBB   ",
            " BB  BWWB      BBBB     ",
            " BBBBWWB      BBBBB     ",
            "  BBBBBB      BB  BB    ",
            "   BBBBBB         BB    ",
            "    BBBBBB              ",
            "   BBB  BB              ",
            "   BBB                  ",
            "  BBB                   ",
            "                        ",
            "                        ",
            "                        "],[
            "                    BB  ",
            "       B     BB    BB   ",
            "       BB   BB          ",
            "            B           ",
            "            B     BB    ",
            " BB    B        BBWB    ",
            "  BB  BBBB     BWWWB    ",
            "      BWWBB  BBWWWB     ",
            "      BBWWBBBWWWWWB  BBB",
            "       BWWWBWWWWWB      ",
            "       BBWBWWWWWB       ",
            "  B     BBWWWWWB        ",
            " BBB   BBWWWWWBB        ",
            " BBBB BBWWWWBBWBBB      ",
            "  BBBBBWWWWBBBWWWBB  BB ",
            "   BBBWWWWB  BBWWWBBBBB ",
            "   BBBWWWB    BBWWBBBB  ",
            "  BBBBBWB      BBBBBB   ",
            " BBBBBBB        BBBBBB  ",
            "BBBBBBBBBB     BBB BBBB ",
            "BBBBBB BBB     BB   BBB ",
            " BBB                    ",
            "  B                     ",
            "                        "
            ]]
        self.handmask = pygame.cursors.compile(self.hand[0],black="B",white="W",xor="o"), pygame.cursors.compile(self.hand[1],black="B",white="W",xor="o")
        self.swordmask = pygame.cursors.compile(self.sword[0],black="B",white="W",xor="o"), pygame.cursors.compile(self.sword[1],black="B",white="W",xor="o")

        self.mask = self.handmask
        self.data,self.maskd = self.mask[0]
        pygame.mouse.set_cursor(self.size, self.point, self.data, self.maskd)

    def pressed(self):
        self.data,self.maskd = self.mask[1]
        pygame.mouse.set_cursor(self.size, self.point, self.data,self.maskd)

    def released(self):
        self.data,self.maskd = self.mask[0]
        pygame.mouse.set_cursor(self.size, self.point, self.data,self.maskd)
                
def refresh():
    pygame.display.flip()
    screen.blit(background,(0,0))

#load image with all 8 directions 0-up 2-right
class MOB():
    def __init__(self, team, pos):
        items.append(self)
        self.team = team
        self.images = []
        if self.team == "player":
            for i in range(0,4):
                self.images.append(pygame.image.load("caballo" + str(i) + ".png"))
            self.index = 0
            self.image = self.images[self.index]
        else:
            self.image = pygame.image.load("persona.png")
        self.speed = 1
        self.attack = False
        self.target = None
        self.direction = [0,1]
        self.steps = 0
        self.hitbox = self.image.get_rect()
        self.death = pygame.image.load("sangre.png")
        self.pos = pos
        self.status = "alive"
 

    def skin(self):
        self.image = self.images[self.index]
        self.hitbox = self.image.get_rect()  

    def draw(self):
        screen.blit(self.image,self.pos)

    def setdirection(self, direction):
        if self.status == "alive":
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
            self.skin()
            self.direction[0] = (diference[0]/(distance/self.speed))
            self.direction[1] = (diference[1]/(distance/self.speed))
            self.steps = (distance/self.speed)

    def move(self):
        if self.status == "alive":
            if self.steps > 0:
                self.pos[0] += self.direction[0]
                self.pos[1] += self.direction[1]
                self.steps -= 1
            elif self.attack:
                self.target.die()
        self.draw()

    def die(self):
        self.status = "dead"
        self.image = self.death
        self.draw()

        

    
def readmouse(mouse,player):
    attacking = False
    for item in items:
        if item.team == "enemy":
            print("Mouse :  "+str(pygame.mouse.get_pos()) +"    Enemy :  "+str(item.pos)+"      Hitbox :  "+str(item.hitbox))
            if item.pos[0] <  pygame.mouse.get_pos()[0] < item.pos[0] + item.hitbox[2]:
                if item.pos[1] <  pygame.mouse.get_pos()[1] < item.pos[1] + item.hitbox[3]:
                    mouse.mask = mouse.swordmask
                    enemy = item
                else:
                    mouse.mask = mouse.handmask
            else:
                mouse.mask = mouse.handmask
   
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:  #1-left, 2-wheel, 3-right
            player.setdirection(pygame.mouse.get_pos())
            mouse.pressed()
            if mouse.mask == mouse.swordmask: 
                player.attack = True
                player.target = enemy
            else:
                player.attack = False
                player.target = None
        if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            mouse.released()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
    if not pygame.mouse.get_pressed()[2]:
        mouse.released()
                    
def game():
    refresh()
    mouse = cursor()
    persona = MOB("enemy", [size[0]/1.5, size[1]/1.5])
    caballo = MOB("player", [size[0]/2,size[1]/2])
    caballo.draw()
    refresh()
    while True:
        clock.tick(60)
        readmouse(mouse,caballo)
        for item in items:
            item.move()
        refresh()





#main script
game()
            
            
            

    
