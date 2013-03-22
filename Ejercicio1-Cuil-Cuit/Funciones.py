'''
Created on Mar 21, 2013

@author: jc
'''

class MyClass(object):
    '''
    classdocs
    '''
def valor1(codigo):
    tuplanumeros = 5,4,3,2,7,6,5,4,3,2 #Tupla con numeros a multiplicar
    sumar = 0
    multivalor = 0
    dni = "" #Limpiar dni
    
    while True: #Verificar el Dni o Numero de empresa
        dni = raw_input("Ingrese el dni o el numero de la empresa")
        if len(dni) == 8:
            cuil = codigo + dni
            cuilformato = codigo + "-" + dni
            cont = 0 #Inicializar cont
            dni = codigo + dni #Dni + codigo de sexo
            while cont < len(dni):   
                multivalor = int(dni[cont]) * int(tuplanumeros[cont])
                sumar = sumar + multivalor
                cont = cont + 1
            break
        print "Error al ingresar Dni"
        print ""
            
    division = sumar % 11    
    codverificador = 11 - division
    if codverificador == 10:
        codverificador = 9
    elif codverificador == 11:
        codverificador = 0
    cuilformato = cuilformato + "-" + str(codverificador)
    cuil = cuil + str(codverificador)
    print "Cuil= " + cuilformato    
