"""
class Persona:
    def __init__(self, nombre, cedula, ti):
        self.nombre= nombre
        self.__cedula= cedula
        self.__ti = ti
    def obrener_documento(self): #encapsulamiento
        if self.__cedula is not None:
            return self.__cedula 
        else: 
            return self.__ti

Persona1= Persona("juan", 1111)
Persona2 = Persona("Maria", 2222)

print ("el nombre de la persona es ", Persona1.nombre)
print("La cedula de la persona 1 es ", Persona1.obrener_documento())

print("el nombre de la segunda persona es ", Persona2.nombre)
print("la cedula de la persona 2 es ", Persona2.obrener_documento())
"""

class Dispositivo:
    def __init__(self, nombre):
        slef.nombre = nombre
        self.estado = False
    def encender(self):
        slef.estado = True 
        print(self.nombre , ": encendido")
    def agregar (self):
        self.estado = False 
        print(self.nombre , ": apagado")

class Espacio:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__dispositivos =[]
    def agreare(self, dispositivo):
        self.__espacios.append(Espacio(nombre))
    def mostrar(self):
        for espacio in self.__espacios:
            print(espacio.nombre)

mi_casa = Casa("calle 123")
mi_casa.agreare("cocina")
mi_casa.agreare("habitacion")
mi_casa.agreare("bano")
television = Dispositivo("television")