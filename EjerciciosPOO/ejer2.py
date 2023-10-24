class Persona():
    
    def __init__(self,identificacion,nombre,correo):
        """_summary_
            Constructor con parametros de inicialización
        Args:
            identificacion (str): # documento de identidad
            nombre (str): Nombre completo de la persona
            correo (str): Correo Electrónico de la Persona
        """
        self.__identificacion=identificacion
        self.__nombre=nombre
        self.__correo=correo
        
    def getIdentificacion(self):
        return self.__identificacion
    
    def setIdentificacion(self,identificacion):
        self.__identificacion=identificacion
        
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self,nombre):
        self.__nombre=nombre
        
    def getCorreo(self):
        return self.__correo
    
    def setCorreo(self,correo):
        self.__correo=correo
        
    def saludar(self):
        print(f"Desde persona...Hola soy un objeto de tipo {type(self).__name__}")
    
        
class Aprendiz(Persona):
    
    def __init__(self,identificacion,nombre,correo,puntajeIcfes):
        super().__init__(identificacion,nombre,correo)
        self.__puntajeIcfes = puntajeIcfes
        
    def getPuntajeIcfes(self):
        return self.__puntajeIcfes
    
    def setPuntajeIcfes(self, puntajeIcfes):
        self.__puntajeIcfes = puntajeIcfes
        
    def saludar2(self):
        print(f"Desde Aprendiz...Hola soy un objeto de tipo {type(self).__name__}")

class Instructor(Persona):
    
    def __init__(self,identificacion,nombre,correo,especialidad):
        super().__init__(identificacion,nombre,correo)
        self.__especialidad = especialidad
        
    def getEspecialidad(self):
        return self.__especialidad
    
    def setEspecialidad(self, especialidad):
        self.__especialidad = especialidad
        
    def saludar(self):
        print(f"Desde Instructor...Hola soy un objeto de tipo {type(self).__name__}")
        
aprendiz = Aprendiz(11,"JUan Lozano","jlozano@gmail.com",250)

print(aprendiz.getNombre())
print(aprendiz.getPuntajeIcfes())

aprendiz.saludar()

instructor = Instructor(12,"Carlos Cadena","ccadena@sena.edu.co","Desarrollo de Software")