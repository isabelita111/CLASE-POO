class Estudiante:
    def __init__(self, nombre, edad, nota):
        self.nombre = nombre
        self.edad = edad
        self.nota = nota

class Profesor:
    def __init__(self, nombre, edad, experiencia):
        self.nombre = nombre
        self.edad = edad
        self.experiencia = experiencia


class GrupoAsignatura:
    def __init__(self, nombre, horario, codigo, profesor):
        self.nombre = nombre
        self.horario = horario
        self.codigo = codigo
        self.profesor = profesor
        self.estudiante = []

    def Agregar_estudiante(self, estudiante):
        self.estudiante.append(estudiante)
        print("estudiante agregado exitosamente")

    def promedio(self):
        acumulador= 0
        for estudiante in self.estudiante:
            acumulador = acumulador + estudiante.nota
            promedio = acumulador/len(self.estudiante)
            return promedio 
    def mostrarasignatura(self):
        return "la cantidad de estudiantes es", len(self.estudiante)

profesor = Profesor("juan esteban", 35, 5)
poo = GrupoAsignatura("programacion orientada a objetos", "M-V 10-12", 62, profesor)
print(poo.profesor.nombre)
estudiante1 = Estudiante("esteban diaz", 17, 5)
estudiante2= Estudiante ("jorge", 20, 2.5)
estudiante3 = Estudiante("luis", 21, 3)

poo.Agregar_estudiante(estudiante1)

poo.Agregar_estudiante(estudiante2)

poo.Agregar_estudiante(estudiante3)

print(poo.promedio())
print (poo.mostrarasignatura())
