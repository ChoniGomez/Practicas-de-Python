#Importar la libreria para ocupar Union
from typing import Union

# agregar Union y los parametros que puede aceptar la funcion, tanto para recibir como para devolver
def calular_perimetro_cuadrado(lado: Union[int, float]) -> Union[int, float]:
    return 4 * lado


print(calular_perimetro_cuadrado(lado=5))