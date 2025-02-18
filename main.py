import argparse
import re
# Configurar el menu de ayuda, para saber que argumentos debe de mandar
parser = argparse.ArgumentParser(description='Procesar un archivo de texto y mostrar las líneas que comienzan con ciertos prefijos.')
parser.add_argument('archivo', type=str, help='Ruta del archivo a procesar')

# Parsear los argumentos
args = parser.parse_args()

# Abrir el archivo recibido como parámetro
with open(args.archivo, 'r') as archivo:
    lineas = archivo.read()

    patterns = {
        "Delivered-To": r"Delivered-To: (.+?)\n",
        "Received": r"Received: (.+?)\n",
        "X-Google-Smtp-Source": r"X-Google-Smtp-Source: (.+?)\n",
        "From": r"From: (.+?)\n",
        "To": r"To: (.+?)\n",
        "Subject": r"Subject: (.+?)\n",
        "Date": r"Date: (.+?)\n",
        "ARC-Seal": r"ARC-Seal: (.+?)\n",
    }

    extracted_fields = {}

    for field, pattern in patterns.items():
        match = re.search(pattern, lineas)
        if match:
            extracted_fields[field] = match.group(1)

# Imprimir los campos extraídos
for field, value in extracted_fields.items():
    print(f"{field}: {value}")
# Procesar el contenido del archivo
"""    for linea in lineas:
        if linea.startswith('Delivered-To'):
            print(linea)
        elif linea.startswith('Received'):
            print(linea)
        elif linea.startswith('X-Google-Smtp-Soucer'):
            print(linea)
        elif linea.startswith('x-Received'):
            print(linea)
        elif linea.startswith('ARC-Seal'):
            print(linea)
        elif linea.startswith('ARC-Message-Signature'):
            print(linea)
        elif linea.startswith('ARC-Authentication-Results'):
            print(linea)
        elif linea.startswith('Return-Path'):
            print(linea)
        elif linea.startswith('From'):
            print(linea)
        elif linea.startswith('To'):
            print(linea)
        elif linea.startswith('Subject'):
            print(linea)
        elif linea.startswith('Date'):
            print(linea)
        elif linea.startswith('Message-ID'):
            print(linea)
        elif linea.startswith('Reply-To'):
            print(linea)
        elif linea.startswith('Authentication-Results'):
            print(linea) """