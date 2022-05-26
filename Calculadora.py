class Calculadora:
    # Constructor
    def __init__(self,num1,num2):
        # Atributos
        self.num1=num1
        self.num2=num2
    
    # Métodos
    def sumar(self):
        return(self.num1+self.num2)        
    def restar(self):
        return(self.num1-self.num2)
    def multiplicar(self):
        return(self.num1*self.num2)
    def dividir(self):
        return(self.num1/self.num2)