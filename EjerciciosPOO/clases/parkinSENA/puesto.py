from carro import Carro

class Puesto():
    def __init__(self,numero=int):
        """_summary_
            Constructor con numero de puesto
        Args:
            numero (_type_, optional): Numero de puesto
        """
        self.__numero=numero
        self.__estado="Disponible"
        self.__carro=None
        
    def getNumero(self):
        return self.__numero
    
    def getEstado(self):
        return self.__estado
    
    def getCarro(self):
        return self.__carro
    
    def setCarro(self,carro:Carro):
        self.__carro=carro
        if(carro ==None):
            self.__estado="Disponible"
        else:
            self.__estado="Ocupado"    
    