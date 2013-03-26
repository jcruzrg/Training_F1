'''
Created on Mar 26, 2013

@author: jc
'''
from Tkinter import *
import thread
import time


codletras = {"2": "a", "22": "b", "222": "c", "3": "d", "33": "e", "333": "f",\
          "4": "g", "44": "h", "444": "i", "5": "j", "55": "k", "555": "l",\
          "6": "m", "66": "n", "666": "o", "7": "p", "77": "q", "777": "r",\
          "7777": "s", "8": "t", "88": "u", "888": "v", "9": "w", "99": "x",\
          "999": "y", "9999": "z", '*': "-", '#': " "}
palabras = {446665552: "hola", 7777444: "si", 4777222244427777: "gracias",\
            2226666666: "como", 727772: "para", 66666: "no", 7666777: "por",\
            62555: "mal", 33777782: "esta", 224443366: "bien", 66232: "nada",\
            3338866222444666662: "funciona", 3332555555666: "fallo",\
            22244288: "chau"}

cont = 0
aculetras = ""
frase = ""
codigo = ""
tiempo = 1.3


def cero():
    pass


def uno():
    capturar(1)
    pass


def dos():
    capturar(2)
    pass


def tres():
    capturar(3)
    pass


def cuatro():
    capturar(4)
    pass


def cinco():
    capturar(5)
    pass


def seis():
    capturar(6)
    pass


def siete():
    capturar(7)
    pass


def ocho():
    capturar(8)
    pass


def nueve():
    capturar(9)
    pass


def numeral():
    capturar("#")
    pass


def asterisco():
    capturar("*")
    pass


def enviar():
    pass


def borrar():
    global codigo, cont, aculetras
    temporal = str(oracion.get(0))
    temporal = temporal[0:(len(temporal) - 1)]
    oracion.delete(0)
    oracion.insert(0, (temporal))
    cont = 0
    aculetras = ""
    codigo = ""



def capturar(event):
    global codigo, cont
    cont = cont + 1
    print event
    codigo = codigo + str(event)


def sugerencias(hilo1, espera):
    global aculetras, codigo, cont, frase
    while 1:
        if codigo == "1":
            palabrasugerida = str(listasugerencias.get(END, 0))
            frase = frase + "" + palabrasugerida
            oracion.delete(0)
            oracion.insert(0, (frase))
            print frase
            while listasugerencias.size() > 0:
                listasugerencias.delete(0)
            cont = 0
            aculetras = ""
            codigo = ""
        if cont != 0 and codigo != "1":
            time.sleep(espera)
            try:
                aculetras = aculetras + codletras[codigo]
                print aculetras
            except:
                aculetras = ""
                cont = 0
            if codigo == '#':
                frase = frase + "" + aculetras
                aculetras = ""
                print codigo
                codigo = ""
                '''
                while listasugerencias.size() > 0:
                    listasugerencias.delete(0)
                '''
            cont = 0
            codigo = ""
            print "Oracion: " + frase + aculetras
            oracion.delete(0)
            oracion.insert(0, (frase + aculetras))
            print aculetras
            if len(aculetras) >= 1:
                for x in palabras:
                    if palabras[x].find(aculetras) >= 0:
                        if len(palabras[x]) == (len(aculetras) + 1) or len(palabras[x]) == (len(aculetras) + 2):
                            if listasugerencias.size() == 0:
                                listasugerencias.insert(END, str(palabras[x]))
        pass
'''
frame = Frame(root, width=200, height=100)
frame.bind_all("<Key>", capturar)
frame.pack()
var = StringVar()
label = Label(frame,textvariable=var, relief=RAISED)
var.set("Presione:\n1:Seleccionar sugerencia\
        \n2:Modificar palabras\n3:Agregar palabras\
        \n0 Borrar")
label.pack(side="left")
listasugerencias = Listbox(height=5, width=10)
listasugerencias.pack(side="left")
'''


ventana = Tk()
ventana.title('Teclado')
ventana.grid(baseWidth=250, baseHeight=250, widthInc=250, heightInc=280)

cartel1 = StringVar()
label = Label(ventana, textvariable=cartel1, fg='red')
cartel1.set("Sugerencias")
label.grid(row=0, column=0, sticky=S)

cartel2 = StringVar()
label = Label(ventana, textvariable=cartel2, fg='red')
cartel2.set("Escribiendo...")
label.grid(row=0, column=1, sticky=S)

listasugerencias = Listbox(ventana, height=5, width=15)
listasugerencias.grid(row=1, column=0, sticky=W)

oracion = Listbox(ventana, height=5, width=15)
oracion.grid(row=1, column=1, sticky=W)

boton1 = Button(ventana, text="1\n", fg='red', height=2, width=2, command=uno)
boton1.grid(row=2, column=0, sticky=W)

boton2 = Button(ventana, text="2\nabc", fg='red', height=2, width=2, command=dos)
boton2.grid(row=2, column=0, sticky=S)

boton3 = Button(ventana, text="3\ndef", fg='red', height=2, width=2, command=tres)
boton3.grid(row=2, column=0, sticky=E)

boton4 = Button(ventana, text="4\nghi", fg='red', height=2, width=2, command=cuatro)
boton4.grid(row=3, column=0, sticky=W)

boton5 = Button(ventana, text="5\njkl", fg='red', height=2, width=2, command=cinco)
boton5.grid(row=3, column=0, sticky=S)

boton6 = Button(ventana, text="6\nmno", fg='red', height=2, width=2, command=seis)
boton6.grid(row=3, column=0, sticky=E)

boton7 = Button(ventana, text="7\npqrs", fg='red', height=2, width=2, command=siete)
boton7.grid(row=4, column=0, sticky=W)

boton8 = Button(ventana, text="8\ntuv", fg='red', height=2, width=2, command=ocho)
boton8.grid(row=4, column=0, sticky=S)

boton9 = Button(ventana, text="9\nwxyz", fg='red', height=2, width=2, command=nueve)
boton9.grid(row=4, column=0, sticky=E)

boton10 = Button(ventana, text="*\n", fg='red', height=2, width=2, command=asterisco)
boton10.grid(row=5, column=0, sticky=W)

boton11 = Button(ventana, text="0\n", fg='red', height=2, width=2, command=cero)
boton11.grid(row=5, column=0, sticky=S)

boton12 = Button(ventana, text="#\n", fg='red', height=2, width=2, command=numeral)
boton12.grid(row=5, column=0, sticky=E)

boton13 = Button(ventana, text="Enviar", fg='red', height=2, width=2, command=enviar)
boton13.grid(row=2, column=1, sticky=W)

boton14 = Button(ventana, text="Borrar", fg='red', height=2, width=2, command=borrar)
boton14.grid(row=2, column=1, sticky=S)
try:
    thread.start_new_thread(sugerencias, ("Thread-1", tiempo, ))
except:
    print "Error"
ventana.mainloop()