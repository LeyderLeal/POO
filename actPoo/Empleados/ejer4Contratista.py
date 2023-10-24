from ejer4Empleado import Empleado
class Contratista(Empleado):
    
    def __init__(self, cedula, nombres, apellidos, correo, cargo, fechaIngreso, valorHora):   
        super().__init__(cedula,nombres,apellidos,correo,cargo,fechaIngreso)
        self.__valorHora = valorHora
        self.__salario=0

    def getvalorHora(self):
        return self.__valorHora
    
    def setValorHoras(self, valorHora):
        self.__valorHora = valorHora
        
    def calcularSalarioMes(self, horasTrabajadas):
        self__salario = float(self.__valorHora * horasTrabajadas)
        return self.__salario