#-*-coding:utf8;-*-
#qpy:3
#qpy:console

#print("This is console module")


number = 2

while True:

    counter = 2
    discard = False
    
    while counter < number and not discard:

        if number % counter == 0:
            discard = True
            
        counter += 1
    
    if not discard :
        
        print (number)
        
    number += 1





