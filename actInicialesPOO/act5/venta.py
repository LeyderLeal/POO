import datetime

class Venta:
    def __init__(self, cliente):
        self.cliente = cliente
        self.detalles = []
        self.fecha = datetime.datetime.now()

    def agregar_detalle(self, detalle):
        self.detalles.append(detalle)

    def calcular_total(self):
        total = 0
        for detalle in self.detalles:
            total += detalle.calcular_total()
        return total

