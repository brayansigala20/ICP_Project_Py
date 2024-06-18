import pandas as pd
from openpyxl import Workbook
import re
from unidecode import unidecode


excel = pd.read_excel("C:\\Users\\braya\\Downloads\\ICP\\descripcionWeb.xlsx")

texto_original = excel["Descripcion"][0]

# # Definir los nuevos valores
# nuevo_mes = "JUNIO"
nueva_oc = excel["OC"][0]

# patron_mes = r"(MES DE )(\w+)"
# patron_oc = r"((?:[A-Z]{2,}-)?OC\s*\d+)"


# # Reemplazar usando re.sub()
# texto_modificado = re.sub(patron_mes, rf"\1{nuevo_mes}", texto_original)
# texto_modificado = re.sub(patron_oc, rf"\1{nueva_oc}", texto_modificado)

# print("Texto original:")
# print(texto_original)
# print("\nTexto modificado:")
# print(texto_modificado)

import re


def modificar_texto(texto, patronesReemplazos):
    """
    Modifica el texto buscando y reemplazando patrones específicos.

    :param texto: Texto original
    :param patrones_reemplazos: Diccionario con patrones a buscar y sus respectivos reemplazos
    :return: Texto modificado
    """
    for patron, reemplazo in patronesReemplazos.items():
        texto = re.sub(patron, reemplazo, texto)
    return texto


# Patrones a buscar y reemplazos
patrones_reemplazos = {
    r"MES DE MAYO": "MES DE JUNIO",
    r"mes de mayo": "MES DE JUNIO",  # Reemplaza 'MES DE MAYO' con 'MES DE JUNIO'
    r"MAYO 2024": "JUNIO 2024",  # Reemplaza 'MAYO 2024' con 'JUNIO 2024'
    r"OC:\s*[\w-]+": nueva_oc,
    r"OC\s*[\w-]+": nueva_oc,
    r"MPR-\d{6}-\d": nueva_oc,  #
}

# Modificar el texto
texto_modificado = modificar_texto(texto_original, patrones_reemplazos)
texto_sin_acentos = unidecode(texto_modificado)

print(texto_sin_acentos)
