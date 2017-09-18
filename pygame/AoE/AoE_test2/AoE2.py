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
    

def readmouse(mouse):
    attacking = False
    target = None
    mouse.setmask("hand")
    #set flags and mouse icon if mous touching item
    for item in units.items:
        item.selected = False
        if item.status == "alive":
            if item.pos[0] - item.size[0]/2 <  pygame.mouse.get_pos()[0] < item.pos[0] + item.size[0]/2:
                if item.pos[1] - item.size[1]/2 <  pygame.mouse.get_pos()[1] < item.pos[1] + item.size[1]/2:
                    if item.team == "enemy":
                        mouse.setmask("sword")
                    target = item
                    target.selected = True

    #actions if clicked
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  #1-left, 2-wheel, 3-right
                mouse.pressed()
                if target == None:
                    mouse.selected = None
                elif target.team == "player":
                    mouse.selected = target
                    target.selected = True
            if event.button == 3 and mouse.selected != None:
                if mouse.selected.team == "player":
                    if target == None:                           
                        mouse.selected.attack = False
                        mouse.selected.target = None
                        mouse.selected.setdirection(pygame.mouse.get_pos())
                    else:
                        if target.team == "enemy":
                            mouse.selected.attack = True
                            mouse.selected.target = target
                            mouse.selected.setdirection(target.pos)
                        else:
                            mouse.selected.attack = False
                            mouse.selected.target = None
                            mouse.selected.setdirection(pygame.mouse.get_pos())
                            
                    mouse.pressed()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
    if not pygame.mouse.get_pressed()[0] and not pygame.mouse.get_pressed()[2]:
        mouse.released()
    if mouse.selected != None:
        mouse.selected.selected = True


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
        readmouse(mouse)
        for item in units.items:
            item.move()
        refresh()



#main script
intro()
game()









