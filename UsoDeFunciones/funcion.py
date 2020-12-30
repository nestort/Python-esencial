# Funcion simple
def eat():
    print("Comiendo...")

# Funcion recibe un parametro
def greet(person):
    print("Hola,", person)

# Funcion retorna un valor
def getAge():
    return 105

# Uso de funcion con parametro opcional y requerido
# El parametro 'a' es requerido mientras que el 'b' es opcional
def sumOfAge(a, b=0):
    return a+b


# Uso de funcion simple
eat()

# Uso de funcion que recibe parametro
person = "Obi wan"
greet(person)

# Uso de funcion que retorna valor
age = getAge()
print("la edad es", age)

# Uso de funcion con parametro opcional
test1 = sumOfAge(1)
test2 = sumOfAge(3,2)
print("Se paso el valor 'a' a la función, Resultado: ", test1)
print("Se paso el valor 'a' y 'b' a la función, Resultado: ", test2)
