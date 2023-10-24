from empleado import Empleado
class Planta(Empleado):
    def __init__(self, cedula, nombres, apellidos, correo, fechaIngreso, cargo,sueldoBasico):
        super().__init__(cedula, nombres, apellidos, correo, fechaIngreso, cargo)
        self.__sueldoBasico=sueldoBasico
        self.__salario=0
        
    def getSueldoBasico(self):
        return self.__sueldoBasico
      
    def setSueldoBasico(self,sueldoBasico):
        self.__sueldoBasico=sueldoBasico
        
    def salarioMensual(self,diasTrabajados):
        salarioMensual=self.__sueldoBasico*diasTrabajados/30
        self.__salario=salarioMensual
        return self.__salario

        
    
    