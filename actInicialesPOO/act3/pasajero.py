class Pasajero():

    def __init__(self,nombre=None, correo=None):
        self.__nombre=nombre
        self.__correo=correo

    def getNombre(self):
        return self.__nombre

    def getCorreo(self):
        return self.__correo

    def setNombre(self,nombre):
        self.__nombre=nombre

    def setCorreo(self,correo):
        self.__correo=correo
