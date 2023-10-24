class Cliente():
    def __init__(self,nombre,direccion,correo):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__correo = correo
        
    def getNombre(self):
        return self.__nombre
    
    def getdireccion(self):
        return self.__direccion
    
    def getCorreo(self):
        return self.__correo
    
    def setNombre(self,nombre):
        self.__nombre = nombre
        
    def setDireccion(self,direccion):
        self.__direccion = direccion
    
    def setCorreo(self,correo):
        self.__correo = correo