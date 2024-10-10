print(" ") #DEFINE UNA LINEA EN BLANCO
print("Roman De la Cruz Leonardo Antonio,3-w, 1211 ")
import math
#operaciones
print(" ") #DEFINE UNA LINEA EN BLANCO
def distancia_dirigida(punto1, punto2):
    x1, y1 = punto1
    x2, y2 = punto2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(" ") #DEFINE UNA LINEA EN BLANCO
# Ejemplo de uso
punto_a = (1, 2)
punto_b = (4, 6)
distancia = distancia_dirigida(punto_a, punto_b)
print(f"La distancia entre los puntos {punto_a} y {punto_b} es: {distancia:.2f}")
#print imprime resultados
print(" ") #DEFINE UNA LINEA EN BLANCO
