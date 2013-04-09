'''
Created on Apr 5, 2013

@author: jc
'''
import random


def moviminetos(random):
    global tempy, tempx, movy, movx, posix, posiy
    if random == 0:  # Movimiento en "y-1", "x-2"
        posiy = posiy - movy1
        posix = posix - movx2
    if random == 1:  # Movimiento en "y-1", "x+2"
        posiy = posiy - movy1
        posix = posix + movx2
    if random == 2:  # Movimiento en "y-2", "x+1"
        posiy = posiy - movy2
        posix = posix + movx1
    if random == 3:  # Movimiento en "y-2", "x-1"
        posiy = posiy - movy2
        posix = posix - movx1
    if random == 4:  # Movimiento en "y+1", "x-2"
        posiy = posiy + movy1
        posix = posix - movx2
    if random == 5:  # Movimiento en "y+1", "x+2"
        posiy = posiy + movy1
        posix = posix + movx2
    if random == 6:  # Movimiento en "y+2", "x-1"
        posiy = posiy + movy2
        posix = posix - movx1
    if random == 7:  # Movimiento en "y+2", "x+1"
        posiy = posiy + movy2
        posix = posix + movx1


def limpiarvariables():
    global matriz, posix, posiy, tempx, tempy, coordenadas, posiciones, \
    posibilidades, lista, seguir, intentando, comienzox, comienzoy
    matriz = []
    posix = comienzox
    posiy = comienzoy
    tempy = 0  # Captura la posicion del caballo en y temporalmente
    tempx = 0  # Captura la posicion del caballo en x temporalmente
    coordenadas = []
    posiciones = ""
    posibilidades = 0
    lista = []
    seguir = 1
    intentando = 1
    for i in range(cantfilas):
        matriz.append([0] * cantcolumnas)
    matriz[posiy][posix] = 1


def mostrartablero():
    global coordenadas, comienzox, comienzoy
    print
    print "Posicion inicial: " + "y(" + str(comienzoy) + ")" + " "\
    + "x(" + str(comienzox) + ")"
    print "Mayor cantidad de movimientos: " + str(len(coordenadas))
    print "Coordenadas: " + str(coordenadas)
    for i in range(cantfilas):
            print matriz[i]


def izqarriba():
    global posiy, posix, matriz
    if posiy == 2 and posix == 1 and matriz[1][2] != 1:
        posiy = posiy - movy2
        posix = posix - movx1
        matriz[posiy][posix] = 1
        aniadircoordenada()
    if posiy == 1 and posix == 2 and matriz[2][1] != 1:
        posiy = posiy - movy1
        posix = posix - movx2
        matriz[posiy][posix] = 1
        aniadircoordenada()


def izqabajo():
    global posiy, posix, matriz
    if posiy == 5 and posix == 1 and matriz[6][2] != 1:
        posiy = posiy + movy2
        posix = posix - movx1
        matriz[posiy][posix] = 1
        aniadircoordenada()
    if posiy == 6 and posix == 2 and matriz[5][1] != 1:
        posiy = posiy + movy1
        posix = posix - movx2
        matriz[posiy][posix] = 1
        aniadircoordenada()


def derarriba():
    global posiy, posix, matriz
    if posiy == 2 and posix == 6 and matriz[1][5] != 1:
        posiy = posiy - movy2
        posix = posix + movx1
        matriz[posiy][posix] = 1
        aniadircoordenada()
    if posiy == 1 and posix == 5 and matriz[2][6] != 1:
        posiy = posiy - movy1
        posix = posix + movx2
        matriz[posiy][posix] = 1
        aniadircoordenada()


def derabajo():
    global posiy, posix, matriz
    if posiy == 6 and posix == 5 and matriz[5][6] != 1:
        posiy = posiy + movy1
        posix = posix + movx2
        matriz[posiy][posix] = 1
        aniadircoordenada()
    if posiy == 5 and posix == 6 and matriz[6][5] != 1:
        posiy = posiy + movy2
        posix = posix + movx1
        matriz[posiy][posix] = 1
        aniadircoordenada()


