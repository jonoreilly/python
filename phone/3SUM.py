
#-*-coding:utf8;-*-
#qpy:3
#qpy:console

#print("This is console module")



valstr = input ("Input numbers with a space between \n")

save = ""
quit = False
output = {}
outcounter = 0

for counter in range (0, len(valstr)):
    
    if valstr[counter] != " ":
    
        save += valstr[counter]
        
    else:
        
        if save != "":
            
            output[outcounter] = int(save)
            outcounter += 1
            save = ""
                
if save != "":
            
    output[outcounter] = int(save)
    outcounter += 1
    save = ""
                        
                
                
for i in range (0, len(output)):
     
    print (output[i])
    


results = ""


for posa in range(0, len(output)-2) :

    for posb in range(posa+1, len(output)-1) :
    
        for posc in range(posb+1, len(output)) :
        
            if output[posa] + output[posb] + output[posc] == 0 :
            
                results += str(output[posa]) + " + " + str(output[posb]) + " + " + str(output[posc]) + " = 0"
                print (results) 
                results = ""
                
                
for i in range (0, len(results)):

    print (results [i])



