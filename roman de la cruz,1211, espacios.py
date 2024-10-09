def longitud_ultima_palabra(texto):
    # Eliminar espacios en blanco al principio y al final, y dividir el texto en palabras
    palabras = texto.strip().split()
    # Verificar si hay palabras
    if palabras:
        return len(palabras[-1])  # Devolver la longitud de la última palabra
    return 0  # Si no hay palabras, devolver 0

# Ejemplo de uso
texto = "   Hola mundo   "
longitud = longitud_ultima_palabra(texto)
print(f"La longitud de la última palabra es: {longitud}")