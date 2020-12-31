# Estructura de la clase para crear objetos persona
class Person:
    # Atributos de la persona
    arms = 0
    legs = 0
    eyes = 0
    name = ""
    # Inicializador o contructor
    # -El atributo self hace referencia hacia si mismo
    def __init__(self, name="Indefinido"):
        self.arms = 2
        self.legs = 2
        self.eyes = 2
        self.name = name
        print("Soy una persona recien creada...")
    # Funciones y/o métodos
    def salute(self):
        return "Hola!, mi nombre es: "+self.name

# Estructura de la clase mujer que hereda de persona
class Woman(Person):
    # Atributos de una mujer
    gender = "Mujer"

# Uso de la clase para crear objeto mujer que usa herencia de persona
humanoidA = Woman("Ivana")

# Uso de los objetos creados
print("Hey humanoide 1 saluda:\n", humanoidA.salute())

