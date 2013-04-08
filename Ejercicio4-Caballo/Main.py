'''
Created on Apr 5, 2013

@author: jc
'''
dir = {'00': 34, '01': 37, '02': 26, '03': 29, '04': 32, '05': 43, '06': 48,\
       '07': 45, '10': 25, '11': 30, '12': 33, '13': 36, '14': 27, '15': 46,\
       '16': 51, '17': 42, '20': 38, '21': 35, '22': 28, '23': 31, '24': 40,\
       '25': 49, '26': 44, '27': 47, '30': 7, '31': 24,  '32': 39, '33': 18,\
       '34': 1, '35': 52, '36': 41, '37': 50, '40': 14, '41': 19, '42': 8,\
       '43': 23, '44': 12, '45': 55, '46': 64, '47': 53, '50': 9, '51': 6,\
       '52': 13, '53': 2, '54': 17, '55': 58, '56': 61, '57': 56, '60': 20,\
       '61': 15, '62': 4, '63': 11, '64': 22, '65': 63, '66': 54, '67': 59,\
       '70': 5, '71': 10, '72': 21, '73': 16, '74': 3, '75': 60, '76': 57,\
       '77': 62}
matriz = []
cantfilas = 8
cantcolumnas = 8
posix = 0  # Posicion del caballo en x
posiy = 0  # Posicion del caballo en y
cont = 0
coordenada = ""
lista = []
while True:
    posix = int(raw_input("Ingrese posicion en x(>= 0 y <= 7): "))
    if posix >= 0 and posix <= 7:
        break
while True:
    posiy = int(raw_input("Ingrese posicion en y(>= 0 y <= 7): "))
    if posiy >= 0 and posiy <= 7:
        break
for i in range(cantfilas):
    matriz.append([0] * cantcolumnas)
matriz[posiy][posix] = 1
comienzo = dir[(str(posiy) + str(posix))]
while cont < 64:
    for i in range(cantfilas):
        for j in range(cantcolumnas):
            seguido = (str(i) + str(j))
            if dir[seguido] == (comienzo + 1):
                if matriz != 1:
                    lista.append((str(i) + str(j)))
                    coordenada = coordenada + str(i) + "-" + str(j) + ", "
                    matriz[i][j] = 1
                    comienzo = comienzo + 1
                    print matriz[i]
            if comienzo == 64:
                comienzo = 0
    cont = cont + 1
print coordenada
print
print
print lista
