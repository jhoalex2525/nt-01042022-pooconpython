# Importar una clase
from Personaje import Personaje

# Utilizar una clase, por tanto creo un objeto
# Un objeto es una variable que hereda los atributos y métodos de la clase
personaje=Personaje("Batman","Negro","Héroe")

# Acceder a los atributos de mi objeto
print(personaje.nombre)

# Acceder a los métodos de mi objeto
personaje.saludar()