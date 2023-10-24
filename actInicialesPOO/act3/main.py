from empresa import Empresa
import os
# crear un objeto de tipo empresa
avianca = Empresa("AVIANCA")
#Agregar un vuelo
def registrarVuelo():
    os.system("cls")
    numeroVuelo=int(input("Ingrese número de Vuelo: "))
    fechaVuelo=input("Ingrese fecha del Vuelo (dia/mes/año): ")
    ciudadOrigen=input("Ingrese Ciudad Origen del Vuelo: ")
    ciudadDestino=input("Ingrese Ciudad Destino del Vuelo: ")
    avianca.registrarVuelo(numeroVuelo, fechaVuelo,ciudadOrigen,ciudadDestino)
    print("Vuelo creado satisfactoriamente...")

def listarVuelos():
    os.system("cls")
    #imprimir vuelos registrados
    for vuelo in avianca.getListaVuelos():
        print("*******************************************************")
        print(f'Número de Vuelo: {vuelo.getNumero()}')
        print(f'Fecha de Vuelo: {vuelo.getFecha()}')
        print(f'Ciudad Origen de Vuelo: {vuelo.getCiudadOrigen()}')
        print(f'Ciudad Destino de Vuelo: {vuelo.getCiudadDestino()}')
        print()

def agregarPasajero():
    os.system("cls")
    nVuelo = int(input("Ingrese número del Vuelo para agregar pasajero: "))    
    #recorrer la lista de vuelos para encontrar el vuelo
    for vuelo in avianca.getListaVuelos():
        if(vuelo.getNumero()==nVuelo):        
            nombreP = input("Ingrese Nombre de Pasajero: ")
            correoP = input("Ingrese Correo Electrónico del Pasajero: ")
            vuelo.agregarPasajero(nombreP,correoP)  
            print("Pasajero agregado al vuelo Correctamente")      
            break
    else:
        print("No existe vuelo con ese número. No se puede agregar el Pasajero")

def listarPasajeros():
    os.system("cls")
    #imprimir los pasajeros del vuelo
    nVuelo = int(input("Ingrese número del Vuelo para listar pasajeros: ")) 
    for vuelo in avianca.getListaVuelos():
        if(vuelo.getNumero()==nVuelo):
            #Listar los pasajeros del Vuelo
            print(f"LISTA DE PASAJEROS DEL VUELO NÚMERO {nVuelo}")
            for pasajero in vuelo.getListaPasajeros():            
                print(f'Nombre: {pasajero.getNombre()}')
                print(f'Correo: {pasajero.getCorreo()}')
                print("**************************************")
            break

def menu():
    while(True):
        os.system("cls")
        print(f"\t\tMENU EMPRESA {avianca.getNombre()}")
        print("\t1. Registrar Vuelo")
        print("\t2. Agregar Pasajero")
        print("\t3. Listar Vuelos")
        print("\t4. Listar Pasajeros")
        print("\t5. Salir")
        opcion = int(input("Ingrese opción(1-5): "))
        
        if(opcion==1):
            registrarVuelo()
        elif(opcion==2):
            agregarPasajero()
        elif(opcion==3):
            listarVuelos()
        elif(opcion==4):
            listarPasajeros()
        elif(opcion==5):
            print("Va a salir")
            break
        else:
            print("Opción no valida...")
            
        input("Presione enter para continuar")
        
menu()
        
        
        