from empleado import Empleado
class Contratista(Empleado):
    def __init__(self, cedula, nombres, apellidos, correo, fechaIngreso, cargo,valorHoras):
        super().__init__(cedula, nombres, apellidos, correo, fechaIngreso, cargo)
        self.__valorHoras=valorHoras
        self.__salario=0
        
    def getValorHoras(self):
        return self.__valorHoras
    def getEmpleadosContratistas(self):
        return self.__empleadosContratistas
    
    def setValorHoras(self,valorHoras):
        self.__valorHoras=valorHoras
        
    def salarioMensual(self,horasTrabajadas=None):
        self.__salario=self.__valorHoras*horasTrabajadas
        return self.__salario
    
        
    