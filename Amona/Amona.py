
import pygame
import time
import math
import random
import threading
import mysql.connector
import logging 
import request
import json    
from enum import Enum
from copy import deepcopy


class Color(Enum):
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)
    DARKGRAY = (50,50,50)
    GRAY = (125,125,125)
    LIGHTGRAY = (200,200,200)

class dbData(Enum):
    ID = 0
    MENSAJE = 1
    LEIDO = 2
    FECHA = 3




gMensajes = []
gNuevo = False
gQuit = False
gFontSize = 50
gMargen = 20

#initialize pygame
pygame.init()
pygame.mouse.set_visible(0)
pygame.font.init()

#screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
screen = pygame.display.set_mode((0, 0), pygame.NOFRAME)
#screen = pygame.display.set_mode((200, 200))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", gFontSize)


url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
headers = {'content-type': 'application/json'}

response = requests.post(url, data=json.dumps(payload), headers=headers)



logging.basicConfig(filename='./myapp.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')






def gui():
    global gQuit
    global gNuevo
    global gMensajes
    global gFontSize
    global gMargen
    try:
        screen.fill(Color.WHITE.value)
        pygame.display.flip()
        time.sleep(2)
        db = mysql.connector.connect(user='python', password='python', database='amona', autocommit=True)
        dbCursor = db.cursor()
        while not gQuit:
            clock.tick(10)
            if gNuevo == True:
                if len(gMensajes) > 0:
                    screen.fill(Color.WHITE.value)
                else:
                    screen.fill(Color.RED.value)
                mensajes = []
                for gMensaje in gMensajes:
                    mensajes.append("- "+gMensaje[dbData.MENSAJE.value])
                gNuevo = False
                for i in range(0,len(mensajes)):
                    text = font.render(mensajes[i], True, Color.BLACK.value)
                    screen.blit(text, (gMargen,gMargen+((gFontSize+gMargen)*i)))
                pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    posicionX, posicionY = pygame.mouse.get_pos()
                    leer = -1
                    if len(gMensajes) > 0 and posicionY < (gMargen+((gFontSize+gMargen)*0)+(gFontSize+(gMargen/2))):
                        leer = 0
                    elif len(gMensajes) > 1 and (gMargen+((gFontSize+gMargen)*0)+(gFontSize+(gMargen/2))) < posicionY < (gMargen+((gFontSize+gMargen)*1)+(gFontSize+(gMargen/2))):
                        leer = 1
                    elif len(gMensajes) > 2 and (gMargen+((gFontSize+gMargen)*1)+(gFontSize+(gMargen/2))) < posicionY < (gMargen+((gFontSize+gMargen)*2)+(gFontSize+(gMargen/2))):
                        leer = 2
                    elif len(gMensajes) > 3 and (gMargen+((gFontSize+gMargen)*2)+(gFontSize+(gMargen/2))) < posicionY < (gMargen+((gFontSize+gMargen)*3)+(gFontSize+(gMargen/2))):
                        leer = 3
                    elif len(gMensajes) > 4 and (gMargen+((gFontSize+gMargen)*3)+(gFontSize+(gMargen/2))) < posicionY < (gMargen+((gFontSize+gMargen)*4)+(gFontSize+(gMargen/2))):
                        leer = 4
                    if leer > -1:
                        dbCursor.execute("UPDATE mensajes SET leido=TRUE WHERE id="+str(gMensajes[leer][dbData.ID.value])+";")
                        gMensajes.pop(leer)
                        gNuevo = True
                if event.type == pygame.QUIT:
                    gQuit = True
                    break
        pygame.quit()
    except:
        logging.exception('')
        logging.info("gQuit: "+str(gQuit)+" - gNuevo: "+str(gNuevo)+" - gMensajes: "+str(gMensajes))
        gQuit = True
        pygame.quit()




def data():
    global gMensajes
    global gNuevo
    global gQuit
    try:
        db = mysql.connector.connect(user='python', password='python', database='amona', autocommit=True)
        dbCursor = db.cursor()
        while not gQuit:
            dbCursor.execute("SELECT * FROM mensajes WHERE "+dbData.LEIDO.name+" = FALSE")
            mensajes = list(dbCursor)
            if len(gMensajes) != len(mensajes):
                gMensajes = deepcopy(mensajes)
                gNuevo = True
            else:
                for mensaje in mensajes:
                    nuevo = True
                    for gMensaje in gMensajes:
                        if mensaje == gMensaje:
                            nuevo = False
                            break
                    if nuevo == True:
                        gMensajes = deepcopy(mensajes)
                        gNuevo = True
                        break
            time.sleep(10)
            while gNuevo == True and not gQuit:
                time.sleep(1)
        db.close()
    except:
        logging.exception('')
        logging.info("gQuit: "+str(gQuit)+" - gNuevo: "+str(gNuevo)+" - gMensajes: "+str(gMensajes))
        gQuit = True
        quit()




#main script
dataThread = threading.Thread(target=data, name='DATA')
dataThread.start()
gui()


