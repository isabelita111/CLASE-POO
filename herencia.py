class Animal:
    def __init__(self,nombre):
        self.nombre= nombre
    def hacer_sonido(self):
        print(f"{self.nombre} hace un sonido")
            pass
class Perro(Animal):
    def __init__(self,nombre, color_pelota):
    def hacer_sonido(self):
        print(f"{self.nombre} hace guau guau") 
    def salir_a_pasear(self):
        print(f"{self.nombre} esta paseando")
class Gato(Animal):
    def hacer_sonido(self):
        print(f"{sef.nombre}hace miau miau")

animal1= Perro("Mia")
animal1.hacer_sonido()
animal1.salir_a_pasear()
animal1.orinar()
animal2 = Gato("lalito")
animal2.hacer_sonido()
animal2.salir_a_pasear()
animal2.orinar()