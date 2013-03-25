'''
Created on Mar 22, 2013

@author: jc
'''


import Funciones


coleccion = ""  # Contiene los numeros de las letras
letras = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',\
          'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
diccionario = {'a': '14', 'b': '01', 'c': '00', 'd': '16', 'e': '05',\
               'f': '20', 'g': '19', 'h': '09', 'i': '24', 'j': '07',\
               'k': '21', 'l': '08', 'm': '04', 'n': '13', 'o': '25',\
               'p': '22', 'q': '18', 'r': '10', 's': '02', 't': '06',\
               'u': '12', 'v': '23', 'w': '11', 'x': '03', 'y': '15',\
               'z': '17'}
while True:
    cont = 0
    cont2 = 0
    verificacion = 0
    verificacion2 = 0
    veriftotal = 0
    patente = raw_input("Ingrese el numero de patente")
    if len(patente) <= 9:
        while cont < len(patente):
            while cont2 < 26:
                if letras[cont2] == patente[cont]:
                    veriftotal = veriftotal + 1
                    if cont < 3:  # Verifica los primeros 3 numeros
                        verificacion = verificacion + 1
                        if verificacion == 1 and cont == 0:
                            verificacion2 = 1
                    coleccion = coleccion + diccionario[letras[cont2]]
                cont2 = cont2 + 1
            cont = cont + 1
            cont2 = 0
        if verificacion == 3 and veriftotal == 3:
            verificacion2 = 0
            print "Patente Valida"
            patente = str(coleccion) + str(patente[3:6])
            Funciones.calculocod(patente, coleccion)
            break
        elif verificacion2 == 1 and verificacion == 1 and veriftotal == 1:
            print "Patente Valida"
            patente = str(coleccion) + str(patente[1:len(patente)])
            Funciones.calculocod(patente, coleccion)
            break
        else:
            print "Patente Invalida"
            continue
    else:
        print "Patente Invalida"
        continue
