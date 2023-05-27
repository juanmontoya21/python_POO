class Triangulo:
    def __init__(self,lado1,lado2,lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def Mayor(self):
        mayor = [self.lado1,self.lado2,self.lado3]
        print(f"el lado de mayor tamaño es {max(mayor)}")

    def Tipo(self):
        if self.lado1 == self.lado2 and self.lado2 == self.lado3:
            print("es un triangulo equilatero")
        elif self.lado1 == self.lado2 or self.lado2 == self.lado3:
            print("es un triangulo isoceles")
        else:
            print("es un triangulo escaleno")
            
tirangulo1 = Triangulo(3,4,2)
tirangulo1.Tipo()
tirangulo1.Mayor()