import pygame
import time
import math
import random

import cursors
import units

#initialize pygame
pygame.init()
background = pygame.image.load("background.png")
size = background.get_size()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Age of Empires :  The secret of Santa Patata")
clock = pygame.time.Clock()


def refresh():
    pygame.display.flip()
    screen.blit(background,(0,0))
    

def intro():
    screen.fill((125,125,125))
    pygame.font.init()
    font = pygame.font.SysFont("Comic Sans MS", 30)
    text = font.render("Age of Empires :  The secret of Santa Patata", True, (255,0,0))
    screen.blit(text, (200,size[1]/2))
    pygame.display.flip()
    time.sleep(2)


def game():
    refresh()
    mouse = cursors.cursors()
    #generate random units
    for i in range (0,5):
        exec ("player%d = units.MOB(screen,units.unitlist[random.randint(0,2)],\"player\",[random.randint(0,int(size[0]*9/10)),random.randint(0,int(size[1]*9/10))])" % (i))
    for i in range (0,5):
        exec ("player%d = units.MOB(screen,units.unitlist[random.randint(0,2)],\"enemy\",[random.randint(0,int(size[0]*9/10)),random.randint(0,int(size[1]*9/10))])" % (i))
    refresh()
    while True:
        clock.tick(60)
        cursors.readmouse(mouse, units.items)
        for item in units.items:
            item.move()
        refresh()



#main script
intro()
game()









