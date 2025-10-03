from abc import ABC, abstractmethod
from typing import  List
from clasesabstractas import Cliente, lineaFactura

class Descuento(ABC):
    @abstractmethod
    def aplicar(self, cliente, lineaFactura) -> float:
        ...
class sindescuento(Descuento):
    def aplicar(self, cliente: Cliente, linea: lineaFactura) -> float:
        return 0.0
class DescuentoVIP(Descuento):
     def aplicar(self, cliente: Cliente, linea: lineaFactura) -> float:
         return 0.10 * linea.subtotal if cliente.vip == True else 0.0
class Descuentovolumen(Descuento):
     def aplicar(self, cliente: Cliente, linea: lineaFactura) -> float:
         return 0.15 * linea.subtotal if linea.cantidad >= 10 else 0.0
