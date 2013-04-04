'''
Created on Mar 28, 2013

@author: jc
'''
from MainZoDb import Manejo_Db
import Visual
import FuncionBotones
import thread
import time


cont = 0
borrar = 0
aculetras = ""  # Acumula las letras
                # para buscar sugerencias
frase = ""  # Va armando la oracion
codigo = ""  # Captura los numeros
tiempo = 1.3  # Es en segundos para darle tiempo al usuario
            # a pulsar los numeros
codigototal = ""  # Saca el codigo de las palabra formada


def capturar(event):
    global codigo, cont, codigototal
    cont = cont + 1
    print "Evento: " + str(event)
    codigo = codigo + str(event)


def escribirdatos(hilo1, espera):
    global aculetras, codigo, cont, frase, borrar, codigototal
    while 1:
        if cont != 0 and codigo != "1":
            Visual.cartel2.set("Escribiendo...")
            # Espera cierto tiempo hasta que el usuario deje de escribir
            time.sleep(espera)
            codigototal = codigototal + codigo
            print "Codigo= " + str(codigototal)
            Visual.cartel2.set("Escribe")
            try:
                db = Manejo_Db('Dataprueba.fs')
                dbroot = db.dbroot
                codletra = dbroot['codletra']
                aculetras = aculetras + codletra[codigo]
                db.close()
                if borrar == 1:
                    borrar = 0
                    frase = str(Visual.oracion.get(0))
                    print "Aculetras try: " + str(Visual.oracion.get(0)) + aculetras
            except:
                aculetras = ""
                cont = 0
            if codigo == '#':
                frase = frase + "" + aculetras
                aculetras = ""
                print codigo
                codigo = ""
                codigototal = ""
                while Visual.listasugerencias.size() > 0:
                    Visual.listasugerencias.delete(0)
            cont = 0
            codigo = ""
            print "Oracion: " + frase + aculetras
            Visual.oracion.delete(0)
            Visual.oracion.insert(0, (frase + aculetras))
            print "Aculetras: " + aculetras
            if len(aculetras) >= 1:
                FuncionBotones.analizar_sugerencia(aculetras)

try:
    # Thread inicia la funcion escribirdatos
    thread.start_new_thread(escribirdatos, ("Thread-1", tiempo, ))
except:
    print "Error"
