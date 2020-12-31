# Estructura de la clase para crear objetos persona
class Person:
    # Atributos de la persona
    arms=0
    legs=0
    eyes=0
    name=""
    
    # Inicializador o contructor
    # -El atributo self hace referencia hacia si mismo
    def __init__(self,name="Indefinido"):        
        self.arms=2
        self.legs=2
        self.eyes=2
        self.name=name
        print("Soy una persona recien creada...")
    # Funciones y/o métodos
    def salute(self):
        return "Hola!, mi nombre es: "+self.name

# Uso de la clase para crear objetos personas
humanoidA=Person()
humanoidB=Person("C-3PO")

# Uso de los objetos creados
print("Hey humanoide 1 saluda:\n",humanoidA.salute())
print("Hey humanoide 2 saluda:\n",humanoidB.salute())



