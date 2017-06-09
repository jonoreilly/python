def BtoD(binstr):

    print(int(binstr,2))

def DtoB(decint):

    x = bin(int(decint))
    p = ""

    for y in range(len(x), 10):
        p += "0"

    for i in range(0, len(x)-len(p)-1):
        p += x[i+2]

    print(p)



answer = input("Select your choice:\n 0.Binary to Decimal\n 1.Decimal to Binary\n>>")

if answer == "0":
    BtoD(input("\nType the Binary:\n>>"))

elif answer == "1":
    DtoB(input("\nType the Decimal:\n>>"))

else:
    print("Error")
