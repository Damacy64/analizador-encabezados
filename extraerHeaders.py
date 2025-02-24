import re
from tkinter import *
from tkinter import filedialog

def extraer_encabezados(texto):
    patron = r"(^[A-Za-z0-0-]+:.*?)(?=\n[A-Za-z0-9-]+:|\Z)"
    encabezados_info = re.findall(patron, texto, re.MULTILINE | re.DOTALL)
    return encabezados_info

def obtener_ruta():
    ruta_archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])
    if ruta_archivo:
        return ruta_archivo
    else:
        return "No fue posible obtener la ruta"

def seleccionar_archivo(widgets_text):
    if  widgets_text != "":
        ruta = obtener_ruta()
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                texto = archivo.read()  # Leer todo el contenido del archivo
            
            # Extraer encabezados con su información completa
            encabezados_info = extraer_encabezados(texto)
        
            # Imprimir los encabezados con su contenido
            for encabezado in encabezados_info:
                widgets_text.insert(END, encabezado.strip() + "\n")  # Imprime cada encabezado con su información
        except FileNotFoundError:
            print(f"Error: El archivo '{ruta}' no existe.")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("error")