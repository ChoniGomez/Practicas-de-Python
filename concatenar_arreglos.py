lista_append = [1, 2, 3]
lista_extend = [4, 5, 6]
lista_insert = [7, 8, 9]

lista_letras = ["a", "b", "c"]

# Append agrega en la ultima posicion de la lista una lista que le mande a agregar
lista_append.append(lista_letras)
print(lista_append)

# Extend agrega a la lista actual, la lista que le mande a agregar, combinando las dos listas en una sola
lista_extend.extend(lista_letras)
print(lista_extend)

# Insert agrega una lista en otra, pero indicando la posicion en donde agregar como primer parametro
lista_insert.insert(1, lista_letras)
print(lista_insert)
