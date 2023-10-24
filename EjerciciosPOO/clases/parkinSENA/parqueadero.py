from carro import Carro
from puesto import Puesto
from parqueo import Parqueo
from datetime import datetime

class Parqueadero():
    
    def __init__(self, nombre=str, cantidadPuestos=int):
        self.__nombre = nombre
        self.__cantidadPuestos=cantidadPuestos
        self.__listaPuestos = []
        self.__listaParqueos = []
        self.inicializarPuestos()
        
    def inicializarPuestos(self):
        for i in range(1,self.__cantidadPuestos + 1,1):
            puesto = Puesto(i)
            for p in self.__listaPuestos:
                if p == puesto:
                    p.setCarro(carro)
            self.__listaPuestos.append(puesto)
            
    def getNombre(self):
        return self.__nombre
    
    def getListaPuestos(self):
        return self.__listaPuestos
    
    def getListaParqueo(self):
        return self.__listaParqueos
    
    def getCantidadPuestos(self):
        return self.__cantidadPuestos
    
    def parquear(self,carro=Carro,puesto=Puesto):
        parqueo = Parqueo(carro,puesto)
        for p in self.__listaPuestos:
            if p ==puesto:
                p.setCarro(carro)
            self.__listaParqueos.append(parqueo)
        
    def retirarCarro(self,placa=str):
        os.system("cls")
        print("PROCESO REGISTRO DE SALIDA DE CARRO")
        placa = input("Ingrese placa del carro: ").upper()
        
        retiro = parking.retirarCarro(placa)
        if(retiro==False):
            print("Carro no parqueado")
        else:
            print("Se ha registrado la salida del carro.")
    
        