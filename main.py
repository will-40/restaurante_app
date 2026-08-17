from typing import Callable, Dict, Tuple

from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante

# Tupla: información estable que no cambia durante la ejecución del programa
OPCIONES_MENU: Tuple[str, ...] = (
    "1. Registrar producto",
    "2. Buscar producto",
    "3. Actualizar producto",
    "4. Eliminar producto",
    "5. Listar productos",
    "6. Registrar usuario",
    "7. Listar usuarios",
    "8. Mostrar categorías",
    "9. Salir",
)


def mostrar_menu() -> None:
    print("=" * 40)
    print("        SISTEMA DE RESTAURANTE")
    print("=" * 40)
    for opcion in OPCIONES_MENU:
        print(opcion)
    print("-" * 40)


def leer_float(mensaje: str) -> float:
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Valor inválido. Ingrese un número, por ejemplo 4.50.")


def registrar_producto(restaurante: Restaurante) -> None:
    codigo = input("Código del producto: ").strip()
    if restaurante.existe_producto(codigo):
        print(f"Ya existe un producto con el código '{codigo}'.")
        return
    nombre = input("Nombre: ").strip()
    categoria = input("Categoría: ").strip()
    precio = leer_float("Precio: ")
    producto = Producto(codigo, nombre, categoria, precio)
    if restaurante.registrar_producto(producto):
        print("Producto registrado correctamente.")
    else:
        print("No se pudo registrar el producto.")


def buscar_producto(restaurante: Restaurante) -> None:
    codigo = input("Código a buscar: ").strip()
    producto = restaurante.buscar_producto(codigo)
    print(producto if producto else "Producto no encontrado.")


def actualizar_producto(restaurante: Restaurante) -> None:
    codigo = input("Código del producto a actualizar: ").strip()
    if restaurante.buscar_producto(codigo) is None:
        print("Producto no encontrado.")
        return
    print("Deje en blanco el campo que no desea modificar.")
    nombre = input("Nuevo nombre: ").strip() or None
    categoria = input("Nueva categoría: ").strip() or None
    precio_str = input("Nuevo precio: ").strip()
    precio = float(precio_str) if precio_str else None
    if restaurante.actualizar_producto(codigo, nombre, categoria, precio):
        print("Producto actualizado correctamente.")
    else:
        print("No se pudo actualizar el producto.")


def eliminar_producto(restaurante: Restaurante) -> None:
    codigo = input("Código del producto a eliminar: ").strip()
    if restaurante.eliminar_producto(codigo):
        print("Producto eliminado correctamente.")
    else:
        print("Producto no encontrado.")


def listar_productos(restaurante: Restaurante) -> None:
    productos = restaurante.listar_productos()
    if not productos:
        print("No hay productos registrados.")
        return
    for producto in productos:
        print(producto)


def registrar_usuario(restaurante: Restaurante) -> None:
    identificacion = input("Identificación: ").strip()
    if restaurante.existe_usuario(identificacion):
        print(f"Ya existe un usuario con la identificación '{identificacion}'.")
        return
    nombre = input("Nombre: ").strip()
    correo = input("Correo: ").strip()
    usuario = Usuario(identificacion, nombre, correo)
    if restaurante.registrar_usuario(usuario):
        print("Usuario registrado correctamente.")
    else:
        print("No se pudo registrar el usuario.")


def listar_usuarios(restaurante: Restaurante) -> None:
    usuarios = restaurante.listar_usuarios()
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    for usuario in usuarios:
        print(usuario)


def mostrar_categorias(restaurante: Restaurante) -> None:
    categorias = restaurante.obtener_categorias()
    if not categorias:
        print("No hay categorías registradas todavía.")
        return
    for categoria in sorted(categorias):
        print(f"- {categoria}")


def salir(restaurante: Restaurante) -> None:
    print("Gracias por usar el sistema. ¡Hasta pronto!")


def main() -> None:
    restaurante = Restaurante()

    # Diccionario: relación clave (opción del menú) -> valor (función que la resuelve)
    acciones: Dict[str, Callable[[Restaurante], None]] = {
        "1": registrar_producto,
        "2": buscar_producto,
        "3": actualizar_producto,
        "4": eliminar_producto,
        "5": listar_productos,
        "6": registrar_usuario,
        "7": listar_usuarios,
        "8": mostrar_categorias,
    }

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "9":
            salir(restaurante)
            break

        accion = acciones.get(opcion)
        if accion is None:
            print("Opción inválida. Intente nuevamente.")
        else:
            accion(restaurante)

        input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    main()
