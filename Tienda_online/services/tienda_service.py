"""Capa de servicios que centraliza las operaciones de la tienda online."""

from typing import Dict, List, Optional

from models.pedido import Pedido
from models.producto import Producto
from models.usuario import Administrador, Cliente, Usuario


class TiendaService:
    """Intermediario entre los usuarios y los productos de la tienda."""

    def __init__(self) -> None:
        """Inicializa los almacenes en memoria de usuarios, productos y pedidos."""
        self.usuarios: Dict[str, Usuario] = {}
        self.productos: Dict[str, Producto] = {}
        self.pedidos: List[Pedido] = []

    def registrar_usuario(self, tipo: str, **atributos: str) -> Usuario:
        """Registra un nuevo usuario del tipo indicado ('cliente' o 'administrador')."""
        if tipo == "cliente":
            usuario: Usuario = Cliente(**atributos)
        elif tipo == "administrador":
            usuario = Administrador(**atributos)
        else:
            raise ValueError(f"Tipo de usuario desconocido: {tipo}")

        self.usuarios[usuario.id] = usuario
        return usuario

    def agregar_producto(self, producto: Producto) -> Producto:
        """Añade al inventario un producto ya construido de cualquier categoría."""
        self.productos[producto.id] = producto
        return producto

    def eliminar_producto(self, producto_id: str) -> bool:
        """Elimina un producto del inventario a partir de su identificador."""
        return self.productos.pop(producto_id, None) is not None

    def listar_productos(self) -> List[Producto]:
        """Devuelve la lista de todos los productos disponibles en la tienda."""
        return list(self.productos.values())

    def realizar_pedido(self, usuario_id: str, cantidades: Dict[str, int]) -> Optional[Pedido]:
        """Verifica usuario y stock, genera el pedido y descuenta el inventario."""
        usuario = self.usuarios.get(usuario_id)
        if not isinstance(usuario, Cliente):
            return None

        productos_pedido: Dict[Producto, int] = {}
        for producto_id, cantidad in cantidades.items():
            producto = self.productos.get(producto_id)
            if producto is None or not producto.hay_stock(cantidad):
                return None
            productos_pedido[producto] = cantidad

        for producto, cantidad in productos_pedido.items():
            producto.actualizar_stock(-cantidad)

        pedido = Pedido(usuario, productos_pedido)
        self.pedidos.append(pedido)
        return pedido

    def listar_pedidos_usuario(self, usuario_id: str) -> List[Pedido]:
        """Lista los pedidos de un usuario ordenados por fecha."""
        pedidos_usuario = [pedido for pedido in self.pedidos if pedido.cliente.id == usuario_id]
        return sorted(pedidos_usuario, key=lambda pedido: pedido.fecha)
