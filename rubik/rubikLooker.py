import sqlite3
import sys
import colorama

connection = sqlite3.connect("rubiksql.db")
cursor = connection.cursor()
colorama.init()



def selectTop (cantidad = 10, direction = "ASC", campos = "*"):
    global cursor, connection
    cursor.execute("SELECT "+campos+" FROM layouts ORDER BY distance "+
                   direction+" LIMIT "+str(cantidad)+";")
    connection.commit()
    return cursor.fetchall()

def getCantidad ():
    global cursor, connection
    cursor.execute("SELECT * FROM layouts;")
    connection.commit()
    return len(cursor.fetchall())

def diferentes ():
    global cursor, connection
    cursor.execute("SELECT distance FROM layouts;")
    connection.commit()
    lineas = cursor.fetchall()
    resultado = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for linea in lineas:
        resultado[linea[0]] += 1
    for i in range(0,len(resultado)):
        if not resultado[i] == 0:
            print(str(i)+": "+str(resultado[i]))
        
def acomulador():
    global connection, cursor
    connection = sqlite3.connect("Acomulador.db")
    cursor = connection.cursor()

def rubiksql():
    global connection, cursor
    connection = sqlite3.connect("rubiksql.db")
    cursor = connection.cursor()

def clearAll():
    global connection, cursor
    acomulador()
    cursor.execute("DROP TABLE layouts;")
    connection.commit()
    rubiksql()
    cursor.execute("DROP TABLE layouts;")
    connection.commit()

def help():
    print(colorama.Fore.GREEN+"rubiksql()                                                      "+
            colorama.Fore.WHITE+"Cambiar base de datos a rubiksql.db")
    print(colorama.Fore.GREEN+"acomulador()                                                    "+
            colorama.Fore.WHITE+"Cambiar base de datos a Acomulador.db")
    print(colorama.Fore.GREEN+"diferentes()                                                    "+
            colorama.Fore.WHITE+"Muestra la cantidad de cada distancia")
    print(colorama.Fore.GREEN+"getCantidad()                                                   "+
            colorama.Fore.WHITE+"Muestra la cantidad total en la BD")
    print(colorama.Fore.GREEN+"selectTop(cantidad = 10, direction = 'ASC', campos = '*')       "+
            colorama.Fore.WHITE+"Muestra la cantidad total en la BD")
    print(colorama.Fore.GREEN+"clearAll()                                                      "+
            colorama.Fore.WHITE+"DROP TABLES")

def quit():
    print("Agur")
    sys.exit(0)

def main ():
    global connection, cursor
    while True:
        exec(input("<rubikLooker:#>"))       
        

main()