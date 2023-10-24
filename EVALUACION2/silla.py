from persona import Persona

class Silla():
    def __init__(self,numero=int):
        """_summary_
            Constructor con parametro de inicializacion 
            Al iniciar su atributo persona es None y su estado
            es disponible
        Args:
            numero (_type_, optional): numero que identifica la silla. Defaults to int.
        """
        self.__numero=numero
        self.__persona=None
        self.__estado='DISPONIBLE'
        
    def getNumero(self):
        return self.__numero
    
    def getPersona(self):
        return self.__persona
    
    def getEstado(self):
        return self.__estado
    
    def setPersona(self,persona:Persona):
        self.__persona = persona
        
    def setEstado(self):
        """
            Modifica el estado     
        """
        if(self.__estado=='DISPONIBLE'):
           self.__estado='OCUPADO'
        else:
            self.__estado='DISPONIBLE'
        