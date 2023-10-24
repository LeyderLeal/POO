class Persona():
    
    def __init__(self, identificacion=str, nombre=str, correo=str, genero=str):
        """_summary_
                Constructor con parametros de inicializacion
        Args:
            identificacion (_type_, optional): documento de identidad str.
            nombre (_type_, optional): nombre completo de la persona str.
            correo (_type_, optional): correo electronico de la persona str.
            genero (_type_, optional): Femenino o masculino str.
        """
        self.__identificacion = identificacion
        self.__nombre = nombre
        self.__correo = correo
        self.__genero = genero
        
    def getIdentificacion(self):
        return self.__identificacion
    
    def getNombre(self):
        return self.__nombre
    
    def getCorreo(self):
        return self.__correo
    
    def getGenero(self):
        return self.__genero