def izqarriba2():
    global posiy, posix, matriz
    if posiy == 2 and posix == 0 and matriz[0][1] != 1:
        posiy = posiy - movy2
        posix = posix + movx1
        matriz[posiy][posix] = 1
        aniadircoordenada()
    if posiy == 2 and posix == 2 and matriz[0][1] != 1:
        posiy = posiy - movy2
        posix = posix - movx1
        matriz[posiy][posix] = 1
        aniadircoordenada()
    if posiy == 1 and posix == 3 and matriz[0][1] != 1:
        posiy = posiy - movy1
        posix = posix - movx2
        matriz[posiy][posix] = 1
        aniadircoordenada()


def izqarriba3():
    global posiy, posix, matriz
    if posiy == 2 and posix == 2 and matriz[1][0] != 1:
        posiy = posiy - movy1
        posix = posix - movx2
        matriz[posiy][posix] = 1
        aniadircoordenada()
    if posiy == 3 and posix == 1 and matriz[1][0] != 1:
        posiy = posiy - movy2
        posix = posix - movx1
        matriz[posiy][posix] = 1
        aniadircoordenada()
    if posiy == 0 and posix == 2 and matriz[1][0] != 1:
        posiy = posiy + movy1
        posix = posix - movx2
        matriz[posiy][posix] = 1
        aniadircoordenada()


def izqabajo2():
    global posiy, posix, matriz
    if posiy == 7 and posix == 2 and matriz[6][0] != 1:
        posiy = posiy - movy1
        posix = posix - movx2
        matriz[posiy][posix] = 1
        aniadircoordenada()
    if posiy == 5 and posix == 2 and matriz[6][0] != 1:
        posiy = posiy + movy1
        posix = posix - movx2
        matriz[posiy][posix] = 1
        aniadircoordenada()
    if posiy == 4 and posix == 1 and matriz[6][0] != 1:
        posiy = posiy + movy2
        posix = posix - movx1
        matriz[posiy][posix] = 1
        aniadircoordenada()


def izqabajo3():
    global posiy, posix, matriz
    if posiy == 5 and posix == 0 and matriz[7][1] != 1:
        posiy = posiy + movy2
        posix = posix + movx1
        matriz[posiy][posix] = 1
        aniadircoordenada()
    if posiy == 5 and posix == 2 and matriz[7][1] != 1:
        posiy = posiy + movy2
        posix = posix - movx1
        matriz[posiy][posix] = 1
        aniadircoordenada()
    if posiy == 6 and posix == 3 and matriz[7][1] != 1:
        posiy = posiy - movy1
        posix = posix - movx2
        matriz[posiy][posix] = 1
        aniadircoordenada()


def derarriba2():
    global posiy, posix, matriz
    if posiy == 2 and posix == 7 and matriz[0][6] != 1:
        posiy = posiy - movy2
        posix = posix - movx1
        matriz[posiy][posix] = 1
        aniadircoordenada()
    if posiy == 2 and posix == 5 and matriz[0][6] != 1:
        posiy = posiy - movy2
        posix = posix + movx1
        matriz[posiy][posix] = 1
        aniadircoordenada()
    if posiy == 1 and posix == 4 and matriz[0][6] != 1:
        posiy = posiy - movy1
        posix = posix + movx2
        matriz[posiy][posix] = 1
        aniadircoordenada()


def derarriba3():
    global posiy, posix, matriz
    if posiy == 2 and posix == 5 and matriz[1][7] != 1:
        posiy = posiy - movy1
        posix = posix + movx2
        matriz[posiy][posix] = 1
        aniadircoordenada()
    if posiy == 0 and posix == 5 and matriz[1][7] != 1:
        posiy = posiy + movy1
        posix = posix + movx2
        matriz[posiy][posix] = 1
        aniadircoordenada()
    if posiy == 3 and posix == 6 and matriz[1][7] != 1:
        posiy = posiy - movy2
        posix = posix + movx1
        matriz[posiy][posix] = 1
        aniadircoordenada()


def derabajo2():
    global posiy, posix, matriz
    if posiy == 5 and posix == 5 and matriz[7][6] != 1:
        posiy = posiy + movy2
        posix = posix + movx1
        matriz[posiy][posix] = 1
        aniadircoordenada()
    if posiy == 5 and posix == 7 and matriz[7][6] != 1:
        posiy = posiy + movy2
        posix = posix - movx1
        matriz[posiy][posix] = 1
        aniadircoordenada()
    if posiy == 6 and posix == 4 and matriz[7][6] != 1:
        posiy = posiy + movy1
        posix = posix + movx2
        matriz[posiy][posix] = 1
        aniadircoordenada()


