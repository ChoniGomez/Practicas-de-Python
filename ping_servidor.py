#ping: enviar una senial a un servidor
#se hace ping a servidores o dominios

import os


def hacer_ping(hostname):
    #funcion para hacer ping a un servidor 
    # retorna 0 si esta activo
    # respuesta = os.system(f"ping -c 1 {hostname}") para linux
    respuesta = os.system(f"ping -n 1 {hostname}")
    if respuesta == 0:
        print (hostname, "está activo.")
    else:
        print (hostname, "está caído.")


hacer_ping("google.com")