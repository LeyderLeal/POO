from parqueadero import Parqueadero
from carro import Carro
import os

parking = Parqueadero("SENA",2)

def parquearCarro():
    os.system("cls")
    print("PROCESO REGISTRO DE INGRESO CARRO")
    placa = input("ingrese Placa del Carro: ").upper()
    color = input("Ingrese color del Carro: ").upper()
    carro = Carro(placa,color)
    #buscar puesto disponible
    for puesto in parking.getListaPuestos():
        if puesto.getEstado()=="Disponible":
            parking.parquear(carro, puesto)
            print(f"El carro se ha parqueado en el puesto {puesto.getNumero()}")
            break
        else:
            print("No hay puesto disponible...")
            
def retirarCarro():
    os.system("cls")
    print("PROCESO REGISTRO DE SALIDA DE CARRO")
    placa = input("Ingrese placa del carro: ").upper()
    
    for parqueo in parking.getListaParqueo():
        if(parqueo.getCarro().getPlaca()==placa):
            parqueo.setFechaHoraSalida()
            parqueo.getPuesto().setCarro(None)
    
def menu():
    while(True):
        os.system("cls")
        print(f"\t\tGESTIÓN PARQUEADERO {parking.getNombre()}")
        print(f"\t1. Parquear Carro")
        print(f"\t2. Retirar Carro")
        print(f"\t3. Consultar Carro Parqueado")
        print(f"\t4. Listar Carro Parqueadero")
        print(f"\t6. Salir")
        opcion = int(input("ingrese un opción: "))
        if (opcion == 1):
            parquearCarro()
        elif (opcion == 2):
            pass
        elif (opcion == 3):
            pass
        elif (opcion == 4):
            pass
        elif (opcion == 5):
            pass
        elif (opcion == 6):
            print("Va a salir..")
            break
        else:
            print("Opcion no valida")
        
        input("Presione enter para continuar")
        
menu()