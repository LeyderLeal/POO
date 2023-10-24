from gato import Gato
from perro import Perro
from pez import Pez

miGato = Gato(4)
miGato.maullar()
miGato.respirar()

tango = Perro(14)
tango.ladrar()
tango.respirar()

Nemo = Pez(1)
Nemo.nadar()
Nemo.respirar()

print(f"{type(tango).__name__} tiene {tango.getPeso()} kilos de peso")
print(f"{type(miGato).__name__} tiene {miGato.getPeso()} kilos de peso")
print(f"{type(Nemo).__name__} tiene {Nemo.getPeso()} kilos de peso")
