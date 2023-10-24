from venta import Venta
from cliente import Cliente
from detalleVenta import DetalleVenta
from producto import Producto
from tienda import Tienda

tienda = Tienda("D1")

producto1 = Producto(11, "Tenis", 300000)
producto2 = Producto(13, "Pizza", 10000)

tienda.agregarProducto(producto1)
tienda.agregarProducto(producto2)

cliente1 = Cliente("Andres", "Cra30E#2-20", "andres@gmail.com")

venta1 = Venta(cliente1)

detalle1 = DetalleVenta(producto1, 3, producto1.getPrecio())
detalle2 = DetalleVenta(producto2, 10, producto2.getPrecio())

venta1.agregarDetalleVenta(detalle1)
venta1.agregarDetalleVenta(detalle2)

print(venta1.getFecha())
print(cliente1.getNombre())
for detalleVenta in venta1.getListaDetalleVenta():
    print(f"- Nombre: {DetalleVenta.getProducto(detalleVenta)}")

# , Precio unitario: ${detalle.producto.precio}, Cantidad: {detalle.cantidad}, Total: ${detalle.calcular_total()}")
    
print(f"Valor total de la venta: ${venta1.valorTotal()}")