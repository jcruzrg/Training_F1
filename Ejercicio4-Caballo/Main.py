'''
Created on Apr 5, 2013

@author: jc
'''
matriz = []
cantfilas = 8
cantcolumnas = 8
caballo = True
acuf = 3
acuc = 4
temporalf = 0
temporalc = 0
x1 = 1
x2 = 2
fueradeltablero = False

for i in range(cantfilas):
    matriz.append([False] * cantcolumnas)
matriz[3][4] = caballo
for i in range(cantfilas):
    for j in range(cantcolumnas):
        if acuf >= 0 and acuf <= 7 and acuc >= 0 and acuc <= 7:
            acuf = acuf + x2
            acuc = acuc + x1
            if acuf <= 7 and acuc <= 7:
                matriz[acuf][acuc] = caballo
                temporalc = acuc
                temporalf = acuf
acuc = temporalc
acuf = temporalf
for i in range(cantfilas):
    for j in range(cantcolumnas):
        if acuf >= 0 and acuf <= 7 and acuc >= 0 and acuc <= 7:
            acuf = acuf - x2
            acuc = acuc + x1
            if acuf <= 7 and acuc <= 7:
                matriz[acuf][acuc] = caballo
                temporalc = acuc
                temporalf = acuf
acuc = temporalc
acuf = temporalf
for i in range(cantfilas):
    for j in range(cantcolumnas):
        if acuf >= 0 and acuf <= 7 and acuc >= 0 and acuc <= 7:
            acuf = acuf - x2
            acuc = acuc - x1
            if acuf <= 7 and acuc <= 7:
                matriz[acuf][acuc] = caballo
                temporalc = acuc
                temporalf = acuf
acuc = temporalc
acuf = temporalf
for i in range(cantfilas):
    for j in range(cantcolumnas):
        if acuf >= 0 and acuf <= 7 and acuc >= 0 and acuc <= 7:
            acuf = acuf + x2
            acuc = acuc - x1
            if acuf <= 7 and acuc <= 7:
                matriz[acuf][acuc] = caballo
                temporalc = acuc
                temporalf = acuf
for i in range(cantfilas):
        print matriz[i]

