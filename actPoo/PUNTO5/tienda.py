from producto import Producto
class Tienda():

    def __init__(self, nombre):
        self.__nombre = nombre
        self.__listaClientes= []
        self.__listaProductos= []
        self.__listaVentas= []

    def getNombre(self):
        return self.__nombre

    def getListaClientes(self):
        return self.__listaClientes
    
    def getListaProductos(self):
        return self.__listaProductos
    
    def getListaVentas(self):
        return self.__listaVentas

    def setNombre(self,nombre):
        self.__nombre=nombre
    
    def setListaClientes(self,ListaClientes):
        self.__listaClientes=ListaClientes

    def setListaProductos(self,listaProductos):
        self.__listaProductos=listaProductos
        
    def setListaVentas(self,listaVentas):
        self.__listaVentas= listaVentas
        
    def agregarProducto(self, producto):
        self.__listaProductos.append(producto)