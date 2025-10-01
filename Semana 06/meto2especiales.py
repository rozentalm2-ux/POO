class Pokemon():
    def __init__(self, nombre, tipo, nivel):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel
        
    def saludar(self):
        return f"""Hola me llamo {self.nombre}"""
    
    def __str__(self):
        return f"""Soy un Pokemon de tipo {self.tipo}"""
    
    def __repr__(self):
        return f"""CLASE: POKEMON
    ATRIBUTOS:
    NOMBRE = {self.nombre} (String) - Not null
    TIPO = {self.tipo} (String) - Not null
    NIVEL = {self.nivel} (Integer) - Not null"""
    
object1 = Pokemon("Pikachu","Electrico", 10)

print(object1.__repr__())