from ast import Lambda
from tkinter import *
from logica.extraerHeaders import seleccionar_archivo

raiz = Tk()
raiz.title("Extraer Headers")
raiz.resizable(False, False)

frame = Frame(raiz, width=800, height=500)
frame.pack()

label = Label(frame, text="Seleccione un archivo:")
label.grid(row=1, column=1, pady=10)

entrada = Text(frame)
entrada.grid(row=2, column=1, pady=5, padx=25)

boton_seleccionar = Button(frame, command=lambda:seleccionar_archivo(entrada), text="Buscar")
boton_seleccionar.grid(row=3, column=1, pady=5)

scroll = Scrollbar(frame, command=entrada.yview)
scroll.grid(row=2, column=3, sticky="nsew")
entrada.config(yscrollcommand=scroll.set)

raiz.mainloop()