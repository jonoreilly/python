import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

car_width = 59
car_height = 54

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
blue = (0,0,200)
bright_red = (250,0,0)
bright_green = (0,250,0)
bright_blue = (0,0,250)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("A bit Racey")
clock = pygame.time.Clock()

carImg = pygame.image.load("pygame1car.png")

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged:"+str(count), True, green)
    gameDisplay.blit(text, (0,0))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def crash():
    message_display("You Crashed")

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf",115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()

def game_logic():
    if x > display_width - car_width or x < 0:
        crash()

    if thing_starty > display_height:
        thing_starty = 0 - thing_height
        thing_startx = random.randrange(0, display_width - (thing_width-(thing_width%1)))
        dodged += 1
        #thing_speed += 1
        #thing_width += (dodged * 1.2)


    if y <= (thing_starty + thing_height):
        print("step 1")

        if x > (thing_startx - car_width) and x < (thing_startx + thing_width):
            print("x crossover")
            crash()

def game_controles():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
                print("leftkey")

            elif event.key == pygame.K_RIGHT:
                x_change = 5
                print("rightkey")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
                print("keyup")

        print(event)

def game_init(x,y,x_change,dodged,thing_startx,thing_starty,thing_speed,thing_width,thing_height):

    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    dodged = 0
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100

def game_quit():
    pygame.quit()
    quit()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x<mouse[0]<x+w and y<mouse[1]<y+h:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)


def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font("freesansbold.ttf",115)
        TextSurf, TextRect = text_objects("A bit Racey", largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!",150,450,100,50,green,bright_green,game_loop)
        button("Quit",500,450,100,50,red,bright_red,game_quit)

        pygame.display.update()
        clock.tick(15)

def game_loop():

    #game_init
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    dodged = 0
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100

    while True:

        #game_controles()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                    print("leftkey")

                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                    print("rightkey")

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                    print("keyup")

            print(event)

        x += x_change

        gameDisplay.fill(white)

        things(thing_startx, thing_starty, thing_width, thing_height, red)

        thing_starty += thing_speed

        #game_logic()
        if x > display_width - car_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width - (thing_width-(thing_width%1)))
            thing_speed += 1
            thing_width += (dodged * 1.2)

        if y <= (thing_starty + thing_height):

            if x > (thing_startx - car_width) and x < (thing_startx + thing_width):
                crash()

        car(x,y)

        things_dodged(dodged)

        pygame.display.update()

        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()
