print(" ")#define una linea en blanco
print(" Roman De la Cruz leonardo Antonio, 3-w, numero:1211")

def calcular_factorial(n):
    if n < 0:
        return "El número debe ser entero positivo."
    if n == 0 or n == 1:
        return 1
    return n * calcular_factorial(n - 1)

# Ejemplo de uso
numero = 6
print(f"El factorial de {numero} es {calcular_factorial(numero)}")