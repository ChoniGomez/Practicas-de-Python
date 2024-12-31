#nos permite acceder al SO
import os
#libreria para manejo de imagenes
from PIL import Image


def abrir_imagen_pilllow(ruta_absoluta_img):

    imagen = Image.open(ruta_absoluta_img)
    imagen.show()


ruta_relativa = "papitas.jpg"
ruta_absoluta = os.path.join(os.getcwd(), ruta_relativa)

#llamar a la funcion
abrir_imagen_pilllow(ruta_absoluta)