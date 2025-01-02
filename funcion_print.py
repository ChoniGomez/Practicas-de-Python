print("Función print con cadena de texto")

#salida formateada
variable = 1
print(f"Concatenando variables {variable}")

#imprime 2 textos separados por un espacio
print("elementos", "separados")

#imprime los textos separados por lo que contiene la variable sep
print("elementos", "separados", "con", "sep", sep=".")

#imprime el texto con un finalizador de linea 
# por defecto end es /n
print("Primero", end=". ")
print("Segundo")

#imprimir texto en un archivo de texto
with open("print_ejemplo.txt", mode="w") as archivo:
    print("Hello World!", file=archivo)

#libreria para importar tiempo de espera
import time


print("Inicio", flush=False)
time.sleep(2)
print("Fin")


print("Inicio", end="...", flush=True)
time.sleep(2)
print("Fin")