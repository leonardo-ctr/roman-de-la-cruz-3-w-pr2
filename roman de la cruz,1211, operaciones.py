print(" ")#define una linea en blanco
print("Roman De la Cruz Leonardo Antonio, numero")
def sum(lista):
    #operaciones y valores
    total = 0
    for numero in lista:
        total += numero
    return total

def multip(lista):
    total = 1
    for numero in lista:
        total *= numero
    return total

# Ejemplo de uso
numeros = [1, 2, 3, 4]

resultado_suma = sum(numeros)#resultado de los datos
resultado_multiplicacion = multip(numeros)

print(f"La suma de la lista es: {resultado_suma}")  # Debería devolver 10
print(f"La multiplicación de la lista es: {resultado_multiplicacion}") # Debería devolver 24
