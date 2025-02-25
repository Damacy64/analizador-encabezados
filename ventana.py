import tkinter as tk
from tkinter import scrolledtext
from logica.extraerHeaders import seleccionar_archivo, buscar_palabra


root = tk.Tk()
root.title("Revisar Correos")
root.geometry("725x450")
root.resizable(False,False)

# Área de texto con scroll
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=20)
text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
text_area.config(state="disabled")

# Botón para seleccionar archivo
btn_abrir = tk.Button(root, text="Abrir Archivo", command=lambda: seleccionar_archivo(text_area))
btn_abrir.pack(pady=10)

# Marco para la barra de búsqueda
busqueda_frame = tk.Frame(root)
busqueda_frame.pack(pady=5)

# Entrada de texto para la búsqueda
busqueda_entry = tk.Entry(busqueda_frame, width=30)
busqueda_entry.pack(side=tk.LEFT, padx=5)

# Botón para buscar
btn_busqueda = tk.Button(busqueda_frame, text="Buscar", command=lambda: buscar_palabra(text_area,busqueda_entry))
btn_busqueda.pack(side=tk.LEFT)
# Ejecutar la aplicación
root.mainloop()