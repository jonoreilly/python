#-*-coding:utf8;-*-
#qpy:3


#print("This is console module")

def write (player) :

    for i in range(1, 22) :
    
        if player == 0 : 
            print (txt[i],txt[i+1])
            
        player += 1
        
        if player >= players :
            player = 0
        
        

txt = {}
txt [22] = ""
for i in range(1, 22) :

    txt [i] = i

txt [7] = "pin"
txt [14] = "pan"
txt [21] = "pun"

players = int (input ("Cuantos juegan?:   ")) - 1


start =0
while start >= 0 :

    start = int (input(" Quien empieza? :   "))
    
    write(start)
    
    if input(" Añadir palabra?(s/n) :   ") != "n" :
        txt [int(input("Donde? :   "))] = input("Que? :   ")
        





