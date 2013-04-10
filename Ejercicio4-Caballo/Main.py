'''
Created on Apr 5, 2013

@author: jc
'''


# Calcula los movimientos posibles desde la posicion del caballo
def alternarmov(movxey, posiactual, matriz):
        movposibles = []
        # Con if (posiactual[0] + movxey[i][0]) in range(8) and (posiactual[1] + movxey[i][1]) in range(8):
        # Me ahorro de escribir if (posiactual[0] + movxey[i][0]) < 8 and (posiactual[1] + movxey[i][1]) < 8
        # and (posiactual[0] + movxey[i][0]) >= 0 and (posiactual[1] + movxey[i][1]) >= 0:
        for i in range(8):
            # Comprueba si el movimiento esta dentro del tablero
            if (posiactual[0] + movxey[i][0]) in range(8) and (posiactual[1] + movxey[i][1]) in range(8):
                # Comprueba si la posicion dentro del tablero fue tocada
                if matriz[posiactual[0] + movxey[i][0]][posiactual[1] + movxey[i][1]] == 0:
                    # Obtiene la coordenada del movimiento posible
                    movimientoscaballo = [posiactual[0] + movxey[i][0], posiactual[1] + movxey[i][1]]
                    # Se agregan las coordenadas no tocadas dentro del rango de
                    # la lista de movimientos posibles
                    movposibles.append(movimientoscaballo)
        return movposibles


# Busca la cantidad de movimientos posibles del caballo
# y calcula la catidad de movimientos posibles desde la
# lista de posiciones de la funcion "def posibles"
def buscar_cant_mov(movimientos, matriz, movxey):
    cantposiciones = []
    for i in range(len(movimientos)):
        posiciones = len(alternarmov(movxey, movimientos[i], matriz))
        cantposiciones.append(posiciones)
    return probabilidad_menor_mayor(cantposiciones, movimientos)


# Con la cantidad de movimientos posibles de cada
# movimiento posible, los ordena de menor cantidad de
# movimiento a mayor cantidad de movimientos
def probabilidad_menor_mayor(listcantmov, listposmov):
    for i in range(len(listcantmov)):
        for j in range(len(listcantmov) - 1):
            if listcantmov[j] > listcantmov[j + 1]:
                listposmov[j], listposmov[j + 1] = listposmov[j + 1], listposmov[j]
                listcantmov[j], listcantmov[j + 1] = listcantmov[j + 1], listcantmov[j]
    return listposmov
matriz = []
cantfilas = 8
cantcolumnas = 8
# Combinacion de movimientos en "y" e "x" posibles
movxey = [[2, 1], [1, 2], [-2, 1], [2, -1], [-1, 2], [1, -2], [-2, -1], [-1, -2]]
posiy = 0
posix = 0
cont = 0
cont2 = 0
coordenadas = []
print "Ingrese la posicion inical del caballo: "
while True:
    posiy = int(raw_input("Eje y(>= 0 y <= 7): "))
    if posiy >= 0 and posiy <= 7:
        break
while True:
    posix = int(raw_input("Eje x(>= 0 y <= 7): "))
    if posix >= 0 and posix <= 7:
        break
posiactual = [posiy, posix]
# Crea el tablero e inicia las posiciones en "0" = No tocadas
for i in range(cantfilas):
        matriz.append([0] * cantcolumnas)
matriz[posiy][posix] = 1  # Se toca la posicion escojida
coordenadas.append([posiy, posix])  # Agrega coordenada inicial
cantmovposibles = 0
cont3 = 0
while cont3 < 64:  # Se ejecuta hasta agotar los 63 movimientos
    movimientos = alternarmov(movxey, posiactual, matriz)
    ocuparposicion = buscar_cant_mov(movimientos, matriz, movxey)
    while cont2 < len(ocuparposicion):
        while cont < 1:
            # Comprueba si la posicion elejida fue tocada, si no fue
            # tocada, la toca
            if matriz[ocuparposicion[cont2][cont]][ocuparposicion[cont2][cont + 1]] != 1:
                matriz[ocuparposicion[cont2][cont]][ocuparposicion[cont2][cont + 1]] = 1
                posiactual = [ocuparposicion[cont2][cont], ocuparposicion[cont2][cont + 1]]
                # Agrega la coordenadas de las posiciones tocadas
                coordenadas.append(posiactual)
                cont2 = (len(ocuparposicion) + 1)
            cont = cont + 1
        cont = 0
        cont2 = cont2 + 1
    cont2 = 0
    cont = 0
    cont3 = cont3 + 1
for i in range(8):  # Muestra el tablero completo
        print matriz[i]
cont = 0
print "Coordenadas: "
while cont < 64:
    print coordenadas[cont]
    cont = cont + 1