def derabajo3():
    global posiy, posix, matriz
    if posiy == 7 and posix == 5 and matriz[6][7] != 1:
        posiy = posiy - movy1
        posix = posix + movx2
        matriz[posiy][posix] = 1
        aniadircoordenada()
    if posiy == 5 and posix == 5 and matriz[6][7] != 1:
        posiy = posiy + movy1
        posix = posix + movx2
        matriz[posiy][posix] = 1
        aniadircoordenada()
    if posiy == 4 and posix == 6 and matriz[6][7] != 1:
        posiy = posiy + movy2
        posix = posix + movx1
        matriz[posiy][posix] = 1
        aniadircoordenada()


def aniadircoordenada():
    global posiciones, coordenadas, posiy, posix
    # Obtiene las coordenadas en "y" y en "x"
    posiciones = (str(posiy) + "-" + str(posix))
    # Acumula las coordenadas en una tupla
    coordenadas.append(posiciones)


matriz = []
cantfilas = 8
cantcolumnas = 8
posix = 0  # Posicion del caballo en x
posiy = 0  # Posicion del caballo en y
tempy = 0  # Captura la posicion del caballo en y temporalmente
tempx = 0  # Captura la posicion del caballo en x temporalmente
comienzoy = 0  # Captura el comienzo del caballo en y
comienzox = 0  # Captura el comienzo del caballo en x
coordenadas = []  # Guarda todo los movimientos en coordenadas de y e x
posiciones = ""  # Obtiene las posiciones temporalmente
posibilidades = 0
movy1 = 1  # Movimiento en "y (+)(-) 1"
movy2 = 2  # Movimiento en "y (+)(-) 2"
movx1 = 1  # Movimiento en "x (+)(-) 1"
movx2 = 2  # Movimiento en "x (+)(-) 2"
seguir = 1
intentando = 1
print "Ingrese la posicion inical del caballo: "
while True:
    posiy = int(raw_input("Eje y(>= 0 y <= 7): "))
    if posiy >= 0 and posiy <= 7:
        break
while True:
    posix = int(raw_input("Eje x(>= 0 y <= 7): "))
    if posix >= 0 and posix <= 7:
        break
comienzoy = posiy  # Obtiene la posicion inicial en "y"
comienzox = posix  # Obtiene la posicion inicial en "x"
while intentando != 0:
    # Limitar cantidad maxima de movimientos, la cual promedia los 55
    # movimientos en la mayoria de los casos. Hay que mejorar el algoritmo!!!
    if len(coordenadas) <= 55:
        limpiarvariables()
    else:
        intentando = 0
    for i in range(cantfilas):
        for j in range(cantcolumnas):
            while seguir != 0:
                tempy = posiy
                tempx = posix
                # Analiza las puntas, si esta en las posiciones en las
                # solo se pueden tocar
                izqarriba2()
                izqabajo2()
                derarriba2()
                derabajo2()
                izqarriba3()
                izqabajo3()
                derarriba3()
                derabajo3()
                izqarriba()
                izqabajo()
                derarriba()
                derabajo()
                tempy = posiy
                tempx = posix
                # Envia aleatoriamente el movimiento que
                # debe hacer el caballo entre el 0 y el 7
                moviminetos(random.randint(0, 7))
                # Analiza si el movimiento esta dentro o fuera del tablero
                if posiy <= 7 and posiy >= 0 and posix <= 7 and posix >= 0:
                    # Analiza si la posicion elejida ya fue tocada
                    if matriz[posiy][posix] != 1:
                        # Toca posicion en el tablero
                        matriz[posiy][posix] = 1
                        aniadircoordenada()
                        posibilidades = 0
                    # Si fue tocada vuelve a tomar la posicion anterior y
                    # sigue intentando
                    else:
                        posiy = tempy
                        posix = tempx
                        if posibilidades < 8:
                            seguir = 1
                        else:
                            seguir = 0
                # Cuando el movimiento esta fuera del tablero
                # vuelve a tomar la posicion anterior y sigue intentando
                else:
                    posiy = tempy
                    posix = tempx
                    # Acumula las cantidad de posibilidades que uso,
                    # como son 8 posibilidades, si las supera termina
                    # de intentar. Por que no le queda mas movimientos
                    posibilidades = posibilidades + 1
                    seguir = 1
mostrartablero()
