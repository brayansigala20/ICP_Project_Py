texto_original = """Antena Satelital KIT400042280 GEN3 
Incluye servicio de consumo ilimitado 150Mbs asimétrico
Prioridad de satélite 1TB
Mes de JUNIO"""

# Texto original con caracteres no reconocidos
# Texto original con caracteres no reconocidos
texto = "Antena Satelital KIT400042280 GEN3\nIncluye servicio de consumo ilimitado 150Mbs asim�trico\nPrioridad de sat�lite 1TB\nMes de JUNIO"


# Función para eliminar o reemplazar caracteres especiales
def limpiar_texto(texto):
    # Diccionario de caracteres problemáticos y sus reemplazos
    reemplazos = {
        "á": "a",
        "é": "e",
        "í": "i",
        "ó": "o",
        "ú": "u",
        "Á": "A",
        "É": "E",
        "Í": "I",
        "Ó": "O",
        "Ú": "U",
        "ñ": "n",
        "Ñ": "N",
        "ü": "u",
        "Ü": "U",
        "à": "a",
        "è": "e",
        "ì": "i",
        "ò": "o",
        "ù": "u",
        "À": "A",
        "È": "E",
        "Ì": "I",
        "Ò": "O",
        "Ù": "U",
        "�": "",
    }

    # Reemplazar caracteres especiales
    for caracter, reemplazo in reemplazos.items():
        texto = texto.replace(caracter, reemplazo)

    return texto


# Limpiar el texto
texto_limpio = limpiar_texto(texto)

# Imprimir el texto limpio
print(texto_limpio)
