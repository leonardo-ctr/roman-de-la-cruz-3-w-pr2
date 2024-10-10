print(" ")#define una linea en blanco
print("Roman De la Cruz Leonardo Antonio,3.w,1211")
import math
print(" ")#define una linea en blanco
#solicita valores
print(" ")#define una linea en blanco
def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)
print(" ")#define una linea en blanco
#solicita valores
def calcular_volumen_cilindro(radio, altura):
    area_base = calcular_area_circulo(radio)  # Usamos la función anterior
    volumen = area_base * altura
    return volumen
    print(" ")#define una linea en blanco
# Datos de entrada
radio = 5  # Radio del círculo
altura = 10  # Altura del cilindro
print(" ")#define una linea en blanco
# Calcular el área del círculo
area = calcular_area_circulo(radio)
print(f"El área del círculo es: {area:.2f}")
print(" ")#define una linea en blanco
# Calcular el volumen del cilindro
volumen = calcular_volumen_cilindro(radio, altura)
print(f"El volumen del cilindro es: {volumen:.2f}")
print(" ")#define una linea en blanco
