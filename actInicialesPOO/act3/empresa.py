from vuelo import Vuelo

class Empresa():

    def __init__(self,nombre=None):
        self.__nombre=nombre
        self.__listaVuelos=[]

    def getNombre(self):
        return self.__nombre

    def getListaVuelos(self):
        return self.__listaVuelos

    def setNombre(self,nombre):
        self.__nombre=nombre

    def registrarVuelo(self, numero=None,fecha=None,ciudadOrigen=None, ciudadDestino=None):
        if(numero and fecha and ciudadOrigen and ciudadDestino):
            unVuelo = Vuelo(numero,fecha,ciudadOrigen,ciudadDestino)
            self.__listaVuelos.append(unVuelo)
        else:
            return False