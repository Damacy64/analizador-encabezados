import argparse
import sys
import re
# Configurar el menu de ayuda, para saber que argumentos debe de mandar
parser = argparse.ArgumentParser(description='Procesar un archivo de texto y mostrar las líneas que comienzan con ciertos prefijos.')
parser.add_argument('archivo', type=str, help='Ruta del archivo a procesar')

# Parsear los argumentos
args = parser.parse_args()

def extraer_encabezados(texto):
    patron = r"(^[A-Za-z0-9-]+:.*?)(?=\n[A-Za-z0-9-]+:|\Z)"

    encabezados_info = re.findall(patron, texto, re.MULTILINE | re.DOTALL)
    return encabezados_info

# Varificamos que el usuario, mande un archivo
if len(sys.argv) < 2:
    print("Uso: python script.py <archivo.txt>")
    sys.exit(1)
    
# Recuperamos el archivo
nombre_archivo = sys.argv[1]

try:
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        texto = archivo.read()  # Leer todo el contenido del archivo

    # Extraer encabezados con su información completa
    encabezados_info = extraer_encabezados(texto)

    # Imprimir los encabezados con su contenido
    for encabezado in encabezados_info:
        print(encabezado.strip())  # Imprime cada encabezado con su información
        print("-" * 80)  # Separador para mejor visualización

except FileNotFoundError:
    print(f"Error: El archivo '{nombre_archivo}' no existe.")
except Exception as e:
    print(f"Error: {e}")
"""    patterns = {
        "Delivered_To": r"Delivered-To: (.+?)\n",
        "Received": r"Received: (.+?)\n",
        "X-Google-Smtp-Source": r"X-Google-Smtp-Source: (.+?)\n",
        "X-Received": r"X-Received: (.+?)\n",
        "ARC-Seal": r"ARC-Seal: (.+?)\n",
        "ARC-Message-Signature": r"ARC-Message-Signature: (.+?)\n",
        "ARC-Authentication-Results": r"ARC-Authentication-Results: (.+?)\n",
        "Return-Path": r"Return-Path: (.+?)\n",
        "Received": r"Received: (.+?)\n",
        "Received-SPF": r"Received-SPF: (.+?)\n",
        "Authentication-Results": r"Authentication-Results: (.+?)\n",
        "DKIM-Signature": r"DKIM-Signature: (.+?)\n",
        "DomainKey-Signature": r"DomainKey-Signature: (.+?)\n",
        "Received": r"Received: (.+?)\n",
        "IdPortal": r"IdPortal: (.+?)\n",
        "IdTipoMail": r"IdTipoMail: (.+?)\n",
        "List-Unsubscribe": r"List-Unsubscribe: (.+?)\n",
        "List-Unsubscribe-Post": r"List-Unsubscribe-Post: (.+?)\n",
        "Feedback-ID": r"Feedback-ID: (.+?)\n",
        "MIME-Version": r"MIME-Version: (.+?)\n",
        "From": r"From: (.+?)\n",
        "To": r"To: (.+?)\n",
        "Reply-To": r"Reply-To: (.+?)\n",
        "Date": r"Date: (.+?)\n",
        "Subject": r"Subject: (.+?)\n",
        "Content-Type": r"Content-Type: (.+?)\n",
        "Content-Transfer-Encoding": r"Content-Transfer-Encoding: (.+?)\n",
        "Message-ID": r"Message-ID: (.+?)\n",
        "X-OriginalArrivalTime": r"X-OriginalArrivalTime: (.+?)\n",
    }

    extracted_fields = {}

    for field, pattern in patterns.items():
        match = re.search(pattern, lineas)
        if match:
            extracted_fields[field] = match.group(1)

# Imprimir los campos extraídos
for field, value in extracted_fields.items():
    print(f"{field}: {value}")"""
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
