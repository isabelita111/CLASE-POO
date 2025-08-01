class Estudiante:
    def __init__(self, nombre, edad, nota1, nota2, nota3):
        self.nombre = nombre
        self.edad = edad
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def mostrar_datos(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)
        print("Nota1: ", self.nota1)
        print("Nota2: ", self.nota2)
        print("Nota3: ", self.nota3)

    def calcular_promedio(self):
        promedio = (self.nota1 + self.nota2 + self.nota3) / 3
        return promedio

print("Bienvendio  la gestion de estudiantes")
lista_estdiantes= []
while True:
    print("ingrese la opcion deseada")
    print("1. Agregar estudiante")
    print("2. Mostrar info del estudainte")
    print("0. salir")
    opcion = int(input())
    if opcion == 1:
        print("Ingrese el nombre del estudiante")
        nombre = input()
        print("Ingrese la edad del estudiante")
        edad = int(input())
        print("Ingrese la primera nota del estudainte")
        nota1 = float(input())
        print("Ingrese la segunda nota del estudainte")
        nota2 = float(input())
        print("Ingrese la tercera nota del estudainte")
        nota3 = float(input())
        estudiante = Estudiante(nombre, edad, nota1, nota2, nota3)
        lista_estdiantes.append(estudiante)
    elif opcion == 2:
        numeroEstudiantes= len(lista_estdiantes)
        print("el numero e estudiante es:", numeroEstudiantes)
        for estudiante in lista_estdiantes:
            print("el nombre del estudiante es ", estudiante.nombre)
            print("el promedio del estudiante es: ", estudiante.calcular_promedio())
    elif opcion == 0:
        print ("hasta luego")
        break
    else:
        print("opcion no valida")
