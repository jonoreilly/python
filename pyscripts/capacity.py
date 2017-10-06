import time

while True:
    #set size of array to measure
    length = int(input("input data size :  "))
    data = []
    for i in range (0, length):
        data.append(0)
    limit = []
    for i in range (0, length):
        limit.append(1)

    #loop through posibilities
    number = 0
    starttime = time.time()
    while data != limit:
            flag = True
            counter = len(data)-1
            print (number, hex(number), data, time.time()-starttime)
            number += 1
            while flag == True:
                    if data[counter] == 0:
                            data[counter] = 1
                            flag = False
                    else:
                            data[counter] = 0
                            counter -= 1
                            if counter < 0:
                                    break
    print (number, hex(number), data)
    print ()
    print(time.time() - starttime, "secs for size", length, "array")
    print()
    
