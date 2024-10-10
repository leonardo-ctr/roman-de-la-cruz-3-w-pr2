print(" ") #DEFINE UNA LINEA EN BLANCO
print("Roman De la Cruz Leonardo Antonio,3-w, 1211 ")
def longitud_ultima_palabra(texto):
    # Eliminar espacios en blanco al principio y al final, y dividir el texto en palabras
    palabras = texto.strip().split()
    # Verificar si hay palabras
    if palabras:
        return len(palabras[-1])  # Devolver la longitud de la última palabra
    return 0  # Si no hay palabras, devolver 0
print(" ") #DEFINE UNA LINEA EN BLANCO
# Ejemplo de uso
print(" ") #DEFINE UNA LINEA EN BLANCO
texto = "   Hola mundo   "
print(" ") #DEFINE UNA LINEA EN BLANCO
longitud = longitud_ultima_palabra(texto)#variable
print(" ") #DEFINE UNA LINEA EN BLANCO
print(f"La longitud de la última palabra es: {longitud}")
#imprime resultado
print(" ") #DEFINE UNA LINEA EN BLANCO
