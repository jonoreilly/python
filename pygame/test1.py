import time
import random
import pygame
import os



#colors
black  = (  0,  0,  0)
white  = (255,255,255)
red    = (200,  0,  0)
green  = (  0,200,  0)
blue   = (  0,  0,200)
yellow = (  0,150,150) 


#init
pygame.init()


#display
size = [400,500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Test1")


#clock
clock = pygame.time.Clock()


#data init
pxarray = []
for i in range (0,size[0]):
    pxarray.append([])
    for e in range (0,size[1]):
        pxarray[i].append([])


def refresh():
    pygame.display.flip()
    
    
def pixel (place,color): #place = (x,y)
    screen.set_at(place,color)
    
    
def gametest ():
    cursor = [0,0]
    color = white
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and cursor[1] > 0:
                    cursor[1] -= 1
                    color = red
                elif event.key == pygame.K_DOWN and cursor[1] < size[1]:
                    cursor[1] += 1
                    color = green
                elif event.key == pygame.K_RIGHT and cursor[0] < size[0]:
                    cursor[0] += 1
                    color = blue
                elif event.key == pygame.K_LEFT and cursor[0] > 0:
                    cursor[0] -= 1
                    color = yellow
        pixel(cursor,color)
        pygame.display.flip()
        clock.tick(10)
        

#main script
screen.fill(white)
gametest()





