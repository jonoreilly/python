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
windowsize = [400,500]  
screen = pygame.display.set_mode(windowsize)
pygame.display.set_caption("Test1")


#clock
clock = pygame.time.Clock()   #clock.tick( X )  where X is FPS


'''
#data init
pxarray = []
for i in range (0,windowsize[0]):
    pxarray.append([])
    for e in range (0,windowsize[1]):
        pxarray[i].append([])
'''


#draw to screen
def refresh():
    pygame.display.flip()

    
#set pixel to
def pixel (place,color): #place = (x,y)
    screen.set_at(place,color)


#end all
def shutdown():
    pygame.quit()
    quit()

'''
#sketch a line using arrow keys step by step
def gametest ():
    cursor = [0,0]
    color = white
    speed = [0,0]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()              
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and cursor[1] > 0:
                    speed[1] = -1
                    color = red
                elif event.key == pygame.K_DOWN and cursor[1] < size[1]:
                    speed[1] = 1
                    color = green
                elif event.key == pygame.K_RIGHT and cursor[0] < size[0]:
                    speed[0] = 1
                    color = blue
                elif event.key == pygame.K_LEFT and cursor[0] > 0:
                    speed[0] = -1
                    color = yellow
            elif event.type == pygame.KEYUP:
                speed = [0,0]
        cursor[0] += speed[0]
        cursor[1] += speed[1]
        pixel(cursor,color)
        pygame.display.flip()
        clock.tick(60)
'''


'''
#test keymap class (arrow keys)
def inputtest ():
    keys = keymap()
    while True:
        keys.inputs()
        keys.action()
'''


#draw a rectangle and move it on screen (main loop)
def rectangletest():
    player = MOB()
    keys = keymap()
    while True:
        keys.inputs()
        keys.action(player)
        screen.fill(white)
        player.draw()
        refresh()
        clock.tick(60)

        
#keyboard input manipulation class
class keymap ():
    #key flags
    UP = False
    DOWN = False
    LEFT = False
    RIGHT = False
    ESCAPE = False
    SPACE = False

    #set input flags
    def inputs (self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                shutdown()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    shutdown()
                elif event.key == pygame.K_UP:
                    self.UP = True
                elif event.key == pygame.K_DOWN:
                    self.DOWN = True
                elif event.key == pygame.K_LEFT:
                    self.LEFT = True
                elif event.key == pygame.K_RIGHT:
                    self.RIGHT = True
                elif event.key == pygame.K_SPACE:
                    self.SPACE = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.UP = False
                elif event.key == pygame.K_DOWN:
                    self.DOWN = False
                elif event.key == pygame.K_LEFT:
                    self.LEFT = False
                elif event.key == pygame.K_RIGHT:
                    self.RIGHT = False
                elif event.key == pygame.K_SPACE:
                    self.SPACE = False

    #call functions if flags 
    def action (self, car):
        speed = [0, 0]
        if self.UP:
            speed[1] += -1
        if self.DOWN:
            speed[1] += 1
        if self.LEFT:
            speed[0] += -1
        if self.RIGHT:
            speed[0] += 1
        car.move(speed)
        if self.SPACE:
            car.color = red
        else:
            car.color = green


#player class
class MOB ():
    pos = [0, 0]
    size = [20, 20]
    color = black


    #set position
    def move(self, speed):
        self.pos[0] += speed[0]
        self.pos[1] += speed[1]


    #draw square
    def draw(self):
        pygame.draw.rect(screen, self.color,(self.pos[0], self.pos[1], self.size[0], self.size[1]))#add frame_size between ")" - ")"


#main script
screen.fill(white)
rectangletest()





