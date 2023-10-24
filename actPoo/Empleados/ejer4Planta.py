from ejer4Empleado import Empleado
class Planta(Empleado):
    def __init__(self, cedula, nombres, apellidos, correo, cargo, fechaIngreso, sueldoBasico):
        super().__init__(cedula,nombres,apellidos,correo,cargo,fechaIngreso)
        self.__sueldoBasico = sueldoBasico
        # self.__valorHora = valorHora
    
    def getsueldoBasico(self):
        return self.__sueldoBasico
    
    def setsueldoBasico(self,sueldoBasico):
        self.__sueldoBasico = sueldoBasico
    
    def calcularSalarioMes(self, diasTrabajados):
        self.__salario = self.__sueldoBasico * diasTrabajados / 30
        return self.__salario