import pygame
import time
import math
import random


#initialize pygame
pygame.init()
waveh = 200
size = [1300, waveh*2+5]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Sine")
clock = pygame.time.Clock()


zero = waveh+2
posx = 0
red = (255,0,0)
blue = (0,0,255)

#frequency = times in the screen     -negative is cosine
times = -37
freq = (size[0]/times)/(2*3.141592)


screen.fill((255,255,255))
pygame.display.flip()

for i in range(0,size[0]):

    if math.sin(posx/freq) > math.sin((posx-1)/freq):
        holder = int(zero+waveh*(math.sin(posx/freq)))
        goal = int(zero+waveh*(math.sin((posx-1)/freq)))
        while holder > goal:
            screen.set_at((posx, holder), red)
            holder -= 1

    elif math.sin(posx/freq) < math.sin((posx-1)/freq):
        holder = int(zero+waveh*(math.sin(posx/freq)))
        goal = int(zero+waveh*(math.sin((posx-1)/freq)))
        while holder < goal:
            screen.set_at((posx, holder), red)
            holder += 1
    screen.set_at((posx, int(zero+waveh*(math.sin(posx/freq)))), red)
    screen.set_at((posx,zero),blue)
    posx += 1

pygame.display.flip()
    
    
