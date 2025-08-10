# 1. Crea una lista con los números del 1 al 5 e imprímela.

my_list = [1, 2, 3, 4, 5]
print(my_list)

# 2. Accede e imprime el tercer elemento de la lista [10, 20, 30, 40, 50].

my_other_list = list((10, 20, 30,30, 40, 50))
print(my_other_list[3])

# 3. Agrega el número 6 al final de la lista [1, 2, 3, 4, 5] e imprímela.

my_list.append(6)
print(my_list)

# 4. Inserta el número 15 en la posición 2 de la lista [10, 20, 30, 40, 50].

my_other_list.insert(2, 15)
print(my_other_list)

# 5. Elimina el primer valor 30 de la lista [10, 20, 30, 30, 40, 50].

my_other_list.remove(30)
print(my_other_list)

# 6. Usa la función pop() para eliminar el último elemento de la lista [1, 2, 3, 4, 5] y almacénalo en una variable.# Imprime la variable y la lista.

my_pop_element = my_list.pop()
print(my_list)
print(my_pop_element)

# 7. Invierte la lista [100, 200, 300, 400, 500] e imprímela.

mi_nueva_lista = [100, 200, 300, 400, 500]
mi_nueva_lista.reverse()
print(mi_nueva_lista)

# 8. Ordena la lista [3, 1, 4, 2, 5] en orden ascendente e imprímela.

mi_lista_desordenada = [3, 1, 4, 2, 5]
mi_lista_desordenada.sort()
print(mi_lista_desordenada)

# 9. Concatena las listas [1, 2, 3] y [4, 5, 6] y almacena el resultado en una nueva lista. Imprime la lista resultante.

my_list1 =[1, 2, 3]
my_list2 =[4, 5, 6]
my_list3 = my_list1 + my_list2
print(my_list3)

# 10. Crea una sublista con los elementos de la lista [10, 20, 30, 40, 50] que van desde la posición 1 hasta la 3 (sin incluir la posición 3).

sublista = my_other_list[1:3]
print(sublista)