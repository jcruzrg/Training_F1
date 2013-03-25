'''
Created on Mar 25, 2013

@author: jc
'''


class MyClass(object):
    '''
    classdocs
    '''


def calculocod(patente, coleccion):
    cont = 0
    suma1 = 0
    suma2 = 0
    while cont < len(patente):
        if (cont % 2) == 0 or cont == 0:
            suma1 = suma1 + int(patente[cont])
        else:
            suma2 = suma2 + int(patente[cont])
        cont = cont + 1
    while suma1 >= 10:
        coleccion = str(suma1)
        suma1 = int(coleccion[0]) + int(coleccion[1])
    while suma2 >= 10:
        coleccion = str(suma2)
        suma2 = int(coleccion[0]) + int(coleccion[1])
    print "Digito Verificador= " + str(suma1) + str(suma2)
