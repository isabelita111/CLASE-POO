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