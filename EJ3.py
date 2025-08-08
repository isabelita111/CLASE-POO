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