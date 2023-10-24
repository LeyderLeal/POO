class Carro():
    def __init__(self,placa=str, color=str):
        """_summary_
            Constructor con parametris de inicializacion
        Args:
            placa (_type_, optional): id carro.
            color (_type_, optional): color carro.
        """
        self.__placa=placa
        self.__color=color
        
    def getPlaca(self):
        return self.__placa
    
    def getColor(self):
        return self.__color