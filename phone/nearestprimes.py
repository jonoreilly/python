#-*-coding:utf8;-*-
#qpy:3
#qpy:console

#print("This is console module")

while True :

    output = "Number "

    
    
    number = int(input("Number :    "))

    output += str(number)
    prime = True
    found = False
    discard = False

    if number > 1 :

        for i in range(2,number) :
            if number % i == 0 :
                prime = False
        if prime :
            output += " is a prime,"

        counter = number -1
        while counter > 1 and not found:
            count = counter - 1
            discard = False
            while not discard and count > 1:
                if counter % count == 0:
                    discard = True
                count -= 1
            if not discard :
                found = True
            else :
                counter -= 1
        if not found :
            output += " has no smaller prime"
        else :
            output += " is closest to "
            output += str(counter)

        found  = False
        counter = number +1
        while not found:
            count = counter -1
            discard = False
            while not discard and count > 1:
                if counter % count == 0:
                    discard = True
                count -= 1
            if not discard :
                found = True
            else :
                counter += 1
    
        output += " and "
        output += str(counter)

        print(output)
    
    else :
        print("invalid number")




