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
        
            # Limpiar el widgets_text
            widgets_text.config(state="normal")
            widgets_text.delete("1.0", "end")
            widgets_text.insert("insert", texto)
            widgets_text.config(state="disabled")

            # Imprimir los encabezados con su contenido
            for encabezado in encabezados_info:
                widgets_text.insert(END, encabezado.strip() + "\n")  # Imprime cada encabezado con su información
        except FileNotFoundError:
            print(f"Error: El archivo '{ruta}' no existe.")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("error")

def buscar_palabra(text_area,busqueda_entry):
    # Eliminar resaltados anteriores
    text_area.tag_remove("highlight", "1.0", END)
    busqueda_term = busqueda_entry.get()
    
    if not busqueda_term:
        return  # Si la entrada está vacía, no hacer nada

    start_pos = "1.0"
    while True:
        start_pos = text_area.search(busqueda_term, start_pos, stopindex=END, nocase=True)
        if not start_pos:
            break  # Si no encuentra más coincidencias, salir del loop
        
        end_pos = f"{start_pos}+{len(busqueda_term)}c"
        text_area.tag_add("highlight", start_pos, end_pos)
        text_area.tag_config("highlight", background="yellow", foreground="black")
        start_pos = end_pos  # Continuar buscando después de la última coincidencia