import re


#funcion solamente para comprobar un formato valido, no revisa si existe o no
def email_valido(email):
    #defino una expresion regular para validar el correo electronico
    formato_valido = r"^([a-z0-9]+[.-_])*[a-z0-9]+@[a-z0-9-]+(\.[a-z]{2,})+$"
    if re.match(formato_valido, email, re.IGNORECASE):
        return True
    return False

valido = email_valido("choni@email.edu.co")
print("Email valido:", valido)