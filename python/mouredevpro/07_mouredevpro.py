# 1. Crea un diccionario con las claves name, age, y country, asignando valores a cada una. Imprime el diccionario.

my_dict = {"name": "Joaquín", "age": 38, "country":"España"}
print(my_dict)

# 2. Accede al valor de la clave name en el diccionario.

print(my_dict["name"])

# 3. Añade una nueva clave job con el valor "Programador" al diccionario del punto anterior. Imprime el diccionario actualizado.

my_dict["job"] = "Programador"
print(my_dict) #{'name': 'Joaquín', 'age': 38, 'country': 'España', 'job': 'Programador'}

# 4. Modifica el valor de la clave age en el diccionario para que sea 38. Imprime el diccionario actualizado.

my_dict["age"] = 39 #{'name': 'Joaquín', 'age': 39, 'country': 'España', 'job': 'Programador'}
print(my_dict) # le he puesto 39 porque mi edad es ya 38 jajajaja para ver el cambio 

# 5. Elimina la clave country del diccionario e imprime el diccionario resultante.

del my_dict["country"]
print(my_dict) #{'name': 'Joaquín', 'age': 39, 'job': 'Programador'}

# 6. Crea un diccionario donde las claves sean números del 1 al 5 y los valores sean sus cuadrados (ejemplo: 1: 1, 2: 4, ...).

my_other_dict = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} #El cuadrado de un número significa multiplicarlo por sí mismo ayuda de chatgpt 
print(my_other_dict)

# 7. Verifica si la clave age está presente en el diccionario {"name": "Brais", "age": 37, "country": "Galicia"}.

print("age" in my_dict) #True

# 8. Imprime solo las claves del diccionario.

print(my_dict.keys()) #dict_keys(['name', 'age', 'job'])

# 9. Convierte las claves del diccionario en una lista e imprime la lista resultante.

print(list(my_dict.values()))

# 10. Crea un nuevo diccionario a partir de una lista de claves ["name", "age", "job"] usando fromkeys(), asignando a todas las claves el valor "Desconocido".

my_new_dict = dict.fromkeys(my_dict, ("Desconocido"))
print(my_new_dict)
