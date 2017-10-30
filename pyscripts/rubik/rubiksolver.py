from copy import deepcopy
import sys
import random
import time

'''
madict = {"patata":"i'm a patata"}
def test(thing):
    try:
        holder = madict[thing]
        print("FULL", madict[thing])
    except KeyError:
        print("EMPTY")
'''

file = open("rubiksolver.txt","w")

endlayout = [[[0,0,0],[0,0,0],[0,0,0]],
            [[1,1,1],[1,1,1],[1,1,1]],
            [[2,2,2],[2,2,2],[2,2,2]],
            [[3,3,3],[3,3,3],[3,3,3]],
            [[4,4,4],[4,4,4],[4,4,4]],
            [[5,5,5],[5,5,5],[5,5,5]]]
dicti = {}
startlayout = []
moves = []
for i in range (0, 6):
    moves.append([i,"a"])
    moves.append([i,"c"])

class cube():

    def __init__ (self, model=deepcopy(endlayout)):
        self.face = model

    def get(self, value):
        return value

    # 0=Front, 1=Back, 2=Top, 3=Right, 4=Bottom, 5=left
    def spin(self, side, direction):
        
        if direction == "C" or direction == "c":
            times = 3
        elif direction == "A" or direction == "a":
            times = 1
        for each in range (0,times):
            held = deepcopy(self.face)
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
                

        
    def printface(self):

        print()
        for i in range(0,3):
            output = "       "
            for e in range (0,3):
                output += str(self.face[2][i][e])
                output += " "
            print(output)
           
        print()

        for i in range(0,3):
            output = ""
            for e in range (0,3):
                output += str(self.face[5][i][e])
                output += " "
            output += " "
            
            for e in range (0,3):
                output += str(self.face[0][i][e])
                output += " "
            output += " "
            
            for e in range (0,3):
                output += str(self.face[3][i][e])
                output += " "
            output += " "

            for e in range (0,3):
                output += str(self.face[1][i][e])
                output += " "
            print (output)
            
        print()

        for i in range(0,3):
            output = "       "
            for e in range (0,3):
                output += str(self.face[4][i][e])
                output += " "
            print(output)
        print()                


    def setsides(self, layout):
        self.face = deepcopy(layout)            


def dictify(layout, lastlayout, side, direction):
    global dicti
    try:
        holder = dicti[str(layout)]
        return False
    except KeyError:
        dicti[str(layout)] = [str(lastlayout),side, direction]
        return True


def progressBar(value, endvalue, bar_length=20):

        percent = float(value) / endvalue
        arrow = '-' * int(round(percent * bar_length)-1) + '>'
        spaces = ' ' * (bar_length - len(arrow))

        sys.stdout.write("\rPercent: [{0}] {1}%".format(arrow + spaces, int(round(percent * 100))))
        sys.stdout.flush()
        

def autogame():
    global rubik, endlayout, startlayout, file, start
    finish = False
    countar = 0
    newlist = [deepcopy(startlayout)]
    dictify (newlist[0], "start", None, None)
    while finish == False:
        mainlist = deepcopy(newlist)
        newlist = []
        if mainlist == []:
            print("u ran out of layouts, mate")
            break
        countar += 1
        print(countar, len(mainlist),"\n")
        counter = 0
        for item in mainlist:
            progressBar(counter, len(mainlist), 50)
            counter += 1
            if item == endlayout:
                finish = True
                break
            for move in moves:
                rubik.setsides(deepcopy(item))
                rubik.spin(move[0], move[1])
                follow = dictify(rubik.face, item, move[0], move[1])
                if follow:
                    newlist.append(deepcopy(rubik.face))
        print()
        print()
        
    if finish:
        selected = endlayout
        output = "["
        while True:
            print("looped")
            output += "["+str(dicti[str(selected)][1])+","+str(dicti[str(selected)][2])+"]"
            selected = dicti[str(selected)][0]
            if selected == str(startlayout):
                output += "]"
                file.write(output)
                print(time.time()-start)
		file.write(time.time()-start)
		file.close()
                break
            else:
                output += ","
                       

def manualgame():
    global rubik, startlayout
    while True:
        rubik.printface()
        try:
            side = int(input("What side do u wanna turn? letter to quit  -> "))
        except ValueError:
            break
        direction = input("Clockways (C) or Anticlockways (A)?  -> ")
        rubik.spin(side, direction)
    startlayout = deepcopy(rubik.face)
    

rubik = cube()    

manualgame()
start = time.time()
autogame()












