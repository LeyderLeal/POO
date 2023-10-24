from silla import Silla
from persona import Persona
from ingresoSala import IngresoSala

class Sala():
    def __init__(self, nombre=str, cantidadSillas=int):
        self.__nombre=nombre
        self.__cantidadSillas=cantidadSillas
        self.__estado='DISPONIBLE'
        self.__listaSillas=[]
        self.__listaIngresos=[]
        self.__inicializarSillas()
        
    def __inicializarSillas():
        for i in range(self.__cantidadSilla):
            silla = Silla(i+1)
            self.__listaSillas.append(silla)
            
    def registrarIngreso(self, identificacion=str, nombre=str, correo=str, genero=str):
        persona = Persona(identificacion,nombre,correo,genero)
        sillaDisponible = self.__obtenerSillaDisponible()
        if(sillaDisponible is not None):
            ingresoSala = IngresoSala(persona, sillaDisponible)
            self.__listaIngresos.append(ingresoSala)
            sillaDisponible.setPersona(persona)
            sillaDisponible.setEstado()
            return True, "Se ha realizado el registro de ingreso"
        else:
            False, "No hay silla disponible"
            
    def __obtenerSillaDisponible(self):
        for silla in self.__listaSillas:
            if silla.getEstado()=='DISPONIBLE':
                return silla
            
        return None
    
    def obtenerDatosPersonaSilla(self, numero=int):
        for silla in self.__listaSillas:
            if silla.getNumero()==numero:
                if silla.getEstado()=='OCUPADO':
                    return silla.getPersona()
                else:
                    return "Silla desocupada"
        return "No existe silla con ese numero"    
    
    def obtenerCantidadMujeresHombres(self):
        mujeres,hombres=0,0
        for ingreso in self.__listaIngresos:        
            if(ingreso.getPersona().getGenero()=='FEMENINO'):
                mujeres +=1
            else: 
                hombres +=1
        return mujeres,hombres        
    
    def getListaSillas(self):
        return self.__listaSillas
    
    def getListaIngreso(self):
        return self.__listaIngresos
    
    def getNombre(self):
        return self.__nombre
    
    def getCantidadSillas(self):
        return self.__cantidadSillas