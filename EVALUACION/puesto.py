from  carro import Carro
class Puesto:
    def __init__(self, numero):
        self.__numero = numero
        self.estado = 'DISPONIBLE'
        self.carro = None

    def ocupar(self, carro):
        self.estado = "OCUPADO"
        self.carro = carro

    def desocupar(self):
        self.estado = "DISPONIBLE"
        carro = self.carro
        self.carro = None
        return carro
        
    def getNumero(self):
        return self.__numero
    
    def getCarro(self):
        return self.carro
    
    def setNumero(self,numero):
        self.__numero = numero
        
    def setCarro(self,carro):
        self.carro = carro
        
    