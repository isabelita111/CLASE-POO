#Crear lista
"""mis_lista=["primer elemento", "segundo elemento", "tercer elemento"]
print(mis_lista[:2])

#crear lista con ceros
lista_ceros= [0]* 10
print(lista_ceros)
"""
#numeros aleatorios
import random 
listaaleatoria=[]
for i in range (0, 10):
    listaaleatoria.append(random.randint(1,100))
print(listaaleatoria)

listaaleatoria2=[random.randint(1, 100)for _ in range (10)]
print(listaaleatoria2)

#poaicioes del q al 10
lista_ejemplo = [i for i in range (0, 10)]
print(lista_ejemplo)


lista lista_ejemplo[2] = 10
lista_ejemplo[5]= 2
print(lista_ejemplo)
#remueve el valor del parentesis
##print(lista_ejemplo)

#eliminar por posicion
#del lista_ejemplo[2]
#print(lista_ejemplo)
"""
lista_ejemplo = [elemento for elemento in lista_ejemplo if elemento != 1]
print(lista_ejemplo)

lista_ejemplo.reverse()
print(lista_ejemplo)

lista_ejemplo.short()
print(lista_ejemplo)

lista_ejemplo.short(reverse=True)
print(lista_ejemplo)
"""
import random
class persona:
    def __init__(self, nombre):
        self.nombre= nombre
        self.numeros= [random.randint(100, 999) for _ in range(5)]

    persona1= persona("Isabella")
    persona2= ("jeronio")

    print("los numeros para", persona1.nombre, "son", persona1.numeros )
    print("los numeros para", persona2.nombre, "son", persona2.numeros )

