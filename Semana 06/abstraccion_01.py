# Importamos lo necesario para usar clases y métodos abstractos
from abc import ABC, abstractmethod

# Clase abstracta Animal (hereda de ABC para definir métodos abstractos)
class Animal(ABC):
    # Constructor de la clase Animal
    def __init__(self, nombre, edad, tamaño):
        # Atributos comunes para todos los animales
        self.nombre = nombre
        self.edad = edad
        self.tamaño = tamaño
        
    # Método abstracto: las subclases deben implementarlo obligatoriamente
    @abstractmethod
    def datos(self):
        pass  # Aquí solo se declara, no se implementa
    

# Clase Perro que hereda de Animal
class Perro(Animal):
    # Constructor de Perro (agregamos un atributo extra: color)
    def __init__(self, nombre, edad, tamaño, color):
        # Llamamos al constructor de la clase padre (Animal)
        super().__init__(nombre, edad, tamaño)
        self.color = color  # Atributo propio de Perro
        
    # Implementación del método abstracto "datos"
    def datos(self):
        # Retorna un texto con la información del animal
        return f"""DATOS DEL ANIMAL
    NOMBRE = {self.nombre}
    EDAD   = {self.edad} años
    TAMAÑO = {self.tamaño}
    COLOR  = {self.color}"""
    

# Creación de un objeto de la clase Perro
object1 = Perro("Boby", 10, "Grande", "Rosado")

# Imprimimos los datos del animal usando el método sobrescrito
print(object1.datos())
