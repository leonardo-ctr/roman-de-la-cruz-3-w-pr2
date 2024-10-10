print(" ")#define una linea en blanco
print("Roman De la Cruz Leonardo Antonio, numero")
def es_email_valido(email):
    return '@' in email
print(" ")#define una linea en blanco
# Capturar dirección de email
email_usuario = input("Introduce tu dirección de email: ")
print(" ")#define una linea en blanco
# Verificar si es válida
if es_email_valido(email_usuario):
    print("La dirección de email es válida.")
    print(" ")#define una linea en blanco
else:
    print("La dirección de email no es válida.")
    print(" ")#define una linea en blanco
