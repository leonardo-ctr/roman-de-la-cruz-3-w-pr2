print(" ") #DEFINE UNA LINEA EN BLANCO
print("Roman De la Cruz Leonardo Antonio,3-w, 1211 ")
def es_vocal(caracter):
    print(" ") #DEFINE UNA LINEA EN BLANCO
    # Convertir el carácter a minúsculas para hacer la comparación
    return caracter.lower() in 'aeiou'
print(" ") #DEFINE UNA LINEA EN BLANCO

# Ejemplo de uso
caracter = 'a'
resultado = es_vocal(caracter)
print(f"¿'{caracter}' es una vocal? {resultado}")  # Debería devolver True
print(" ") #DEFINE UNA LINEA EN BLANCO
