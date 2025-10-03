from abc import ABC, abstractmethod
from typing import  List
from clasesabstractas import Cliente, lineaFactura

class Impuesto(ABC):
    @abstractmethod
    def calcular(self, cliente: Cliente, linea: lineaFactura):
        ...
class IVA(Impuesto): 
    def calcular(self, cliente: Cliente, linea: lineaFactura):
        if linea.producto.categoria == "alimentos":
            return 0.0

class Excentos (Impuesto):
    def calcular(self, cliente: Cliente, linea: lineaFactura):
        return linea.subtotal * 0.08 if linea.producto.categoria != 'servicios' else 0.0 