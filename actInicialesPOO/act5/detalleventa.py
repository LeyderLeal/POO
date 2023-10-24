class DetalleVenta:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad

    def calcular_total(self):
        return self.producto.precio * self.cantidad

    
    