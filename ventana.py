from tkinter import *
from tkinter import filedialog

def seleccionar_archivo():
    ruta_archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])
    if ruta_archivo:
        entrada.delete(0, END)
        entrada.insert(0, ruta_archivo)

raiz = Tk()
raiz.title("Extraer Headers")
raiz.geometry("400x150")

label = Label(raiz, text="Ingrese la cabecera o seleccione un archivo:")
label.pack(pady=10)

entrada = Entry(raiz, width=50)
entrada.pack(pady=5)

boton_seleccionar = Button(raiz, text="Buscar", command=seleccionar_archivo)
boton_seleccionar.pack(pady=10)

raiz.mainloop()