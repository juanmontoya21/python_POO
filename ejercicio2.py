class Persona:
    def __init__(self,Nombre,Edad):
        self.nombre = Nombre
        self.edad = Edad

    def VerificarEdad(self):
        if self.edad >= 18:
            print(f"{self.nombre} su edad es de {self.edad} por lo tanto es mayor de edad")
        else:
            print(f"{self.nombre} su edad es de {self.edad} por lo tanto es menor de edad")

Persona1 = Persona("juan",17)
Persona1.VerificarEdad()