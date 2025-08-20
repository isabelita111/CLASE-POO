"""
#creamos un diccionario 
agenda = {
    "Ana: "12345"
    "Bruno: "22220"
    "Carla: "33330"
}

#MOSTRAR EL NUMERO DE CONTACTO ESPECIFICO
agenda ["carla"] = 
nombre = input ("ingrese el de nombre de la persona")

if nombre in agenda:
    print("telefono de : ", +nombre, agenda[nombre])
else:
    print("no existe")
"""

inventario = {
    "cuaderno" : 15,
    "lapiz" : 40, 
    "borraor" : 0,
    "marcador" : 10,
    "regla" : 5, 
}

while True:
    print("Bienvenidios a la papeleria")
    print("1. agregar producto")
    print("2. vender pruducto")
    print ("3. salir del sistema")

    opcion = input ("elige una opcion")

    if opcion == 1:
        nombreproducto = input ("ingrese el nombre del producto ") 