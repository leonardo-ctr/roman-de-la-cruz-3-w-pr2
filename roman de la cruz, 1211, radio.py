import math

def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

def calcular_volumen_cilindro(radio, altura):
    area_base = calcular_area_circulo(radio)  # Usamos la función anterior
    volumen = area_base * altura
    return volumen
    
    # Datos de entrada
radio = 5  # Radio del círculo
altura = 10  # Altura del cilindro

# Calcular el área del círculo
area = calcular_area_circulo(radio)
print(f"El área del círculo es: {area:.2f}")

# Calcular el volumen del cilindro
volumen = calcular_volumen_cilindro(radio, altura)
print(f"El volumen del cilindro es: {volumen:.2f}")