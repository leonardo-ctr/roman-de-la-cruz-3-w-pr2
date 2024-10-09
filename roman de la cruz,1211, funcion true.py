def es_vocal(caracter):
    # Convertir el carácter a minúsculas para hacer la comparación
    return caracter.lower() in 'aeiou'

# Ejemplo de uso
caracter = 'a'
resultado = es_vocal(caracter)
print(f"¿'{caracter}' es una vocal? {resultado}")  # Debería devolver True