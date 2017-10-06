import random
import time

gate = [0,0,0,0,0]

firststate = [0,0,0,0]

#item = [[first],[second],"name",selected]
lever = [[1,0,1,0,0],[0,0,0,1,1],"lever", firststate[0]]
switch = [[0,1,1,0,1],[0,0,0,0,1],"switch", firststate[1]]
valve = [[1,0,1,0,1],[1,1,0,0,0],"valve", firststate[2]]
tele = [[1,0,1,1,0],[1,0,0,0,0],"tele", firststate[3]]

triggers = [lever, switch, valve,tele]

finish = False

database = {}

#results will be dumped here
file = open("borderlands2puzzle.txt","w")


def press(lock, item):
    lastlock = list(lock)
    steped = database[str(lastlock)][0]
    follow = False
    for i in range(0, len(lock)):
        lock[i] += item[item[3]][i]
        if lock[i] > 1:
            lock[i] = 0
    if database[str(lock)] == None:
        database[str(lock)] = [steped+1, lastlock, [item[2], item[3]]]
        follow = True
    elif database[str(lock)][0] > steped+1:
        database[str(lock)] = [steped+1, lastlock, [item[2], item[3]]]
        follow = True
    if item[3]:
        item[3] = 0
    else:
        item[3] = 1
    if lock == database["end"]:
        finish = True
    return [follow, lock]


#make a dictionary of {"[a,r,r,a,y]" : [step, last array, [last switch, shitch cycle]]}
def begindict():
    dictholder = {}
    start = [0,0,0,0,0]
    end = [1,1,1,1,1]
    while start != end:
            flag = True
            counter = len(start)-1
            dictholder[str(start)] = None
            while flag == True:
                    if start[counter] == 0:
                            start[counter] = 1
                            break
                    else:
                            start[counter] = 0
                            counter -= 1
                            if counter < 0:
                                    break
    dictholder[str(start)] = None
    dictholder[str(gate)] = [0,0,0,0]
    dictholder["end"] = [1,1,1,1,1]
    return dictholder


def mainloop():
    global finish
    newcurrent = []
    newcurrent.append(list(gate))
    while finish == False:
        print(newcurrent)
        current = list(newcurrent)
        newcurrent = []
        if current == []:
            break

        for item in current:
            if item == database["end"]:
                finish = True
                break
            for i in range(0, len(triggers)):
                unitholder = list(item)
                whatdo = press(unitholder, triggers[i])
                if whatdo[0]:
                    newcurrent.append(list(whatdo[1]))
                else:
                    print(whatdo[1])
        #time.sleep(1)
        print()
        print()


def ending():
    global finish
    if finish:
        finish = False
        selected = database["end"]
        print("Begining state of lever :  ", firststate[0], ", shitch :  ", firststate[1], "valve :  ", firststate[2])
        file.write("\nBegining state of lever :  "+ str(firststate[0]) +", shitch :  "+ str(firststate[1]) +"valve :  "+ str(firststate[2]))
        while True:
            print(selected, " : ",database[str(selected)][0],"steps with",database[str(selected)][2], ", from :",database[str(selected)][1])
            file.write("\n"+ str(selected)+ " : "+ str(database[str(selected)][0]) +"steps with"+ str(database[str(selected)][2]) +", from :"+ str(database[str(selected)][1]))
            selected = database[str(selected)][1]
            if selected == gate:
                break
    #else:
    for i in range (0, len(firststate)):
        if firststate[i] == 0:
            firststate[i] = 1
            break
        if firststate[i] == 1:
            firststate[i] = 0
    print("Changing firststate to :  ", firststate)
    file.write("\nChanging firststate to :  "+ str(firststate) +"\n\n")
        

def begining():
    global database
    database = begindict()
    global triggers
    for i in range(0,len(triggers)):
        triggers[i][3] = firststate[i]

    
def game():
    while True:
        begining()
        mainloop()
        ending()
        if firststate == [0,0,0,0]:
            print("FAIL")
            break
            
game()
file.close()
    
