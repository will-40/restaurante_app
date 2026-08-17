from typing import List, Optional, Set

from modelos.producto import Producto
from modelos.usuario import Usuario


class Restaurante:
    """Servicio encargado de administrar las colecciones y operaciones del sistema."""

    def __init__(self) -> None:
        # Listas: colecciones dinámicas de objetos que crecen y cambian en tiempo de ejecución
        self.productos: List[Producto] = []
        self.usuarios: List[Usuario] = []

    # ---------------------- Productos ----------------------

    def existe_producto(self, codigo: str) -> bool:
        return any(producto.codigo == codigo for producto in self.productos)

    def registrar_producto(self, producto: Producto) -> bool:
        if self.existe_producto(producto.codigo):
            return False
        self.productos.append(producto)
        return True

    def buscar_producto(self, codigo: str) -> Optional[Producto]:
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto
        return None

    def actualizar_producto(
        self,
        codigo: str,
        nombre: Optional[str] = None,
        categoria: Optional[str] = None,
        precio: Optional[float] = None,
    ) -> bool:
        producto = self.buscar_producto(codigo)
        if producto is None:
            return False
        if nombre:
            producto.nombre = nombre
        if categoria:
            producto.categoria = categoria
        if precio is not None:
            producto.precio = precio
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        producto = self.buscar_producto(codigo)
        if producto is None:
            return False
        self.productos.remove(producto)
        return True

    def listar_productos(self) -> List[Producto]:
        return list(self.productos)

    def obtener_categorias(self) -> Set[str]:
        # Conjunto: elimina automáticamente categorías repetidas
        return {producto.categoria for producto in self.productos}

    # ---------------------- Usuarios ----------------------

    def existe_usuario(self, identificacion: str) -> bool:
        return any(usuario.identificacion == identificacion for usuario in self.usuarios)

    def registrar_usuario(self, usuario: Usuario) -> bool:
        if self.existe_usuario(usuario.identificacion):
            return False
        self.usuarios.append(usuario)
        return True

    def listar_usuarios(self) -> List[Usuario]:
        return list(self.usuarios)
