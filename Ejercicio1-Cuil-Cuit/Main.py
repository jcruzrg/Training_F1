'''
Created on Mar 21, 2013

@author: jc
'''
import Funciones
hombremujerempresa = "" #Limpiar hombremujerempresa
codident = 0 #Limpiar codigo de identificador

print "Hola..."
hombremujerempresa = raw_input("Ingrese:\nM si es mujer\nV si es varon\nE si es empresa")
if hombremujerempresa == "M" or hombremujerempresa == "m":
    codident = "27"
elif hombremujerempresa == "V" or hombremujerempresa == "v":
    codident = "20"
elif hombremujerempresa == "E" or hombremujerempresa == "e":
    codident = "30"
cuil = codident
Funciones.valor1(codident)


