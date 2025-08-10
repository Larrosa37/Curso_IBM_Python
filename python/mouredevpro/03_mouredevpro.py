# 1. Declara una variable text con la frase “Aprendiendo Python” y luego imprime la longitud de la cadena usando len().

my_estudy = "Programación en Python"
print(len(my_estudy))

# 2. Concatena dos cadenas: “Hola” y “Python”, y muestra el resultado en una sola línea.

saludo = "Hola"
lenguaje = "Python"
print(saludo + " " + lenguaje)

# 3. Crea una cadena que incluya un salto de línea, y luego imprímela para ver el resultado.
lenguaje = "Estudiando\nPython"
print(lenguaje)

# 4. Usa el formateo de cadenas con f-strings para imprimir tu nombre, apellido y edad en una cadena de texto.

name, surname, age = "joaquín", "Larrosa", 38

print(f"Mi nonbre es {name} {surname} y mi edad es {38}")

# 5. Desempaqueta los caracteres de la palabra “Python” en variables separadas y luego imprímelos uno por uno.

lenguaje = "Python"
a, b, c, d, e, f = lenguaje
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# 6. Extrae un “slice” de la palabra “Programación” para obtener los caracteres desde la posición 3 hasta la 7.
study = "Programación"
study_slice = study[3:7]
print(study_slice)

# 7. Invierte la cadena “Python” usando slicing y muestra el resultado.

reversed_lenguaje = lenguaje[::-1]
print(reversed_lenguaje)

# 8. Convierte la cadena “aprendiendo python” en mayúsculas usando el método adecuado e imprímela.

print(my_estudy.upper())

# 9. Cuenta cuántas veces aparece la letra “n” en la cadena “Programación en Python”.

print(my_estudy.count("n"))

# 10. Verifica si la cadena “12345” es numérica usando el método adecuado e imprime el resultado.

print("12345".isnumeric())
