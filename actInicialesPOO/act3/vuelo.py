from pasajero import Pasajero

class Vuelo():

    def __init__(self,numero=None, fecha=None, ciudadOrigen=None, ciudadDestino=None):
        self.__numero=numero
        self.__fecha=fecha
        self.__ciudadOrigen=ciudadOrigen
        self.__ciudadDestino=ciudadDestino
        self.__listaPasajeros=[]

    def getNumero(self):
        return self.__numero

    def getFecha(self):
        return self.__fecha

    def getCiudadOrigen(self):
        return self.__ciudadOrigen

    def getCiudadDestino(self):
        return self.__ciudadDestino

    def getListaPasajeros(self):
        return self.__listaPasajeros

    def setNumero(self,numero):
        self.__numero=numero

    def setFecha(self,fecha):
        self.__fecha=fecha

    def setCiudadOrigen(self,ciudadOrigen):
        self.__ciudadOrigen=ciudadOrigen

    def setCiudadDestino(self,ciudadDestino):
        self.__ciudadDestino=ciudadDestino

    def agregarPasajero(self, nombre=None, correo=None):
        """[summary]
            Permite agregar un pasajero al vuelo
        Args:
            nombre ([string]): [Nombre de la persona]
            correo ([string]): [Correo de la Persona]
        """
        pasajero = Pasajero(nombre,correo)
        self.__listaPasajeros.append(pasajero)
        
    def agregarPasajero2(self, pasajero=None):
        """_summary_

        Args:
            pasajero (_type_, optional): _description_. Defaults to None.
        """
        self.__listaPasajeros.append(pasajero)

    

