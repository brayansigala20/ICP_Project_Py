import pandas as pd
from openpyxl import Workbook
from dotenv import load_dotenv
import re
import os as OS
from unidecode import unidecode

load_dotenv()

descripcion_web = OS.getenv("DESCRIPCION_WEB")
lista_nombres = OS.getenv("LISTA_NOMBRES")
excel = pd.read_excel(descripcion_web)
excel_Nombres = pd.read_excel(lista_nombres)


texto_original = excel["Descripcion"][0]
nueva_oc = excel["OC"][0] if pd.notna(excel["OC"][0]) else None
nuevo_kit = excel["Kit"][0] if pd.notna(excel["Kit"][0]) else None
nuevo_mes = "AGOSTO"
nueva_ubicacion = excel["Ubicacion"][0] if pd.notna(excel["Ubicacion"][0]) else None


def modificar_texto(texto, patrones_reemplazos, adicionales):
    """
    Modifica el texto buscando y reemplazando patrones específicos.
    Si algún patrón no se encuentra, lo añade al final del texto.

    :param texto: Texto original
    :param patrones_reemplazos: Diccionario con patrones a buscar y sus respectivos reemplazos
    :param adicionales: Diccionario con textos adicionales a añadir si no se encuentran
    :return: Texto modificado
    """
    texto_modificado = texto.lower()

    # Reemplazar los patrones
    for patron, reemplazo in patrones_reemplazos.items():
        if reemplazo:  # Solo reemplazar si el valor no está vacío
            texto_modificado = re.sub(patron, reemplazo, texto_modificado)

    # Convertir a mayúsculas antes de añadir textos adicionales
    texto_modificado_mayusculas = texto_modificado.upper()

    # Añadir textos adicionales si no se encuentran
    for clave, texto_adicional in adicionales.items():
        if texto_adicional:  # Solo añadir si el valor no está vacío
            patron_adicional = re.escape(texto_adicional.upper())
            if not re.search(patron_adicional, texto_modificado_mayusculas):
                texto_modificado_mayusculas += f" {texto_adicional.upper()}"

    return texto_modificado_mayusculas


# Patrones a buscar y reemplazos
patrones_reemplazos = {
    r"mes\s*(de\s*)?julio( '?\d{0,2})?": nuevo_mes,
    r"oc[:\s]*[\w-]+": nueva_oc,
    r"orden\s*compra\s*[\w-]+": nueva_oc,  # Patrón para "Orden Compra"
    r"kit\s*[\w-]+": nuevo_kit,
    r"antena\s*kit\s*[\w-]+": f"ANTENA {nuevo_kit}",  # Patrón para "ANTENA KIT"
    r"santa elena banamichi": nueva_ubicacion,
    r"unidad ermitaño": nueva_ubicacion,  # Patrón para "UNIDAD ERMITAÑO"
    r"banamichi": nueva_ubicacion,  # Patrón para "BANAMICHI"
    r"orisivo": nueva_ubicacion,  # Patrón para "ORISIVO"
    r"unidad san julian": nueva_ubicacion,  # Patrón para "UNIDAD SAN JULIAN"
    r"prepago costo 30 dias incluye\s*:\s*\d+ mbps de velocidad y consumo de datos": f"PREPAGO COSTO 30 DIAS INCLUYE: 200 MBPS DE VELOCIDAD Y CONSUMO DE DATOS {nuevo_kit}",  # Patrón para "PREPAGO COSTO 30 DIAS INCLUYE"
}

# Textos adicionales a añadir si no se encuentran
textos_adicionales = {
    "oc": nueva_oc,
    "kit": nuevo_kit,
    "mes": nuevo_mes,
    "ubicacion": nueva_ubicacion,
}


def construir_plantilla(ubicacion, kit, oc, mes):
    partes = ["SERVICIO DE INTERNET SATELITAL"]
    if ubicacion:
        partes.append(f"UBICACIÓN: {ubicacion}")
    if kit:
        partes.append(f"KIT: {kit}")
    if oc:
        partes.append(f"OC: {oc}")
    if mes:
        partes.append(f"MES DE {mes}")
    return " ".join(partes)


# Aplicar la modificación a todos los textos originales y ajustar al patrón deseado
textos_modificados = []

texto_modificado = modificar_texto(
    texto_original, patrones_reemplazos, textos_adicionales
)
# Construir el texto final según el patrón requerido
texto_final = construir_plantilla(nueva_ubicacion, nuevo_kit, nueva_oc, nuevo_mes)

print(unidecode(texto_final))
