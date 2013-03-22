'''
Created on Mar 22, 2013

@author: jc
'''


cont = 0
cont2 = 0
suma1 = 0
suma2 = 0
verificacion = 0
coleccion = ""
coleccion2 = ""
letras = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',\
          'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
diccionario = {'a': '14', 'b': '01', 'c': '00', 'd': '16', 'e': '05',\
               'f': '20', 'g': '19', 'h': '09', 'i': '24', 'j': '07',\
               'k': '21', 'l': '08', 'm': '04', 'n': '13', 'o': '25',\
               'p': '22', 'q': '18', 'r': '10', 's': '02', 't': '06',\
               'u': '12', 'v': '23', 'w': '11', 'x': '03', 'y': '15',\
               'z': '17'}

patente = raw_input("Ingrese el numero de patente")
while cont < 3:
    while cont2 < 26:
        if letras[cont2] == patente[cont]:
            verificacion = verificacion + 1
            coleccion = diccionario[letras[cont2]]
            coleccion2 = coleccion2 + coleccion
            cont2 = cont2 + 1
        cont2 = cont2 + 1
    cont = cont + 1
    cont2 = 0
if verificacion == 3:
    print "patente valida"
    patente = str(coleccion2) + str(patente[3:6])
else:
    print "patente invalida"
    coleccion = ""
    coleccion2 = ""
    cont = 0
    cont2 = 0
    while cont < 1:
        while cont2 < 26:
            if letras[cont2] == patente[cont]:
                verificacion = verificacion + 1
                coleccion = diccionario[letras[cont2]]
                coleccion2 = coleccion2 + coleccion
                cont2 = cont2 + 1
            cont2 = cont2 + 1
        cont = cont + 1
        cont2 = 0
        patente = str(coleccion2) + str(patente[1:len(patente)])
    cont = 0
    while cont < len(patente):
        if (cont % 2) == 0 or cont == 0:
            suma1 = suma1 + int(patente[cont])
        else:
            suma2 = suma2 + int(patente[cont])
        cont = cont + 1
    while suma1 >= 10:
        coleccion2 = str(suma1)
        suma1 = int(coleccion2[0]) + int(coleccion2[1])
    while suma2 >= 10:
        coleccion = str(suma2)
        suma2 = int(coleccion[0]) + int(coleccion[1])
    print "Codigo= " + str(suma1) + str(suma2)
# resultado = int(diccionario[patente]) + int(diccionario[patente])
# print resultado
