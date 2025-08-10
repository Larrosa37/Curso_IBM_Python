### Functions ###


def my_function ():
    print("Esto es una función")
   
    
my_function()         
my_function()
my_function()


def sum_two_values (first_values: int, second_values ):
    print(first_values + second_values)
    
sum_two_values(5, 7)
sum_two_values(54754, 71231)
sum_two_values("5", "7")
sum_two_values(1.4, 5.2)    

def sum_two_values_with_return (first_value, second_value):
    my_sum = first_value + second_value
    return my_sum

my_result = sum_two_values(1.4, 5.2)
print(my_result)

my_result = sum_two_values_with_return(10, 5)
print(my_result)

def print_name (name, surname):
    print(f"{name} {surname}")
    
print_name(surname = "Larrosa", name = "joaquín")

def print_name_with_default (name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")
    
print_name_with_default("joaquín", "Larrosa")
print_name_with_default("joaquín", "Larrosa", "JoaquínDev")

def print_upper_texts(*texts):
    print(type(texts))
    for text in texts:
        print(text.upper())
    
    
print_upper_texts("Hola", "Python", "JoaquínDev")
print_upper_texts("Hola")