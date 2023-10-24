class Empleado():
    def __init__(self, cedula, nombres, apellidos, correo, cargo, fechaIngreso):
        self.__cedula = cedula
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__correo = correo
        self.__fechaIngreso = fechaIngreso
        self.__cargo = cargo
        
    
    def getCedula(self):
        return self.__cedula
    def getNombres(self):
        return self.__nombres
    def getApellidos(self):
        return self.__apellidos
    def getCorreo(self):
        return self.__correo
    def getFechaIngreso(self):
        return self.__fechaIngreso
    def getCargo(self):
        return self.__cargo
    
    def setCedula(self,cedula):
        self.__cedula
    def setNombres(self,nombres):
        self.__nombres
    def setApellidos(self,apellidos):
        self.__apellidos
    def setCorreo(self,correo):
        self.__correo
    def setFechaIngreso(self,fechaIngreso):
        self.__fechaIngreso
    def setCargo(self,cargo):
        self.__cargo