from carro import Carro
from puesto import Puesto
from datetime import datetime

class Parqueo():
    def __init__(self,carro=Carro,puesto=Puesto):
        """_summary_
            Constructor parqueo. Se crea cuando un carro 
            ingresa al parqueadero y se actualiza cuando
            va a salir
        Args:
            carro (_type_, Carro): Carro que se va a parquear.
            puesto (_type_, Puesto): Puesto donde se parquea el carro.
        """
        self.__carro=carro
        self.__puesto=puesto
        self.__fechaHoraIngreso = datetime.now()
        self.__fechaHoraSalida = None
        
    def getCarro(self):
        return self.__carro
    
    def getPuesto(self):
            return self.__puesto
    
    def getFechaHoraIngreso(self):
            return self.__fechaHoraIngreso
    
    def getFechaHoraSalida(self):
            return self.__fechaHoraSalida
        
    def setFechaHoraSalida(self):
        self.__fechaHoraSalida=datetime.now()