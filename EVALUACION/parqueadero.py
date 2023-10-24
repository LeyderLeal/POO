from carro import Carro
from puesto import Puesto

class Parqueadero:
    
    def __init__(self):
        self.puestos = [Puesto(i) for i in range(1, 21)]
        self.carros = []

    def registrarIngreso(self, placa, color, fecha, hora, puesto):
        puesto = Puesto(puesto)
        if  puesto.estado == 'DISPONIBLE':
            carro = Carro(placa, color)
            puesto.estado = 'OCUPADO'
            puesto.carro = carro
            self.carros.append(carro)
            print(f'El carro con placa {placa} ingresó al parqueadero en el puesto {puesto.getNumero} el {fecha} a las {hora}.')
        else:
            print(f'El puesto {puesto.numero} está ocupado.')

    def registrarSalida(self, placa, fecha, hora):
        for puesto in self.puestos:
            if puesto.carro and puesto.carro.placa == placa:
                puesto.estado = 'DISPONIBLE'
                carro = puesto.carro
                puesto.carro = None
                print(f'El carro con placa {placa} salió del parqueadero desde el puesto {puesto.numero} el {fecha} a las {hora}.')
                return carro
        print(f'El carro con placa {placa} no está en el parqueadero.')

    def consultarPuesto(self, numero):
        puesto = self.puestos[numero - 1]
        if puesto.estado == 'OCUPADO':
            print(f'El puesto {puesto.getNumero} está ocupado por un carro con placa {puesto.carro.placa} de color {puesto.carro.color}.')
        else:
            print(f'El puesto {puesto.getNumero} está disponible.')

    def consultarCarros(self):
        print('Carros que han utilizado el parqueadero:')
        for carro in self.carros:
            print(f'Placa: {carro.getPlaca} - Color: {carro.color}')

    def mostrarEstado(self):
        print('Estado de los puestos:')
        for puesto in self.puestos:
            print(f'Puesto {puesto.getNumero}: {puesto.estado}')

