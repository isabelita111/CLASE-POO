class Cuenta:
    def __init__(self,ususario, numero_cuenta):
        self.ususario= ususario
        self.nueva_cuenta= nueva_cuenta
        self.saldo= 0

    def depositar(self, cantidad):
        self.saldo = self.saldo + cantidad
        return self.saldo

    def retirar(self, saldo):
        if self.saldo >= cantidad:
            self.saldo = self.saldo - cantidad
            return self.saldo
        else:
            print("Dinero insuficiente para el retiro")
            return -1

    def consultar(self):
        return self.saldo

#programa principal
Cuentas = []

print("Bienvenido al banco trululu")
while True:
    print("INGRESE LA OPCION DESEADA")
    print("1. Registrar cuenta")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Consultar saldo")
    print("0. Salir")
    
    opcion = int(input())

    if opcion == 1:
        nombre = input("ingrese el nobre del titular")
        numero_cuenta = int(input("ingrese nuero de cuenta"))
        nueva_cuenta = Cuenta(ususario, numero_cuenta)
        Cuentas.append(nueva_cuenta)
        print("Cuenta creada exitosamente")
    
    elif opcion== 2:
        numero_cuenta = int(input("ingrese el numero de cuenta"))
        
    
    elif opcion == 3:
        numero_cuenta = int(input("ingrese numero de cuenta"))
        existe = False
        for cuenta in Cuentas:
            if cuenta.numero_cuenta == numero_cuenta:
                existe = True
                cantidad = float(input("INGRESE LA CANTIDAD A RETIRAR"))
                nuevo_saldo = cuenta.retirar(cantidad)

                if nuevo_saldo  >= 0:
                    print ("retiro exitoso, su nuevo saldo es," nuevo_saldo)
        if existe == False:
            print("La cuenta no exite")
    
    elif opcion == 4:
        numero_cuenta = int(input("ingrese numero de cuenta"))
        existe = False
        for cuenta in Cuentas:
            if cuenta.numero_cuenta ==

