class Estudiante:
    def __init__(self,Nombre,Nota):
        self.nombre = Nombre
        self.nota = Nota

    def Calificacion(self):
        if self.nota >= 3 and self.nota <= 5:
            print(f"{self.nombre} aprobaste con una nota de {self.nota}")
        else:
            print(f"{self.nombre} reprobaste con una nota de {self.nota}")

estudiante1 = Estudiante("Juan",3.9)
estudiante1.Calificacion()

        