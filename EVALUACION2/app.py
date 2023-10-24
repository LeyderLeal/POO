from sala import Sala
from persona import Persona
import os
import datetime

miSala = Sala("SENA",3)

    
def ingresoSala():
    os.system("cls")
    print("Registrar Ingreso a la Sala")
    id = input("Ingrese identificacion de la persona: ")
    nombre = input("Ingrese nombre de la persona: ")
    correo = input("Ingrese correo de la persona: ")
    genero = input("Ingrese genero de la persona (Femenino/Masculino): ").upper()
    estado,mensaje = miSala.registrarIngreso(id,nombre,correo,genero)
    print(mensaje)

def consultarSilla():
    os.system("cls")
    print("Consultar Silla")
    numero = int(input(f"Ingrese el numero de silla a consultar de 1 a {miSala.getCantidadSillas()}: "))
    persona = miSala.obtenerDatosPersonaSilla(numero)
    
    if (type(persona) == Persona):
        print("Datos de la Persona ubicada en la Silla # {numero}")
        print(f"Identificacion: {persona.getIdentificacion()}")
        print(f"Nombre: {persona.getNombre()}")
        print(f"Correo: {persona.getCorreo()}")
        print(f"Genero: {persona.getGenero()}")
    else:
        print(persona)

def cantidadPersonaGenero():
    os.system("cls")
    print("Consultar cantidad personas genero")
    mujeres, hombres = miSala.obtenerCantidadMujeresHombres()
    print(f"Cantidad Mujeres {mujeres}")
    print(f"Cantidad Hombres {hombres}")

def datosPersonasSala():
    os.system("cls")
    print("Datos Personas Sala")
    for ingreso in miSala.getListaIngreso():
        print(f"Nombre: {ingreso.getPersona().getNombre()}")
        print(f"Silla: {ingreso.getSilla().getNumero()}")
        print(f"FechaIngreso: {ingreso.getFechaHora().strftime('%X')}")
        print(f"HoraIngreso: {ingreso.getfechaHora().strftime('%X')}")
        print("*"*50)
    

def menu():
    while(True):
        od.system("cls")
        print(f"\t\tGESTIÓN SALA {miSala.getNombre()}")
        print(f"\t1. Registrar Ingreso Sala")
        print(f"\t2. Consultar Silla")
        print(f"\t3. Cantidad Personas Genero")
        print(f"\t4. Datos Personas en Sala")
        print(f"\t5. Salir")
        opcion=int(input("\tIngrese opcion: "))
        if opcion == 1:
            ingresoSala()
        elif opcion == 2:
            consultarSilla()
        elif opcion == 3:
            cantidadPersonaGenero()
        elif opcion == 4:
            datosPersonasSala()
        elif opcion == 5:
            print("saliendo..")
            break
        else:
            print("opcion no valida")
            
        input("Presione enter para continuar")

menu()