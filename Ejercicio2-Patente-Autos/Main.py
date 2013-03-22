'''
Created on Mar 22, 2013

@author: jc
'''


cont = 0
cont2 = 0
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
            print diccionario[letras[cont2]]
            coleccion = diccionario[letras[cont2]]
            coleccion2 = coleccion2 + coleccion
            cont2 = cont2 + 1
        cont2 = cont2 + 1
    cont = cont + 1
    cont2 = 0
if verificacion == 3:
    print "patente valida"
else:
    print "patente invalida"

patente = str(coleccion2) + str(patente[3:6])
print patente[0]
# resultado = int(diccionario[patente]) + int(diccionario[patente])
# print resultado
