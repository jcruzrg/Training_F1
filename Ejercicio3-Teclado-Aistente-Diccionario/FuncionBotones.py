'''
Created on Mar 28, 2013

@author: jc
'''
from Tkinter import *
from MainZoDb import Manejo_Db, transaction
import tkMessageBox
import Visual
import Main


class MyClass(object):
    '''
    classdocs
    '''


def agregar_sugerencia(e):
    posicion = str(Visual.listasugerencias.curselection())
    palabrasugerida = str(Visual.listasugerencias.get(posicion[2]))
    Main.frase = Main.frase + "" + palabrasugerida
    Visual.oracion.delete(0)
    Visual.oracion.insert(0, (Main.frase))
    while Visual.listasugerencias.size() > 0:
        Visual.listasugerencias.delete(0)
    Main.cont = 0
    Main.aculetras = ""
    Main.codigo = ""


def analizar_sugerencia(aculetras):
    lista1 = []
    lista2 = []
    palabraa = ""
    i = 0
    j = 0
    k = 0
    w = 0
    db = Manejo_Db('Dataprueba.fs')
    dbroot = db.dbroot
    palabras = dbroot['palabras']
    for x in palabras:
        if palabras[x].find(aculetras) >= 0:
            lista1.append(palabras[x])
            i = i + 1
    while j < i:
        palabraa = str(lista1[j])
        if len(aculetras) == 1:
            if palabraa[len(aculetras) - 1] == aculetras:
                lista2.append(palabraa)
                w = w + 1
        else:
            if palabraa[0:len(aculetras)] == aculetras:
                lista2.append(palabraa)
                w = w + 1
        j = j + 1
    if Visual.listasugerencias.size() > 0:
        Visual.listasugerencias.delete(0, END)
    while k < w:
        Visual.listasugerencias.insert(k, str(lista2[k]))
        k = k + 1
    db.close()


def enviar():
    global oracion, listasugerencias
    try:
        fichero = open('Mensaje.txt', 'w')
        fichero.write(str(Visual.oracion.get(0)))
        fichero.close()
        tkMessageBox.showinfo("", "Mensaje enviado con exito")
        # Limpiar todas las varibles, para poder escribir
        # otro mensaje
        Visual.oracion.delete(0)
        Visual.listasugerencias.delete(0)
        Main.cont = 0
        Main.borrar = 0
        Main.aculetras = ""
        Main.frase = ""
        Main.codigo = ""
        Main.tiempo = 1.3
        Main.codigototal = ""
    except E:
        tkMessageBox.showinfo("", "Error al enviar el mensaje")
        print str(E)


def borrar():
    global codigo, cont, aculetras, borrar, oracion
    temporal = str(Visual.oracion.get(0))
    print temporal
    if len(temporal) > 1:
        Main.borrar = 1
        temporal = temporal[0:(len(temporal) - 1)]
        Visual.oracion.delete(0)
        Visual.oracion.insert(0, (temporal))
        print "Temporal IF: " + str(Visual.oracion.get(0))
    else:
        Visual.oracion.delete(0)
        print "Temporal ELSE: " + str(Visual.oracion.get(0))
        pass
    # Limpiar variables
    Main.cont = 0
    Main.aculetras = ""
    Main.codigo = ""


def agregar():
    # Obtiene todas las palabras de la oracion
    conjunto = str(Visual.oracion.get(0))
    # Separa las palabras por el espacio
    conjunto = conjunto.split(' ')
    lista1 = []
    # Agrega las palabras separadas en una lista
    for x in conjunto:
        lista1.append(x)
    # Se obtiene la ultima palabra escrita
    # y se inserta en un listbox para mostrar la palabra agregada
    Visual.agregarpalabra.insert(0, (lista1[len(lista1) - 1]))
    db = Manejo_Db('Dataprueba.fs')
    dbroot = db.dbroot
    palabras = dbroot['palabras']
    # Se agrega la palabra con su codigo a la bd
    palabras[Main.codigototal] = str(Main.aculetras)
    dbroot._p_changed = 1
    transaction.commit()
    db.close()


def modificar():
    pass
