"""
class Productos:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad 
    def vender(self, cantidad_vendida):
        if cantidad_vendida <= self.cantidad:
            self.cantidad -= cantidad_vendida
            print(f"se vendieron {cantidad_vendida} unidades de {self.nombre} ")
        else:
            print(f"no hay suficientes unidades de {self.nombre} solo quedan {self.cantidad}")
    def inventario(self):
        print(f"{self.nombre}: {self.cantidad} unidades disponibles")
    

print("Bienvendio  a la tienda de don Pacho")
productos =[]
def buscar_producto(nombre):
    for producto in productos:
        if producto.nombre.lower() == nombre.lower():
            return producto
    return None
while True:
    print("MENÚ DE LA TIENDA DE DON PACHO")
    print("1. Agregar producto")
    print("2. Vender producto")
    print("3. Mostrar inventario")
    print("4. Salir")

    opcion = input("Elige una opción: ")
    if opcion == "1" :
        nombre = input("Nombre del producto: ")
        precio = float(input("Precio del producto: "))
        cantidad = int(input("Cantidad disponible: "))
        productos.append(Productos(nombre, precio, cantidad))
        print("Producto agregado.")
    elif opcion == "2" :
        nombre = input("Nombre del producto a vender: ")
        producto = buscar_producto(nombre)
        if producto:
            cantidad = int(input("¿Cuántas unidades quieres vender?: "))
            producto.vender(cantidad)
        else:
            print("Producto no encontrado.")
    elif opcion == "3" :
        if not productos:
            print(" No hay productos registrados.")
        else:
            print("inventario de productos:")
            for p in productos:
                p.inventario()
    elif opcion == "4":
        print("Saliendo del sistema.")
        break
    else:
        print("Opción no válida.")
    """
    class Cuenta:
    def __init__(self, numero_cuenta, nombre, saldo):
        self.numero_cuenta = numero_cuenta
        self.nombre = nombre
        self.saldo = saldo
    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Se depositaron {monto} en la cuenta de {self.nombre}.")
        else:
            print("El monto debe ser mayor que cero.")
    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            print(f"Se retiraron ${monto} de la cuenta de {self.nombre}.")
        else:
            print(f"Fondos insuficientes. Saldo actual: ${self.saldo}")
    def mostrar_saldo(self):
        print(f"Cuenta: {self.numero_cuenta} Titular: {self.nombre} Saldo: ${self.saldo}")
    def buscar_cuenta(numero):
    for cuenta in cuentas:
        if cuenta.numero_cuenta == numero:
            return cuenta
    return None

cuentas=[]
while True:
    print(" SISTEMA BANCARIO")
    print("1. Crear nueva cuenta")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Consultar saldo")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        numero = input("Número de cuenta: ")
        if buscar_cuenta(numero):
            print("Esa cuenta ya existe.")
        else:
            titular = input("Nombre del titular: ")
            saldo_inicial = float(input("Saldo inicial (puede ser 0): "))
            nueva_cuenta = Cuenta(numero, titular, saldo_inicial)
            cuentas.append(nueva_cuenta)
            print("Cuenta creada con éxito.")

    elif opcion == "2":
        numero = input("Número de cuenta: ")
        cuenta = buscar_cuenta(numero)
        if cuenta:
            monto = float(input("Monto a depositar: "))
            cuenta.depositar(monto)
        else:
            print("Cuenta no encontrada.")

    elif opcion == "3":
        numero = input("Número de cuenta: ")
        cuenta = buscar_cuenta(numero)
        if cuenta:
            monto = float(input("Monto a retirar: "))
            cuenta.retirar(monto)
        else:
            print("Cuenta no encontrada.")

    elif opcion == "4":
        numero = input("Número de cuenta: ")
        cuenta = buscar_cuenta(numero)
        if cuenta:
            cuenta.mostrar_saldo()
        else:
            print("Cuenta no encontrada.")

    elif opcion == "5":
        print("Saliendo del sistema bancario. ¡Hasta luego!")
        break

    else:
        print("Opción inválida. Intenta de nuevo.")