import datetime
from cliente import Cliente

class Venta():
    def __init__(self,cliente=Cliente):
        self.__fecha = datetime.datetime.now()
        self.__cliente=cliente
        self.__listaDetalleVenta=[]
    
    def agregarDetalleVenta(self,detalleVenta):
        self.__listaDetalleVenta.append(detalleVenta)
        
    def getFecha(self):
        return self.__fecha
    
    def getCliente(self):
        return self.__cliente
    
    def getListaDetalleVenta(self):
        return self.__listaDetalleVenta
    
    def setFecha(self,fecha):
        self.__fecha=fecha
        
    def setCliente(self,cliente):
        self.__cliente=cliente
    
    def setListaDetalleVenta(self,listaDetalleVenta):
        self.__listaDetalleVenta=listaDetalleVenta
    
    def valorTotal(self):
        total = 0
        for detalleVenta in self.getListaDetalleVenta():
            total += detalleVenta.calcularTotal()
        return total
        
        