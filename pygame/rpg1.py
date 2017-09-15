import time
import random
import pygame
import os



#colors
black  = (  0,  0,  0)
grey   = (120,120,120)
white  = (255,255,255)
red    = (255,  0,  0)
green  = (  0,255,  0)
blue   = (  0,  0,255)
yellow = (250,250, 60)
brown  = (133, 87, 35)
purple = (143, 22,178)

#monsters   G=ground P=plant E=electric F=fire W=water B=bug   
monsters = (("id", "name", "hp", "dmg", "spd", "type", "color"),
            (1, "Ganjamon", 50, 8, 9, "P", green),
            (2, "Pilamon", 60, 6, 7, "E", yellow),
            (3, "Cacamon", 52, 7, 11, "G", brown),
            (4, "Fufumon", 54, 7, 10, "F", red),
            (5, "Gotamon", 40, 10, 12, "W", blue),
            (6, "Gusamon", 53, 8, 8, "B", purple))

#init
pygame.init()

#display
windowsize = [800,400]  
screen = pygame.display.set_mode(windowsize)
pygame.display.set_caption("RPG 1")

#clock
clock = pygame.time.Clock()   #clock.tick( X )  where X is FPS

#text
pygame.font.init()
font = pygame.font.SysFont("Comic Sans MS", 30)

#pint text
def text(msg, pos, col):
    text = font.render(msg, True, col)
    screen.blit(text, pos)
    
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

#single key pressings
def getkey():
    done = True
    while done:    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                shutdown()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    shutdown()
                elif event.key == pygame.K_SPACE:
                    done = False

'''
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
        if self.UP:
            
        if self.DOWN:
            
        if self.LEFT:
            
        if self.RIGHT:
            
        if self.SPACE:
'''
            
#MOB
class MOB():
    def __init__ (self, side):
        self.id    = random.randint(1,6)
        self.name  = monsters[self.id][1]
        self.hp    = monsters[self.id][2]
        self.dmg   = monsters[self.id][3]
        self.spd   = monsters[self.id][4]
        self.type  = monsters[self.id][5]
        self.color = monsters[self.id][6]
        self.side = side

    #draw square mob
    def rectangle(self, pos):
        pygame.draw.rect(screen, self.color,(pos[0], pos[1], 100, 100))#add frame_size between ")" - ")"


#menu loop
def menu():
    screen.fill(grey)
    text("Fight?     press space", (100,100), black)
    text("Exit?    press escape", (100,300), black)
    refresh()
    getkey()

#draw fight to screen
def drawfight(player,enemy):
    screen.fill(grey)
    text(player.name + "  HP :   " + str(player.hp),(20,100), black)
    text(enemy.name + "  HP :   " + str(enemy.hp),(420,100), black)
    player.rectangle((50,250))
    enemy.rectangle((450,250))
    refresh()

#deal dmg to each other
def strugle(player, enemy, first):
    done = True
    drawfight(player,enemy)
    time.sleep(1)
    while done:
        clock.tick(1)
        pygame.event.pump()
        print("Player :  "+str(player.hp)+"     Enemy :  "+str(enemy.hp))
        print(time.time())
        if first:
            attacker = player
            defender = enemy
            first = False
        else:
            attacker = enemy
            defender = player
            first = True
        defender.hp -= attacker.dmg
        if defender.hp <= 0:
            done = False
        if defender.side == "left":
            pos = (150,300)
        else:
            pos = (550,300)
        drawfight(player, enemy)
        text(str(attacker.dmg),pos,red)
        refresh()

#fight loop
def fight():
    player = MOB("left")
    enemy = MOB("right")
    drawfight(player,enemy)
    if enemy.spd > player.spd:
        strugle(player,enemy,False)
    else :
        strugle(player,enemy,True)
    if enemy.hp > player.hp:
        screen.fill(white)
        text("YOU LOST !!", (150, 150), red)
    else:
        screen.fill(white)
        text("YOU WON !!!!", (150,150), green)
    refresh()
    time.sleep(5)
    shutdown()

#main game loop
def game():
    menu()
    fight()
    

#main class
game()






































