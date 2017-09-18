import pygame
import math
import random
import time

# 0
#3+1
# 2

unitlist =[
    "archer",
    "swordsman",
    "horse"]

class MOBclass():
    def __init__ (self, hp, dmg, rng, spd, aspd, skin):
        self.hp = hp
        self.dmg = dmg
        self.rng = rng
        self.spd = spd
        self.aspd = aspd
        self.skin = skin

units = {
    #"name"    : MOBclass(hp, dmg, rng, spd, aspd, skin),
    "archer"   : MOBclass(200, 20, 150,  10,   60, ("archer")),
    "swordsman": MOBclass(400, 60,  10,   5,   80, ("swordsman")),
    "horse"    : MOBclass(300, 35,  20,  20,   50, ("horse")),
    }

def screenify(surface):
    screen = surface
    


items = []
        
class MOB():
    def __init__ (self, surface, unit, team, pos):
        items.append(self)
        self.unit = unit
        self.team = team
        self.surface = surface

        self.images = []
        for i in range (0,4):
            self.images.append(pygame.image.load(str(unit)+"_"+str(team)+"_"+str(i)+".png"))
        self.index = random.randint(0,3)
        self.image = self.images[self.index]
        self.images.append(pygame.image.load("death.png"))

        self.hp = units[unit].hp
        self.dmg = units[unit].dmg
        self.rng = units[unit].rng
        self.spd = units[unit].spd
        self.aspd = units[unit].aspd

        self.attack = False
        self.target = None

        self.direction = [0,0]
        self.steps = 0
        self.asteps = 0
        self.size = [32,32]
        self.pos = pos
        self.status = "alive"
        self.selected = False

    def draw(self):
        self.image = self.images[self.index]
        if self.selected and self.status == "alive":
            self.healthbar()
        self.surface.blit(self.image,(self.pos[0]-self.size[0]/2,self.pos[1]-self.size[1]/2))

    def setdirection(self, direction):
        diference = [direction[0] - self.pos[0], direction[1] - self.pos[1]]
        distance = math.sqrt(diference[0]**2 + diference[1]**2)
        
        self.direction[0] = diference[0]/(distance/self.spd)
        self.direction[1] = diference[1]/(distance/self.spd)
        if self.attack:
            self.steps = int(((distance-self.rng)/self.spd) +1)
        else:
            self.steps = int(distance/self.spd +1)
        if self.steps < 0:
            self.steps = 0
        
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

    def move(self):
        if self.status == "alive":                    
            if self.steps > 0:
                self.pos[0] += self.direction[0]
                self.pos[1] += self.direction[1]
                self.steps -= 1
            
            elif self.attack:
                if self.asteps <= 0:
                    self.target.damaged(self.dmg,self)
                    self.asteps = self.aspd
            if self.asteps > 0:
                self.asteps -= 1
                        
        else:
            if self.steps == 0:
                items.remove(self)
            else:
                self.steps -= 1
                
        self.draw()

    def die(self):
        self.status = "dead"
        self.index = 4
        self.steps = 100
        self.draw()

    def healthbar(self):
        start = [int(self.pos[0]-self.size[0]/2), int(self.pos[1]-self.size[0]/2-3)]
        pygame.draw.rect(self.surface, (0,0,0), (start[0]-1, start[1]-1, self.size[0]+2,3), 0)
        for i in range(0, self.size[0]):
            self.surface.set_at((start[0]+i, start[1]), (255,0,0))
        for i in range(0, int((self.hp / units[self.unit].hp) * self.size[0]) ):
            self.surface.set_at((start[0]+i, start[1]), (0,255,0))
        
    def damaged(self, dmg, attacker):
        self.hp -= dmg
        if self.hp <1:
            attacker.attack = False
            attacker.target = None
            self.die()
            
            






