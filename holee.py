
class perro:
    def __init__(self,nombre,raza):
        self.nombre= nombre
        self.raza= raza
    
    def ladrar(self):
        print("el perro que esta ladrando es: ", self.nombre)

class persona:
    def _init_(self,nombre, edad, sexo):
        self.nombre = nombre 
        self.edad = edad
        self.sexo = sexo

print("Hola")

#vamos a instancar un objeto desde la clase perro
print("mi primer perrito")
mi_perrito = perro("Alaska", "Pomsky")
print(mi_perrito.nombre)
print(mi_perrito.raza)

print("mi segundo perrito")
mi_otro_perrito = perro("coquito", "husky")
print(mi_otro_perrito.nombre)
print(mi_otro_perrito.raza)

print("ingrese los datos de tu peludito")
nombre= input("ingrese el nombre de tu perrito")
raza= input("ingrese la raza de tu perrito")

mi_tercer_perrito = perro(nombre, raza)
print("este son los datos de tu peludito")
print(mi_tercer_perrito.nombre)
print(mi_tercer_perrito.raza)

print("ahora los perros van a ladrar")
mi_perrito.ladrar()
mi_otro_perrito.ladrar()
mi_tercer_perrito.ladrar()

"""