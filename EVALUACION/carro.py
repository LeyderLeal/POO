class Carro:
    def __init__(self, placa, color):
        self.__placa = placa
        self.color = color
        
    def getPlaca(self):
        return self.__placa
    
    def setPlaca(self,placa):
        self.__placa = placa