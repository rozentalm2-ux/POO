# Importamos para crear clases abstractas
from abc import ABC, abstractmethod

# Clase abstracta Vehiculo 
class Vehiculo(ABC):
    # Constructor de la clase Vehiculo
    def __init__(self, dueño, marca, año):
        # Definimos atributos
        self.dueño = dueño
        self.marca = marca
        self.año = año
        
    # Método abstracto
    @abstractmethod
    def datos(self):
        pass  
    

# Clase Carro que hereda de Vehiculo
class Carro(Vehiculo):
    # Constructor de Carro 
    def __init__(self, dueño, marca, año, color):
        # Llamamos al constructor de la Super Clase (Vehiculo)
        super().__init__(dueño, marca, año)
        self.color = color  # Añadimos un atributo
        
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

