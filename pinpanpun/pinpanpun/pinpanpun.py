
txt = {}
for i in range(1, 22) :

    txt [i] = i

txt [7] = "pin"
txt [14] = "pan"
txt [21] = "pun"

players = int(input ("Number of players :    "))

def write (player) : 
   
    for i in range(1, 22) :

        if player == 0 :
            print (txt [i])

        player += 1
    
        if player >= players :
            player = 0


start = 0
while start >= 0  :

    #player is 0
    start = int(input ("Who starts? :    "))

    write(start)

    if input("Add word?(Y/N) :     ") == "Y" :
        txt [int(input("Where? :      "))] = input("What? :     ")





