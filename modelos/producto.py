class Producto:
    """Representa un producto disponible en el restaurante."""

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float) -> None:
        self.codigo: str = codigo
        self.nombre: str = nombre
        self.categoria: str = categoria
        self.precio: float = precio

    def __str__(self) -> str:
        return f"[{self.codigo}] {self.nombre} - {self.categoria} - ${self.precio:.2f}"
