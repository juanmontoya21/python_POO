import math
class RaizCuadrada:
    def __init__(self,radicando):
        self.radicando = radicando
    
    def calcularRaiz(self):
        if self.radicando < 0:
            print("el numero ingresado no puede ser negativo")
        else:
            print(f"la raiz cuadrada de {self.radicando} es {round(math.sqrt(self.radicando))} ")

numero = RaizCuadrada(8)
numero.calcularRaiz()