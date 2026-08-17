class Usuario:
    """Representa a una persona registrada en el sistema."""

    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        self.identificacion: str = identificacion
        self.nombre: str = nombre
        self.correo: str = correo

    def __str__(self) -> str:
        return f"[{self.identificacion}] {self.nombre} - {self.correo}"
