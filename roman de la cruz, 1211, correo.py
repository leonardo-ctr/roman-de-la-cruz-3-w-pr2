def es_email_valido(email):
    return '@' in email

# Capturar dirección de email
email_usuario = input("Introduce tu dirección de email: ")

# Verificar si es válida
if es_email_valido(email_usuario):
    print("La dirección de email es válida.")
else:
    print("La dirección de email no es válida.")