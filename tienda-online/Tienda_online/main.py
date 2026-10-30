"""Punto de entrada del programa: prueba manual del sistema de la tienda."""

from models.producto import Producto, ProductoElectronico, ProductoRopa
from services.tienda_service import TiendaService


def main() -> None:
    """Registra usuarios y productos, simula pedidos y muestra el resultado."""
    tienda = TiendaService()

    cliente1 = tienda.registrar_usuario(
        "cliente", nombre="jose", email="jose@planetexpress.com", direccion="Calle Delivery 1"
    )
    cliente2 = tienda.registrar_usuario(
        "cliente", nombre="francisco", email="francisco@planetexpress.com", direccion="Calle Delivery 2"
    )
    cliente3 = tienda.registrar_usuario(
        "cliente", nombre="juan", email="juan@planetexpress.com", direccion="Calle Delivery 3"
    )
    tienda.registrar_usuario(
        "administrador", nombre="marcos", email="marcos@planetexpress.com"
    )

    portatil = tienda.agregar_producto(
        ProductoElectronico("Portátil", 899.99, 10, meses_garantia=24)
    )
    telefono = tienda.agregar_producto(
        ProductoElectronico("Teléfono", 499.99, 15, meses_garantia=12)
    )
    camiseta = tienda.agregar_producto(
        ProductoRopa("Camiseta", 19.99, 50, talla="S", color="Verde")
    )
    pantalon = tienda.agregar_producto(
        ProductoRopa("Pantalón", 39.99, 30, talla="XL", color="Azul")
    )
    libro = tienda.agregar_producto(Producto("Libro", 14.99, 20))

    print("--- Inventario inicial ---")
    for producto in tienda.listar_productos():
        print(producto)

    pedido1 = tienda.realizar_pedido(cliente1.id, {portatil.id: 1, camiseta.id: 2})
    pedido2 = tienda.realizar_pedido(cliente2.id, {telefono.id: 1, pantalon.id: 1})
    pedido3 = tienda.realizar_pedido(cliente3.id, {libro.id: 3, camiseta.id: 1})

    print("\n--- Pedidos realizados ---")
    for pedido in (pedido1, pedido2, pedido3):
        print(pedido)

    print("\n--- Histórico de pedidos de Jose ---")
    for pedido in tienda.listar_pedidos_usuario(cliente1.id):
        print(pedido)

    print("\n--- Stock actualizado ---")
    for producto in tienda.listar_productos():
        print(producto)


if __name__ == "__main__":
    main()
