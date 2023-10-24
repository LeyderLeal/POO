from contratista import Contratista
from planta import Planta
def contratarEmpleado():
    if z==1:
        cedula=input("Ingrese su Cedula ")
        nombres=input("Ingrese sus Nombre: ")
        apellidos=input("Ingrese sus Apellidos: ")
        correo=input("Ingrese su Correo: ")
        fechaIngreso=input("Ingrese la Fecha de Ingreso(dd/mm/aaaa): ")
        cargo=input("Ingrese su Cargo: ")
        sueldoBasico=int(input("Ingrese el Sueldo Basico: "))
        planta=Planta(cedula,nombres,apellidos,correo,fechaIngreso,cargo,sueldoBasico)
        diasTrabajados=int(input("Ingrese los dias trabajados: "))
        salario=planta.salarioMensual(diasTrabajados)
        print(f"el empleado {planta.getNombres} en el cargo de {planta.getCargo} tiene un salario de {salario}")
    if z==2:
        cedula=input("Ingrese su Cedula ")
        nombres=input("Ingrese sus Nombre: ")
        apellidos=input("Ingrese sus Apellidos: ")
        correo=input("Ingrese su Correo: ")
        fechaIngreso=input("Ingrese la Fecha de Ingreso(dd/mm/aaaa): ")
        cargo=input("Ingrese su Cargo: ")
        valorHoras=int(input("Ingrese el Valor de las Horas: "))
        contratista=Contratista(cedula,nombres,apellidos,correo,fechaIngreso,cargo,valorHoras)
        horasTrabajadas= int(input("Ingrese las horas trabajadas: "))
        salario=contratista.salarioMensual(horasTrabajadas)
        print(f"el empleado {contratista.getNombres()} en el cargo de {contratista.getCargo()} tiene un salario de {salario}")
x=0

while(x!=2):
    z=0
    print("1. Contratar Empleado")
    print("2. Regresar")
    x=int(input("Ingrese Opción (1-2): "))
    if x==1:
        while(z!=3):
            print("1. Contratar Empleado de Planta")
            print("2. Contratar Empleado Contratista")
            print("3. Regresar")
            z=int(input("Ingrese Opción (1-3): "))
            if z==1 or z==2:
                contratarEmpleado()