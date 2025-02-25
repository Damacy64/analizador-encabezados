import re
from tkinter import *
from email.policy import default as DefaultPolicy
from tkinter import filedialog
from email.parser import Parser

def extraer_encabezados(texto):
    msg = Parser(policy=DefaultPolicy).parsestr(texto)
    cabecera = {key: value for key, value in msg.items()}
    return cabecera

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

            security_results = {
            "ARC": any(key in encabezados_info for key in ["ARC-Seal", "ARC-Message-Signature", "ARC-Authentication-Results"]),
            "SPF": "Received-SPF" in encabezados_info,
            "DKIM": "DKIM-Signature" in encabezados_info,
            "DMARC": "Authentication-Results" in encabezados_info and "dmarc=pass" in encabezados_info["Authentication-Results"].lower()
            }

            # Limpiar el widgets_text
            widgets_text.config(state="normal")
            widgets_text.delete("1.0", END)
            
            buscar_links(texto,widgets_text)
            buscar_ip(texto,widgets_text)

            widgets_text.insert("insert","\n Protocolos encontrados:\n")
            for key, value in security_results.items():
                widgets_text.insert("insert", f"{key}: {'✅ Presente' if value else '❌ No encontrado'}\n")
                widgets_text.insert("insert", "-" * 85)

            for clave, valor in encabezados_info.items():
                widgets_text.insert("insert", f"{clave} : \n              {valor}\n")
                widgets_text.insert("insert", "-" * 85)
            widgets_text.config(state="disabled")

            # Imprimir los encabezados con su contenido
        except FileNotFoundError:
            print(f"Error: El archivo '{ruta}' no existe.")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("error")

def buscar_links(texto,widgets_text):
    links = re.findall(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', texto)
    links = list(dict.fromkeys(links)) # Borramos los links que esten duplicados
    links = list(filter(None, links))
    if links:
        widgets_text.insert("insert", " URLs encontradas:\n")
        for link in links:
            widgets_text.insert("insert", f" {link}\n")
            widgets_text.insert("insert", ("-" * 50) + "\n")
    else:
        widgets_text.insert("insert","No hay URLs encontradas.\n")

def buscar_ip(texto,widgets_text):
    direcciones_ip = re.findall(r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b', texto)
    if direcciones_ip:
        widgets_text.insert("insert","\n IPs encontradas:\n")
        for ip in direcciones_ip:
            widgets_text.insert("insert",f" {ip}\n")
            widgets_text.insert("insert",("-" * 50) + "\n") 
    else:
        widgets_text.insert("insert"," | No hay IPs encontradas.\n")

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