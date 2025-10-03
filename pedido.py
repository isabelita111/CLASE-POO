from dataclasses import dataclass, field
from typing import List
from clasesabstractas import Cliente, lineaFactura, Prouducto
from descuentos import Descuento
from impuestos import Impuesto

@dataclass

class Factura: 
    cliente : Cliente
    lineas : list[lineaFactura] = field(default_factory=list)

    def agregar_linea(self, producto, cantidad= 1):
        self.linea.append (lineaFactura(producto, cantidad))
    
    def calcular_descuentos(self, descuento: Descuento):
        return sum(descuento.aplicar(self.cliente, 1) for 1 in self.lineas)
    
    def calcular_impuestos(self, impuestos: Impuesto):
        return sum(impuestos.calcular(self.cliente, 1)for 1 in self.lineas)
    def calcular_total(self, descuento: Descuento, impuestos: Impuesto):
        return sum(1.subtotal for 1 in self.lineas) + self.calcular_impuesto(impuestos) - self.calcular_descuento(descuento)