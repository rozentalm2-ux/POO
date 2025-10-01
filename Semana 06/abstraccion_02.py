# Importamos las herramientas necesarias para crear clases abstractas
from abc import ABC, abstractmethod

# Clase abstracta Vehiculo (hereda de ABC para poder definir métodos abstractos)
class Vehiculo(ABC):
    # Constructor de la clase Vehiculo
    def __init__(self, dueño, marca, año):
        # Atributos comunes para todos los vehículos
        self.dueño = dueño
        self.marca = marca
        self.año = año
        
    # Método abstracto: las subclases estarán obligadas a implementarlo
    @abstractmethod
    def datos(self):
        pass  # Aquí no se implementa nada, solo se define la "plantilla"
    

# Clase Carro que hereda de Vehiculo
class Carro(Vehiculo):
    # Constructor de Carro (agregamos un atributo extra: color)
    def __init__(self, dueño, marca, año, color):
        # Llamamos al constructor de la clase padre (Vehiculo)
        super().__init__(dueño, marca, año)
        self.color = color  # Atributo propio de Carro
        
    # Implementación del método abstracto "datos"
    def datos(self):
        # Retorna un texto con la información del vehículo
        return f"""DATOS DEL VEHICULO
    NOMBRE = {self.dueño}
    MARCA  = {self.marca} 
    AÑO    = {self.año}
    COLOR  = {self.color}"""
    

# Creación de un objeto de la clase Carro
object1 = Carro("Johan", "Toyota", 2020, "Rojo")

# Imprimimos los datos del vehículo usando el método sobrescrito
print(object1.datos())
