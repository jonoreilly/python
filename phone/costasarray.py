#-*-coding:utf8;-*-
#qpy:3
#qpy:console

#print("This is console module")





matrix = []


dimension = int(input("matrix dimension :   "))

for i in range (0, dimension):
    matrix.append([])
    for e in range (0, dimension):
        matrix[i].append(0)
        
        
        
matrix [3][6] = "X"
   
for i in range (0, dimension):  
    print(matrix[i])


