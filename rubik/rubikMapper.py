from rubikCubo import cube
import sys
import random
import time
import sqlite3
import json
import colorama

colorama.init()

moves = []
for i in range (0, 6):
    moves.append([i,"a"])
    moves.append([i,"c"])

loadicons = ["-", "\\", "/"]
loader = 0
loads = 0
counter = 0


connection = sqlite3.connect("rubiksql.db")
cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS layouts (
                    layout VARCHAR(90) PRIMARY KEY,
                    lastlayout VARCHAR(90),
                    side INTEGER,
                    direction CHAR,
                    distance INTEGER );""")
connection.commit()
cursor.execute("SELECT * FROM layouts;")
connection.commit()
counter = len(cursor.fetchall())


connectionAcomulador = sqlite3.connect("Acomulador.db")
cursorAcomulador = connectionAcomulador.cursor()
cursorAcomulador.execute("""CREATE TABLE IF NOT EXISTS layouts (
                    layout VARCHAR(90) PRIMARY KEY,
                    lastlayout VARCHAR(90),
                    side INTEGER,
                    direction CHAR,
                    distance INTEGER );""")
connectionAcomulador.commit()


def diferentes ():
    global cursor, connection, counter
    cursor.execute("SELECT distance FROM layouts;")
    connection.commit()
    lineas = cursor.fetchall()
    resultado = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for linea in lineas:
        resultado[linea[0]] += 1
    for i in range(0,len(resultado)):
        if not resultado[i] == 0:
            print(str(i)+": "+str(resultado[i]))
    print(counter)
            

#cool awesome progression bar copied from stackoverflow
def progressBar(posicion):
    global loader, loadicons, loads, counter
    counter += 1
    if loads > 25:
        loads = 0
        if loader > 1:
            loader = 0
        else:
            loader += 1
    else:
        loads += 1

    sys.stdout.write(("\rCounted: {0:>7}        "+colorama.Fore.GREEN+"({1})"+colorama.Style.RESET_ALL+"  "+colorama.Fore.RED+" {2}"+colorama.Style.RESET_ALL).format(counter, loadicons[loader], posicion))
    sys.stdout.flush()


#check if layout is saved in DB, if not it saves it
def dictify(layout, lastlayout, side, direction, distance):
    global cursor
    distanciaGuardada = cursor.execute("SELECT distance FROM layouts WHERE layout=\""+str(layout)+"\";").fetchall()
    if distanciaGuardada == []:
        cursor.execute("""INSERT INTO layouts (layout, lastlayout, side, direction, distance)
                    VALUES (""" +"\""+str(layout)+"\", \""+str(lastlayout)+"\", "+str(side)+", '"+str(direction)+"', "+str(distance)+");")
        connection.commit()
        if cursorAcomulador.execute("SELECT distance FROM layouts WHERE layout=\""+str(layout)+"\";").fetchall() == []:
            cursorAcomulador.execute("""INSERT INTO layouts (layout, lastlayout, side, direction, distance)
                        VALUES (""" +"\""+str(layout)+"\", \""+str(lastlayout)+"\", "+str(side)+", '"+str(direction)+"', "+str(distance)+");")
        else:
            cursorAcomulador.execute("UPDATE layouts SET lastlayout= \""+str(lastlayout)+"\", side = "+str(side)+""",
                        direction = '"""+str(direction)+"', distance = "+str(distance)+" WHERE layout = \""+str(layout)+"\";")
        connectionAcomulador.commit()
        return True
    elif distanciaGuardada[0][0] > distance:
        cursor.execute("UPDATE layouts SET lastlayout= \""+str(lastlayout)+"\", side = "+str(side)+""",
                    direction = '"""+str(direction)+"', distance = "+str(distance)+" WHERE layout = \""+str(layout)+"\";")
        connection.commit()
        if cursorAcomulador.execute("SELECT distance FROM layouts WHERE layout=\""+str(layout)+"\";").fetchall() == []:
            cursorAcomulador.execute("""INSERT INTO layouts (layout, lastlayout, side, direction, distance)
                        VALUES (""" +"\""+str(layout)+"\", \""+str(lastlayout)+"\", "+str(side)+", '"+str(direction)+"', "+str(distance)+");")
        else:
            cursorAcomulador.execute("UPDATE layouts SET lastlayout= \""+str(lastlayout)+"\", side = "+str(side)+""",
                        direction = '"""+str(direction)+"', distance = "+str(distance)+" WHERE layout = \""+str(layout)+"\";")
        connectionAcomulador.commit()
        return True
    else:
        return False
    


#automate the cube's solving
def autogame():
    global moves
    start = time.time()
    rubik = cube()
    follow = True
    if not dictify(rubik.face, "start", 0, 'a',0) and cursorAcomulador.execute("SELECT distance FROM layouts WHERE layout=\""+str(rubik.face)+"\";").fetchall() == []:
            cursorAcomulador.execute("""INSERT INTO layouts (layout, lastlayout, side, direction, distance)
                        VALUES (""" +"\""+str(rubik.face)+"\", \"start\", 0, 'a', 0);")
    while follow:
        result = cursorAcomulador.execute("SELECT * FROM layouts ORDER BY distance ASC LIMIT 1;").fetchall()
        if result == []:
            follow = False
            break
        for move in moves:
            progressBar(result[0][4])
            rubik.setsides(json.loads(result[0][0]))
            rubik.spin(move[0], move[1])
            dictify(rubik.face, json.loads(result[0][0]), move[0], move[1], result[0][4]+1) #if not repeated return True
        cursorAcomulador.execute("DELETE FROM layouts WHERE layout = \""+str(json.loads(result[0][0]))+"\";")
        connectionAcomulador.commit()
    print("Terminado en "+(time.time()-start)+"s")



while True:
    diferentes()
    try:
        autogame()
    except KeyboardInterrupt:
        input("\nSeguro?")
    print("\n\n\n\n\n\n\n")












