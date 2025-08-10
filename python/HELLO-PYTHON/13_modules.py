### Modules ###

import my_module

my_module.sumvalue(5, 3, 1)
my_module.printvalue("Hola Python")

from my_module import sumvalue, printvalue

sumvalue(5, 3, 1)
printvalue("Hola Python")

import math

print(math.pi)
print(math.pow(2, 8))

from math import pi as PI_VALUE

print(PI_VALUE)