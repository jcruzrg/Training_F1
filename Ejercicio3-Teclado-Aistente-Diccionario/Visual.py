'''
Created on Mar 28, 2013

@author: jc
'''
from FuncionBotones import *
from Tkinter import *
import Main


class MyClass(object):
    '''
    classdocs
    '''


ventana = Tk()
ventana.title('Teclado JCRUZRG')
ventana.grid(baseWidth=250, baseHeight=370, widthInc=250, heightInc=370)

# Label que sirve como titulo del Listbox de sugerencias
cartel1 = StringVar()
label = Label(ventana, textvariable=cartel1, fg='black')
cartel1.set("Sugerencias")
label.grid(row=0, column=0, sticky=S)

# Label para saber si se esta escribiendo o no
cartel2 = StringVar()
label = Label(ventana, textvariable=cartel2, fg='black')
label.grid(row=0, column=1, sticky=S)
cartel2.set("Escribe")

# Label palabras agregadas
cartel3 = StringVar()
label = Label(ventana, textvariable=cartel3, fg='black')
label.grid(row=2, column=1, sticky=S + W + E)
cartel3.set("Palabra agregada")

# Listbox donde se almacenan las sugerencias
# Este llama a una funcion cuando se hace click en algun
# contenido del Listboxscroll
scroll = Scrollbar(ventana, orient=VERTICAL)
listasugerencias = Listbox(ventana, height=5, width=15)
listasugerencias.grid(row=1, column=0, sticky=W)
listasugerencias.config(yscrollcommand=scroll.set)
scroll.config(command=listasugerencias.yview)
listasugerencias.bind('<<ListboxSelect>>', agregar_sugerencia)

# Listbox donde se almacena todo lo escrito
xScroll = Scrollbar(ventana, width=15, orient=HORIZONTAL)
xScroll.grid(row=2, column=1, sticky=N + E + W)
oracion = Listbox(ventana, height=5, width=15, xscrollcommand=xScroll.set)
oracion.grid(row=1, column=1, sticky=N + S + E + W)
xScroll['command'] = oracion.xview

# Listbox donde salen las litas de palabra a agregar palabras
agregarpalabra = Listbox(ventana, height=2, width=15)
agregarpalabra.grid(row=3, column=1, sticky=W)

# Inicio creacion de los botones, los cuales llaman a una
# funcion y pasan parametros
boton1 = Button(ventana, text="1\n", activeforeground='green',\
activebackground='black', bg='black', fg='white', height=2, width=2)
boton1.grid(row=4, column=0, sticky=W)

boton2 = Button(ventana, text="2\nabc", activeforeground='green',\
activebackground='black', bg='black', fg='white', height=2, width=2,\
command=lambda: Main.capturar(2))
boton2.grid(row=4, column=0, sticky=S)

boton3 = Button(ventana, text="3\ndef", activeforeground='green',\
activebackground='black', bg='black', fg='white', height=2, width=2,\
command=lambda: Main.capturar(3))
boton3.grid(row=4, column=0, sticky=E)

boton4 = Button(ventana, text="4\nghi", activeforeground='green',\
activebackground='black', bg='black', fg='white', height=2, width=2,\
command=lambda: Main.capturar(4))
boton4.grid(row=5, column=0, sticky=W)

boton5 = Button(ventana, text="5\njkl", activeforeground='green',\
activebackground='black', bg='black', fg='white', height=2, width=2,\
command=lambda: Main.capturar(5))
boton5.grid(row=5, column=0, sticky=S)

boton6 = Button(ventana, text="6\nmno", activeforeground='green',\
activebackground='black', bg='black', fg='white', height=2, width=2,\
command=lambda: Main.capturar(6))
boton6.grid(row=5, column=0, sticky=E)

boton7 = Button(ventana, text="7\npqrs", activeforeground='green',\
activebackground='black', bg='black', fg='white', height=2, width=2,\
command=lambda: Main.capturar(7))
boton7.grid(row=6, column=0, sticky=W)

boton8 = Button(ventana, text="8\ntuv", activeforeground='green',\
activebackground='black', bg='black', fg='white', height=2, width=2,\
command=lambda: Main.capturar(8))
boton8.grid(row=6, column=0, sticky=S)

boton9 = Button(ventana, text="9\nwxyz", activeforeground='green',\
activebackground='black', bg='black', fg='white', height=2, width=2,\
command=lambda: Main.capturar(9))
boton9.grid(row=6, column=0, sticky=E)

boton10 = Button(ventana, text="*\n", activeforeground='green',\
activebackground='black', bg='black', fg='white', height=2, width=2,\
command=lambda: Main.capturar('*'))
boton10.grid(row=7, column=0, sticky=W)

boton11 = Button(ventana, text="0\n", activeforeground='green',\
activebackground='black', bg='black', fg='white', height=2, width=2)
boton11.grid(row=7, column=0, sticky=S)

boton12 = Button(ventana, text="#\n", activeforeground='green',\
activebackground='black', bg='black', fg='white', height=2, width=2,\
command=lambda: Main.capturar('#'))
boton12.grid(row=7, column=0, sticky=E)

boton13 = Button(ventana, text="Enviar\n<-|", activeforeground='green',\
activebackground='black', bg='black', fg='white', height=2, width=4,\
command=enviar)
boton13.grid(row=2, column=0, sticky=W)

boton14 = Button(ventana, text="Borrar\n<--", activeforeground='green',\
activebackground='black', bg='black', fg='white', height=2, width=5,\
command=borrar)
boton14.grid(row=2, column=0, sticky=E)

boton14 = Button(ventana, text="Agregar\npalabra", activeforeground='green',\
activebackground='black', bg='black', fg='white', height=2, width=4,\
command=agregar)
boton14.grid(row=3, column=0, sticky=W)

boton14 = Button(ventana, text="Modificar\npalabra", activeforeground='green',\
activebackground='black', bg='black', fg='white', height=2, width=5,\
command=modificar)
boton14.grid(row=3, column=0, sticky=E)
# Fin creacion de los botones
ventana.mainloop()
