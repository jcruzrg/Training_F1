'''
Created on Mar 21, 2013

@author: jc
'''


import Funciones  # Importar clase

hombremujerempresa = ""  # Limpiar hombremujerempresa
codident = 0  # Limpiar codigo de identificador
verempresa = 1  # Codigo para verificar si es cuil o cuit

print "Hola..."

while True:  # Se verifica si lo que se
            # ingreso es valido y de un solo caracter
    hombremujerempresa = raw_input("Ingrese:\
    \nM si es mujer\nV si es varon\nE si es empresa")

    if len(hombremujerempresa) == 1:
        if hombremujerempresa.lower() == "m":
            codident = "27"
        elif hombremujerempresa.lower() == "v":
            codident = "20"
        elif hombremujerempresa.lower() == "e":
            codident = "30"
            verempresa = 0
        elif hombremujerempresa >= 0:
            print "Error, ingrese lo pedido"
            continue
        break
    print "Error, ingrese lo pedido"

Funciones.averiguaciondelcuil(codident, verempresa)  # Se le pasa el valor
                            # de los 2 primeros numeros de identificacion
