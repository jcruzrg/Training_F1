'''
Created on Mar 21, 2013

@author: jc
'''


class MyClass(object):
    '''
    classdocs
    '''


def averiguaciondelcuil(codigo, cuilcuit):
    tuplanumeros = 5, 4, 3, 2, 7, 6, 5, 4, 3, 2  # Numerosmultiplicar
    sumar = 0
    multivalor = 0  # Se utiliza para multiplicar la tupla con el dni
    dni = ""   # Limpiar dni
    while True:  # Verificar el Dni o Numero de empresa
        dni = raw_input("Ingrese el dni o el numero de la empresa")
        if len(dni) == 8:
            cuil = codigo + dni
            cuilformato = codigo + "-" + dni
            cont = 0  # Inicializar cont
            dni = codigo + dni  # Dni + codigo de sexo
            try:  # Verifica si en el numero de dni o empresa
                # se ingresaron caracteres no validos
                while cont < len(dni):
                    multivalor = int(dni[cont]) * int(tuplanumeros[cont])
                    sumar = sumar + multivalor
                    cont = cont + 1
                break
            except Exception:
                        pass
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
    if cuilcuit == 0:
        print "Cuit= " + cuilformato
    else:
        print "Cuil= " + cuilformato
