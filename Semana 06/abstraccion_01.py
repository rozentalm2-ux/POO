# Importamos para usar clases y métodos abstractos
from abc import ABC, abstractmethod

# Clase abstracta Animal 
class Animal(ABC):
    # Constructor de la clase Animal
    def __init__(self, nombre, edad, tamaño):
        # Atributos
        self.nombre = nombre
        self.edad = edad
        self.tamaño = tamaño
        
    # Método abstracto
    @abstractmethod
    def datos(self):
        pass  
    

# Clase Perro que hereda de Animal
class Perro(Animal):
    # Constructor de Perro 
    def __init__(self, nombre, edad, tamaño, color):
        # Llamamos al constructor de la super clase (Animal)
        super().__init__(nombre, edad, tamaño)
        self.color = color  # Agregamos ese atributo
        
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

