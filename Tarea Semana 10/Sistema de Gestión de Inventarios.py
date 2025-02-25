import os
import json


class Producto:
    """Clase que representa un producto en el inventario."""

    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto  # ID único del producto
        self.nombre = nombre  # Nombre del producto
        self.cantidad = cantidad  # Cantidad disponible en el inventario
        self.precio = precio  # Precio del producto

    def __str__(self):
        """Devuelve una representación en cadena del producto."""
        return f"{self.id_producto} - {self.nombre}: {self.cantidad} unidades, ${self.precio:.2f}"


class Inventario:
    """Clase que gestiona el inventario de productos."""
    ARCHIVO_INVENTARIO = "inventario.txt"  # Nombre del archivo donde se guarda el inventario

    def __init__(self):
        """Inicializa el inventario y carga los datos desde el archivo si existe."""
        self.productos = {}  # Diccionario para almacenar productos
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        """Carga el inventario desde un archivo al iniciar el programa."""
        if not os.path.exists(self.ARCHIVO_INVENTARIO):
            with open(self.ARCHIVO_INVENTARIO, "w") as f:
                json.dump({}, f)  # Crea un archivo vacío si no existe
            return

        try:
            with open(self.ARCHIVO_INVENTARIO, "r") as f:
                datos = json.load(f)  # Carga los datos desde el archivo JSON
                # Convierte los datos JSON en objetos Producto
                self.productos = {int(k): Producto(int(k), v["nombre"], v["cantidad"], v["precio"]) for k, v in
                                  datos.items()}
        except (FileNotFoundError, json.JSONDecodeError):
            print("⚠️ Error al cargar el inventario. Creando nuevo archivo vacío.")
            self.productos = {}
        except PermissionError:
            print("❌ Error: No tienes permisos para leer el archivo de inventario.")

    def guardar_en_archivo(self):
        """Guarda el inventario en un archivo después de cada modificación."""
        try:
            with open(self.ARCHIVO_INVENTARIO, "w") as f:
                json.dump({p.id_producto: {"nombre": p.nombre, "cantidad": p.cantidad, "precio": p.precio} for p in
                           self.productos.values()}, f)
        except PermissionError:
            print("❌ Error: No tienes permisos para escribir en el archivo de inventario.")
        except Exception as e:
            print(f"⚠️ Ocurrió un error al guardar el inventario: {e}")

    def agregar_producto(self, id_producto, nombre, cantidad, precio):
        """Agrega un nuevo producto al inventario."""
        if id_producto in self.productos:
            print("⚠️ El producto ya existe en el inventario.")
            return
        self.productos[id_producto] = Producto(id_producto, nombre, cantidad, precio)
        self.guardar_en_archivo()
        print("✅ Producto agregado con éxito.")

    def actualizar_producto(self, id_producto, cantidad, precio):
        """Actualiza la cantidad y el precio de un producto existente."""
        if id_producto not in self.productos:
            print("⚠️ El producto no existe en el inventario.")
            return
        self.productos[id_producto].cantidad = cantidad
        self.productos[id_producto].precio = precio
        self.guardar_en_archivo()
        print("✅ Producto actualizado con éxito.")

    def eliminar_producto(self, id_producto):
        """Elimina un producto del inventario."""
        if id_producto not in self.productos:
            print("⚠️ El producto no existe en el inventario.")
            return
        del self.productos[id_producto]
        self.guardar_en_archivo()
        print("✅ Producto eliminado con éxito.")

    def mostrar_inventario(self):
        """Muestra todos los productos en el inventario."""
        if not self.productos:
            print("📦 El inventario está vacío.")
        else:
            for producto in self.productos.values():
                print(producto)


# Menú interactivo en la consola
def menu():
    """Función que maneja la interacción con el usuario mediante un menú."""
    inventario = Inventario()
    while True:
        print("\n📋 Menú de Gestión de Inventario")
        print("1. Agregar producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar inventario")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                id_producto = int(input("ID del producto: "))
                nombre = input("Nombre del producto: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                inventario.agregar_producto(id_producto, nombre, cantidad, precio)
            except ValueError:
                print("⚠️ Entrada inválida. Asegúrate de ingresar números en los campos correspondientes.")

        elif opcion == "2":
            try:
                id_producto = int(input("ID del producto a actualizar: "))
                cantidad = int(input("Nueva cantidad: "))
                precio = float(input("Nuevo precio: "))
                inventario.actualizar_producto(id_producto, cantidad, precio)
            except ValueError:
                print("⚠️ Entrada inválida.")

        elif opcion == "3":
            try:
                id_producto = int(input("ID del producto a eliminar: "))
                inventario.eliminar_producto(id_producto)
            except ValueError:
                print("⚠️ Entrada inválida.")

        elif opcion == "4":
            inventario.mostrar_inventario()

        elif opcion == "5":
            print("👋 Saliendo del programa...")
            break

        else:
            print("⚠️ Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    menu()
