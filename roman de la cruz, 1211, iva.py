print(" ")#define una linea en blanco
print("Roman De la Cruz Leonardo Antonio, numero")
def calcular_total_factura(cantidad_sin_iva, porcentaje_iva):
    iva = cantidad_sin_iva * (porcentaje_iva / 100)
    total_con_iva = cantidad_sin_iva + iva
    return total_con_iva
print(" ")#define una linea en blanco
# Ejemplo de uso
cantidad_sin_iva = 1000  # Cantidad sin IVA
porcentaje_iva = 21     # Porcentaje de IVA
print(" ")#define una linea en blanco
total = calcular_total_factura(cantidad_sin_iva, porcentaje_iva)
print(f"El total de la factura es: {total:.2f}")
print(" ")#define una linea en blanco
