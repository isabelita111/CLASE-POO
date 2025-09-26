class Empleado:
    def __init__(self, nombre, documento, edad):
        self.__nombre = nombre
        self.__documento = documento
        self.__edad = edad
    
    def mostrar_datos(self):
        return {"Nombre": self.__nombre, "Documento": self.__documento, "Edad": self.__edad}
"""
empleado1 = Empleado("juan", 11111, 36)
print(empleado1.mostrar_datos())
"""
class Desarrollador(Empleado):
    def __init__(self, nombre, documento, edad, tipo):
        super().__init__(nombre, documento, edad)
        self.__tipo = tipo
    def mostrar_datos(self):
        datos= super().mostrar_datos()
        datos["Tipo"]= self.__tipo
        return datos

empleado2= Desarrollador ("Isa", 1111, 17, "backend")
print(empleado2.mostrar_datos())

class Gerente(Empleado):
    def __init__(self, nombre, documento, edad, area):
        super().__init__(nombre, documento, edad)
        self.__area = area
        self.__empleado_a_cargo= []
    
    def mostrar_datos(self):
        datos = super().mostrar_datos()
        datos ["area"] = self.__area
        return datos
    def mostrar_empleado_a_cargo(self):
        for empleado in self.__empleado_a_cargo:
            print(empleado.mostrar_datos())
    def asignar_empleado(self, empleado):
        self.__empleado_a_cargo.append(empleado)

empleado1 = Gerente("Isaac", 2222, 5, "Desarrollador")
empleado2 = Desarrollador ("juan" , 1111, 30, "backend")
empleado3 = Empleado ("carlos", 3333, 20)
empleado1.asignar_empleado(empleado2)
empleado1.asignar_empleado(empleado3)