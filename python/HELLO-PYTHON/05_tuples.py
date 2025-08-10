### Tuples ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (38, 1.74, "joaquín", "larrosa", "joaquín")
my_other_tuple = (38, 60, 30)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) IndexError
#print(my_tuple[-6]) IndexError

print(my_tuple.count("joaquín"))
print(my_tuple.index("larrosa"))
print(my_tuple.index("joaquín"))

#my_tuple[1] = 1.80 'tuple' object does not support item assignment

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3, 6])