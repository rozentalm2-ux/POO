#Definiendo la Super Clase llamada Saiyajin

class Saiyajin:
    
#Se define el metodo constructor    

    def __init__(self, nombre, ki, tecnica):
        self.nombre = nombre
        self.ki = ki
        self.tecnica = tecnica
        
#Se define el metodo str que nos ayuda para presentar cadenas de texto  

    def __str__(self):
        return f"""
    ----- DATOS DE GUERRERO -----
    NOMBRE: {self.nombre}
    NIVEL DE KI: {self.ki}
    TECNICA BASICA: {self.tecnica}"""
    
#Definiendo la Sub Clase "Transformación" que heredará los atributos de Saiyajin
   
class Tranformacion(Saiyajin):
    def __init__(self, nombre, ki, tecnica, transformacion):
        super().__init__(nombre, ki, tecnica)
        self.transformacion = transformacion

#Usamos el metodo str para mostrar los datos de la sub clase y concatenar con los datos de la Super Clase

    def __str__(self):
        return super().__str__() + f"""
    TRANSFORMACION = {self.transformacion}"""
    
#Definimos los objetos, en este caso son object1 = "Goku" y object2= "Vegeta"

object1 = (Saiyajin("Goku",5000,"Kamehameha"))
object2 = (Tranformacion("Vegeta",4000,"Big Bang","SSJ BLUE"))

#Usando la función print llamamos a nuestros objetos para mostrar los datos 

print(object1)
print(object2)