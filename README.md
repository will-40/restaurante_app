# restaurante_app

**Estudiante:** Walter Ortiz
**Asignatura:** Programación Orientada a Objetos
**Actividad:** Tarea Semana 9 — Estructuras de datos aplicadas al proyecto restaurante_app

## Descripción del sistema

`restaurante_app` es un sistema de consola para administrar productos y usuarios de un
restaurante. En esta entrega se incorporan las principales estructuras de datos de Python
(`list`, `tuple`, `dict` y `set`) para resolver necesidades concretas del sistema, sin perder
la separación entre modelos, servicios y `main.py` trabajada en semanas anteriores.

## Estructura del proyecto

restaurante_app/
├── modelos/
│ ├── init.py
│ ├── producto.py # Clase Producto
│ └── usuario.py # Clase Usuario
├── servicios/
│ ├── init.py
│ └── restaurante.py # Clase Restaurante (servicio)
├── main.py # Punto de arranque y menú interactivo
└── README.md


## Responsabilidad de los componentes

- **`modelos/producto.py`**: define la clase `Producto`, con código, nombre, categoría y precio.
- **`modelos/usuario.py`**: define la clase `Usuario`, con identificación, nombre y correo.
- **`servicios/restaurante.py`**: define la clase `Restaurante`, encargada de administrar las
  colecciones de productos y usuarios, y de resolver registro, búsqueda, actualización,
  eliminación y listado.
- **`main.py`**: presenta el menú, solicita datos por consola mediante `input()`, crea los
  objetos y delega toda la lógica al servicio `Restaurante`. Nunca accede directamente a las
  listas internas del servicio.

## Uso de las estructuras de datos

- **`list`** (`servicios/restaurante.py`): `self.productos` y `self.usuarios` son listas que
  administran dinámicamente los objetos `Producto` y `Usuario` registrados en el sistema
  (agregar, buscar, actualizar, eliminar y listar).
- **`tuple`** (`main.py`): `OPCIONES_MENU` es una tupla con los textos del menú principal,
  porque esa información es fija y no debe modificarse durante la ejecución.
- **`dict`** (`main.py`): `acciones` asocia cada opción del menú (clave, por ejemplo `"1"`)
  con la función correspondiente que la resuelve (valor, por ejemplo `registrar_producto`),
  evitando una larga cadena de `if/elif`.
- **`set`** (`servicios/restaurante.py`): `obtener_categorias()` construye un conjunto a
  partir de las categorías de los productos registrados, para mostrarlas sin duplicados en la
  opción "Mostrar categorías".

## Cómo ejecutar el programa

1. Ubicarse en la carpeta `restaurante_app/`.
2. Ejecutar:

python main.py

3. Usar el menú numérico para registrar productos, buscar, actualizar, eliminar y listar
   productos; registrar y listar usuarios; y mostrar las categorías únicas registradas.

## Reflexión

Elegir la estructura de datos correcta según la necesidad del problema evita trabajo
innecesario y hace el código más claro: usar una lista para colecciones que cambian, una
tupla para datos fijos, un diccionario cuando existe una relación clave-valor y un conjunto
cuando lo que importa es la unicidad, permite que cada parte del sistema use exactamente el
comportamiento que necesita, en lugar de forzar todo a una sola estructura genérica
