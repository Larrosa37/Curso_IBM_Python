# 1. Crea una tupla con los valores (10, 20, 30, 40, 50) e imprímela.

my_tuple = (10, 20,30, 40, 50)
print(my_tuple)

# 2. Accede al segundo elemento de la tupla (100, 200, 300, 400, 500) y muéstralo.

print(my_tuple[2])

# 3. Intenta modificar el primer elemento de la tupla (1, 2, 3) a 10 y observa el resultado.

my_other_tuple = (1, 2, 3)
#my_other_tuple[0] = 10
#print(my_other_tuple)
#TypeError: 'tuple' object does not support item assignment

# 4. Cuenta cuántas veces aparece el número 3 en la tupla (1, 2, 3, 3, 4, 5, 3).
mi_tupla =(1, 2, 3, 3, 4, 5, 3)
print(mi_tupla.count(3))

# 5. Encuentra el índice de la primera aparición de la cadena "Python" en la tupla ("Java", "Python", "JavaScript","Python").

my_new_tuple = ("Java", "Python", "Javascript", "Python")
print(my_new_tuple.index("Python"))

# 6. Concatena dos tuplas: (1, 2, 3) y (4, 5, 6) e imprime la tupla resultante.

mi_tupla1 = (4, 5, 6)
print(my_other_tuple + mi_tupla1)

# 7. Crea una subtupla con los elementos desde la posición 2 hasta la 4 (sin incluir la 4) de la tupla (10, 20, 30, 40, 50).

print(my_tuple[2:4])

# 8. Convierte la tupla ("rojo", "verde", "azul") en una lista, cambia el segundo elemento a "amarillo" y vuelve a convertirla en una tupla. Imprime la tupla resultante.

my_color_tuple = ("Rojo", "Verde", "Azul")
my_color_tuple = list((my_color_tuple))
print(type(my_color_tuple))

my_color_tuple[2] = "Amarillo"
my_color_tuple = tuple(my_color_tuple)
print(tuple(my_color_tuple))
print(type(my_color_tuple))

# 9. Elimina una tupla llamada my_tuple usando del y luego intenta imprimirla para ver el resultado.
del (my_tuple)
#print(my_tuple)  NameError: name 'my_tuple' is not defined

# 10. Crea una tupla con un solo elemento (el número 100) e imprímela.
# Asegúrate de usar la sintaxis correcta para crear una tupla con un solo elemento.
my_super_tuple = (100)
print(my_super_tuple)