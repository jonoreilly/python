import time
import random
from copy import deepcopy


class cube():

    def __init__ (self, model=None):

        if model == None:

            self.face = [
                [[0,0,0],
                [0,0,0],
                [0,0,0]],
                
                [[1,1,1],
                [1,1,1],
                [1,1,1]],
                
                [[2,2,2],
                [2,2,2],
                [2,2,2]],
                
                [[3,3,3],
                [3,3,3],
                [3,3,3]],
                
                [[4,4,4],
                [4,4,4],
                [4,4,4]],

                [[5,5,5],
                [5,5,5],
                [5,5,5]],
                ]
        else:
            self.face = model



    def get(self, value):
        return value



    # 0=Front, 1=Back, 2=Top, 3=Right, 4=Bottom, 5=left

    def spin(self, side, direction):

        held = deepcopy(self.face)
        
        if direction == "C" or direction == "c":
            times = 3
        elif direction == "A" or direction == "a":
            times = 1

        for each in range (0,times):

            for i in range (0,3):
                for e in range (0,3):
                    self.face [side] [e] [i] = int(held [side] [i] [2-e])

            if side == 0:
                for i in range (0,3):
                    self.face [2] [2] [i] = int(held [3] [i] [0])
                    self.face [3] [i] [0] = int(held [4] [0] [2-i])
                    self.face [4] [0] [i] = int(held [5] [i] [2])
                    self.face [5] [i] [2] = int(held [2] [2] [2-i])

            elif side == 1:
                for i in range (0,3):
                    self.face [3] [i] [2] = int(held [2] [0] [i])
                    self.face [2] [0] [i] = int(held [5] [2-i] [0])
                    self.face [5] [i] [0] = int(held [4] [2] [i])
                    self.face [4] [2] [i] = int(held [3] [2-i] [2])

            elif side == 2:
                for i in range (0,3):
                    self.face [0] [0] [i] = int(held [5] [0] [i])
                    self.face [5] [0] [i] = int(held [1] [0] [i])
                    self.face [1] [0] [i] = int(held [3] [0] [i])
                    self.face [3] [0] [i] = int(held [0] [0] [i])

            elif side == 3:
                for i in range (0,3):
                    self.face [0] [i] [2] = int(held [2] [i] [2])
                    self.face [2] [i] [2] = int(held [1] [2-i] [0])
                    self.face [1] [i] [0] = int(held [4] [2-i] [2])
                    self.face [4] [i] [2] = int(held [0] [i] [2])

            elif side == 4:
                for i in range (0,3):
                    self.face [0] [2] [i] = int(held [3] [2] [i])
                    self.face [3] [2] [i] = int(held [1] [2] [i])
                    self.face [1] [2] [i] = int(held [5] [2] [i])
                    self.face [5] [2] [i] = int(held [0] [2] [i])

            elif side == 5:
                for i in range (0,3):
                    self.face [0] [i] [0] = int(held [4] [i] [0])
                    self.face [4] [i] [0] = int(held [1] [2-i] [2])
                    self.face [1] [i] [2] = int(held [2] [2-i] [0])
                    self.face [2] [i] [0] = int(held [0] [i] [0])
                

        
    def print(self, face):

        print()
        for i in range(0,3):
            output = "       "
            for e in range (0,3):
                output += str(face[2][i][e])
                output += " "
            print(output)
           
        print()

        for i in range(0,3):
            output = ""
            for e in range (0,3):
                output += str(face[5][i][e])
                output += " "
            output += " "
            
            for e in range (0,3):
                output += str(face[0][i][e])
                output += " "
            output += " "
            
            for e in range (0,3):
                output += str(face[3][i][e])
                output += " "
            output += " "

            for e in range (0,3):
                output += str(face[1][i][e])
                output += " "
            print (output)
            
        print()

        for i in range(0,3):
            output = "       "
            for e in range (0,3):
                output += str(face[4][i][e])
                output += " "
            print(output)
        print()                



def game():
    rubik = cube()
    while True:
        rubik.print(rubik.face)
        side = int(input("What side do u wanna turn?  -> "))
        direction = input("Clockways (C) or Anticlockways (A)?  -> ")
        rubik.spin(side, direction)


game()














