'''
Created on Apr 5, 2013

@author: jc
'''


# Calcula los movimientos posibles desde la posicion del caballo
def alternarmov(movxey, posiactual, matriz):
        movposibles = []
        for i in range(8):
            if (posiactual[0] + movxey[i][0]) in range(8) and (posiactual[1] + movxey[i][1]) in range(8):
                if matriz[posiactual[0] + movxey[i][0]][posiactual[1] + movxey[i][1]] == 0:
                    movimientoscaballo = [posiactual[0] + movxey[i][0], posiactual[1] + movxey[i][1]]
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
for i in range(cantfilas):
        matriz.append([0] * cantcolumnas)
matriz[posiy][posix] = 1

coordenadas.append([posiy, posix])
cantmovposibles = 0
cont3 = 0
while cont3 < 64:
    movimientos = alternarmov(movxey, posiactual, matriz)
    ocuparposicion = buscar_cant_mov(movimientos, matriz, movxey)
    while cont2 < len(ocuparposicion):
        while cont < 1:
            if matriz[ocuparposicion[cont2][cont]][ocuparposicion[cont2][cont + 1]] != 1:
                matriz[ocuparposicion[cont2][cont]][ocuparposicion[cont2][cont + 1]] = 1
                posiactual = [ocuparposicion[cont2][cont], ocuparposicion[cont2][cont + 1]]
                coordenadas.append(posiactual)
                cont2 = (len(ocuparposicion) + 1)
            cont = cont + 1
        cont = 0
        cont2 = cont2 + 1
    cont2 = 0
    cont = 0
    cont3 = cont3 + 1
for i in range(8):
        print matriz[i]
cont = 0
print "Coordenadas: "
while cont < 64:
    print coordenadas[cont]
    cont = cont + 1
