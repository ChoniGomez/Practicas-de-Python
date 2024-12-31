#iterar listas con la funcion zip()

lista_nombres = ["Ana", "Paco", "Javier", "Emilio", "Choni"]
lista_edades = [25, 27, 25, 26]

#unir las 2 listas con zip
datos = zip(lista_nombres, lista_edades)

print (list(datos))

#recorrer zip con un for
for nombre, edades in zip (lista_nombres, lista_edades):
    print (nombre, edades)