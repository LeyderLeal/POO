from tienda import Tienda
from producto import Producto
from cliente import Cliente
from venta import Venta
from detalleventa import DetalleVenta

# Crear una tienda
tienda = Tienda("Mi Tienda")

# Crear productos
producto1 = Producto("Camiseta", 25.0)
producto2 = Producto("Pantalón", 40.0)

# Agregar productos a la tienda
tienda.agregar_producto(producto1)
tienda.agregar_producto(producto2)

# Crear un cliente
cliente = Cliente("Juan Pérez", "12345678")

# Crear una venta
venta = Venta(cliente)

# Agregar detalles de venta
detalle1 = DetalleVenta(producto1, 2)
detalle2 = DetalleVenta(producto2, 1)

venta.agregar_detalle(detalle1)
venta.agregar_detalle(detalle2)

# Imprimir los datos de la venta
print("Fecha de la venta:", venta.fecha)
print("Nombre del cliente:", venta.cliente.nombre)
print("Productos de la venta:")
for detalle in venta.detalles:
    print("- Nombre: {}, Precio unitario: ${}, Cantidad: {}, Total: ${}"
          .format(detalle.producto.nombre, detalle.producto.precio, detalle.cantidad, detalle.calcular_total()))

print("Valor total de la venta: ${}".format(venta.calcular_total()))


