import os

def listar_archivos(ruta):
    #guardo en esta variable los nombres de la lista que hay en el directorio
    lista_archivos = os.listdir(ruta)
    return lista_archivos

#guardo la ruta en donde esta corriendo mi codigo
ruta_absoluta = os.getcwd()
#nombre de la carpeta en donde esta mi codigo
ruta_relativa = "c:/Users/MiEquipo/Documents/Practicas de Python/"
archivos = listar_archivos(ruta_relativa)
print(archivos)