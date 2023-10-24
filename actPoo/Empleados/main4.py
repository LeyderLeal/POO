from ejer4Contratista import Contratista
from ejer4Planta import Planta

cedula = 11
nombres = "maria"
apellidos = "rojas"
correo = "maria@gmail.com"
cargo = "asistente"
fechaIngreso = "20/02/23"
valorHora = 32000

contratista = Contratista(cedula, nombres, apellidos, correo, cargo, fechaIngreso, valorHora)

horasTrabajadas = 22
sueldoContratista = contratista.calcularSalarioMes(horasTrabajadas)

print("Sueldo mes de enero")
print(f"Empleado: {contratista.getNombres()} {contratista.getApellidos()}")
print(f"Cargo: {contratista.getCargo()}")
print(f"Tipo empleado: {type(contratista).__name__}")
print(f"Valor hora: {contratista.getvalorHora()}")
print(f"Horas trabajadas: {horasTrabajadas}")
print(f"Salario mensual: {sueldoContratista}")
print("-------------------------------------------")
print(f"El salario mensual de {contratista.getNombres()} {contratista.getApellidos()} para \
      el mes de Enero es de : {sueldoContratista}")

cedula = 11
nombres = "andres"
apellidos = "nuñez"
correo = "andres@gmail.com"
cargo = "asistente"
fechaIngreso = "14/01/23"
sueldoBasico = 250000

planta = Planta(cedula, nombres, apellidos, correo, cargo, fechaIngreso, sueldoBasico)
horasTrabajadas = 20
diasTrabajados = 25
sueldoPlanta = planta.calcularSalario(diasTrabajados)

print("Sueldo mes de enero")
print(f"Empleado: {planta.getNombres()} {planta.getApellidos()}")
print(f"Cargo: {planta.getCargo()}")
print(f"Tipo empleado: {type(planta).__name__}")
print(f"Horas trabajadas: {horasTrabajadas}")
print(f"Dias trabajados: {diasTrabajados}")
print(f"Sueldo basico: {sueldoPlanta}")

# def registrarEmpleado():
#     os.system("cls")
#     Cedula=input("Ingrese número de cedula: ")
#     nombres=input("Ingrese sus nombres: ")
#     apellidos=input("Ingrese sus apellido: ")
#     correo=input("Ingrese su correo: ")
#     genero=input("Ingrese su genero: ")
#     fechaIngresoEmpresa=input("Ingrese fecha de ingreso (dia/mes/año): ")
#     cargo=input("Ingrese su cargo: ")
#     horasTrabajadas=input("Ingrese las horas trabajadas: ")
#     print("Vuelo creado satisfactoriamente...")