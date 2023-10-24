from parqueadero import Parqueadero
from carro import Carro
from puesto import Puesto

parqueadero = Parqueadero()

while True:
    print('Menú de opciones:')
    print('1. Registrar ingreso de carro')
    print('2. Registrar salida de carro')
    print('3. Consultar puesto')
    print('4. Consultar carros')
    print('5. Mostrar estado de los puestos')
    print('6. Salir')
    opcion = input('Seleccione una opción: ')
    if opcion == '1':
        placa = input('Ingrese la placa del carro: ')
        color = input('Ingrese el color del carro: ')
        fecha = input('Ingrese la fecha (dd/mm/aaaa): ')
        hora = input('Ingrese la hora (hh:mm): ')
        puesto = int(input('Ingrese el número del puesto: '))
        parqueadero.registrarIngreso(placa, color, fecha, hora, puesto)
    if opcion == '2':
        placa = input('Ingrese la placa del carro: ')
        fecha = input('Ingrese la fecha (dd/mm/aaaa): ')
        hora = input('Ingrese la hora (hh:mm): ')
        parqueadero.registrarSalida(placa, fecha, hora)
    if opcion == '3':
        puesto = int(input('Ingrese el número del puesto: '))
        parqueadero.consultarPuesto(puesto)
    if opcion == '4':
        parqueadero.consultarCarros()
    if opcion == '5':
        parqueadero.mostrarEstado()
    if opcion == '6':
        break