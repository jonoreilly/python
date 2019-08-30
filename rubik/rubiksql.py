from copy import deepcopy
import sys
import random
import time
import sqlite3



file = open("rubiksolver.txt","w")

endlayout = [[[0,0,0],[0,0,0],[0,0,0]],
            [[1,1,1],[1,1,1],[1,1,1]],
            [[2,2,2],[2,2,2],[2,2,2]],
            [[3,3,3],[3,3,3],[3,3,3]],
            [[4,4,4],[4,4,4],[4,4,4]],
            [[5,5,5],[5,5,5],[5,5,5]]]
#dicti = {}
startlayout = []
moves = []
for i in range (0, 6):
    moves.append([i,"a"])
    moves.append([i,"c"])

loadicons = ["-", "\\", "/"]
loader = 0
loads = 0

connection = sqlite3.connect("company.db")
cursor = connection.cursor()

try:
    cursor.execute("DROP TABLE layouts;")
    
except:
    pass
    
cursor.execute("""CREATE TABLE layouts (
                    layout VARCHAR(90) PRIMARY KEY,
                    lastlayout VARCHAR(90),
                    side INTEGER,
                    direction CHAR );""")



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


#check if layout is saved in dict, if not it saves it
def dictify(layout, lastlayout, side, direction):
    global cursor
    
    if cursor.execute("SELECT * FROM layouts WHERE layout=\""+str(layout)+"\"").fetchall() == []:
        cursor.execute("""INSERT INTO layouts (layout, lastlayout, side, direction)
                    VALUES (""" +"\""+str(layout)+"\", \""+str(lastlayout)+"\", "+str(side)+", '"+str(direction)+"');")
        return True
    
    else:
        return False
    
    


#cool awesome progression bar copied from stackoverflow
def progressBar(value, endvalue, bar_length=20):
        global loader, loadicons, loads
        percent = float(value) / endvalue
        arrow = '-' * int(round(percent * bar_length)-1) + '>'
        spaces = ' ' * (bar_length - len(arrow))
        
        if loads > 25:
            loads = 0
            if loader > 1:
                loader = 0
            else:
                loader += 1
        else:
            loads += 1

        sys.stdout.write("\rPercent: [{0}] {1:2}% ({2})".format(arrow + spaces, int(round(percent * 100)), loadicons[loader]))
        sys.stdout.flush()
       

def randomize():
    moves = random.randint(10, 20)
    print("\nRRRRRRRRRANDOM  ",moves,"moves")
    global rubik
    for i in range (0, moves):
        if random.randint(0,1):
            letra = "c"
        else:
            letra = "a"
        rubik.spin(random.randint(0, 5),letra)
    rubik.printface()


#automate the cube's solving
def autogame():
    global rubik, endlayout, startlayout, file, start
    finish = False
    countar = 1
    newlist = [deepcopy(startlayout)]
    dictify (newlist[0], "start", 100, 'x')
    #reload the layout list with the next batch
    while finish == False:
        mainlist = deepcopy(newlist)
        newlist = []
        if mainlist == []:
            print("u ran out of layouts, mate")
            break
        print(countar, len(mainlist),"\n")
        countar += 1
        counter = 0
        #select a layout to move
        for item in mainlist:
            progressBar(counter, len(mainlist), 50)
            counter += 1
            if item == endlayout:
                finish = True
                break
            #move, check and save that layout 
            for move in moves:
                rubik.setsides(deepcopy(item))
                rubik.spin(move[0], move[1])
                follow = dictify(rubik.face, item, move[0], move[1]) #if not repeated return True
                if follow:
                    newlist.append(deepcopy(rubik.face))
                    if rubik.face == endlayout:
                        finish = True
                        break
            if finish:
                break
        print()
        print()

    #calculate the route and display/save it
    if finish:
        selected = endlayout
        output = []
        print("\nResults :")
        while True:

            output.append(cursor.execute("SELECT * FROM layouts WHERE layout=\""+str(selected)+"\"").fetchall()[0][2:4])
            #output.append([dicti[str(selected)][1],dicti[str(selected)][2]])

            selected = cursor.execute("SELECT * FROM layouts WHERE layout=\""+str(selected)+"\"").fetchall()[0][1]
            #selected = dicti[str(selected)][0]
            
            if selected == str(startlayout):
                holder = []
                for i in range(0, len(output)):
                    holder.append(output[i])
                file.write(str(holder))
                file.write("\n"+str(time.time()-start))
                print(time.time()-start)
                print(holder)
                file.close()
                break

                       
#set the cube layout from begining with inputs
def manualgame():
    global rubik, startlayout
    while True:
        rubik.printface()
        #if input isnt int then Break out and begin autosolving
        value = input("What side do u wanna turn? S to start, R to randomize -> ")
        try:
            side = int(value)
        except ValueError:
            if value == "r" or value == "R":
                randomize()
            break
        direction = input("Clockways (C) or Anticlockways (A)?  -> ")
        rubik.spin(side, direction)
    startlayout = deepcopy(rubik.face)
    

rubik = cube()    


#main script
manualgame()
start = time.time()
autogame()












