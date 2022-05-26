class Personaje:
    # Constructor de la clase Personaje
    # El constructor inicializa los atributos y métodos de mi clase
    def __init__(self,nombre,colorTraje,tipo):

        # Atributos = Datos = Variables
        self.nombre=nombre
        self.colorTraje=colorTraje
        self.tipo=tipo  
    
    # Métodos = Acciones = Funciones
    def saludar(self):
        print("Hola...")