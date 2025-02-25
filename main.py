import argparse
import sys
import re
import hashlib
from email.policy import default as DefaultPolicy
from email.parser import Parser
# Configurar el menu de ayuda, para saber que argumentos debe de mandar
parser = argparse.ArgumentParser(description='Procesar un archivo de texto y mostrar las líneas que comienzan con ciertos prefijos.')
parser.add_argument('archivo', type=str, help='Ruta del archivo a procesar')

# Parsear los argumentos
args = parser.parse_args()

# Varificamos que el usuario, mande un archivo
if len(sys.argv) < 2:
    print("Uso: python script.py <archivo.txt>")
    sys.exit(1)
    
# Recuperamos el archivo
nombre_archivo = sys.argv[1]

try:
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        texto = archivo.read()
        msg = Parser(policy=DefaultPolicy).parsestr(texto)

        # Buscamos URL que haya en el correo
        links = re.findall(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', texto)
        links = list(dict.fromkeys(links)) # Borramos los links que esten duplicados
        links = list(filter(None, links))
        if links:
            print(' | URLs encontradas:')
            for link in links:
                print("-" * 50)
                print(f"| {link}")
                print("-" * 50)
        else:
            print('No hay URLs encontradas.')
        print('\n')

        # Buscamos IP's en el correo
        direcciones_ip = re.findall(r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b', texto)
        if direcciones_ip:
            print(' | IPs encontradas:')
            for ip in direcciones_ip:
                print("-" * 50)
                print(f" | {ip}")
                print("-" * 50) 
        else:
            print('No hay IPs encontradas.')
        print('\n')

        # Busqueda de los headers
        cabecera = {key: value for key, value in msg.items()}    

        # Verificar protocolos de seguridad
        security_results = {
        "ARC": any(key in cabecera for key in ["ARC-Seal", "ARC-Message-Signature", "ARC-Authentication-Results"]),
        "SPF": "Received-SPF" in cabecera,
        "DKIM": "DKIM-Signature" in cabecera,
        "DMARC": "Authentication-Results" in cabecera and "dmarc=pass" in cabecera["Authentication-Results"].lower()
        }

        # Mostrar resultados
        for key, value in security_results.items():
            print(f"{key}: {'✅ Presente' if value else '❌ No encontrado'}\n")


        for header in ['Received']:
            cabecera[header] = msg.get_all(header) if header in msg else []

        for clave, valor in cabecera.items():
            print(f"{clave} : \n              {valor}")
            print("-" * 250)
        
except FileNotFoundError:
    print(f"Error: El archivo '{nombre_archivo}' no existe.")
except Exception as e:
    print(f"Error: {e}")