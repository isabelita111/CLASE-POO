class Registro:
    def __init__(self, tipo, cantidad, valor_unitario):
        self.tipo = tipo
        self.cantidad = cantidad
        self.valor_unitario = valor_unitario
class Factura:
    def __init__(self,codigo):
        self.codigo = codigo
        self.registros =[]
        self.total = 0 

    def agregar_registro(self, tipo, cantidad, valor_unitario):
        nuevo_registro = Registro(tipo, cantidad, valor_unitario)
        self.registros.apppend(nuevo_registro)
        self.total = self.total+ (registro.cantidad * registro.valor_unitario)

mi_Factura = Factura("12345")
registro1 = Registro("gaseosa", 5, 2500)
registro2= Registro("arepas", 3, 2500)
mi_Factura.agregar_registro(registro1)
mi_factura.agregar_registro(registro2)
print("el total es", mi_factura.total)