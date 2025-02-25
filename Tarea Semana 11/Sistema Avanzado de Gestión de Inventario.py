import json

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        """Inicializa un nuevo producto con un ID, nombre, cantidad y precio."""
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def obtener_id(self):
        """Devuelve el ID del producto."""
        return self.id_producto

    def obtener_nombre(self):
        """Devuelve el nombre del producto."""
        return self.nombre

    def obtener_cantidad(self):
        """Devuelve la cantidad del producto."""
        return self.cantidad

    def obtener_precio(self):
        """Devuelve el precio del producto."""
        return self.precio

    def establecer_cantidad(self, nueva_cantidad):
        """Establece una nueva cantidad para el producto."""
        self.cantidad = nueva_cantidad

    def establecer_precio(self, nuevo_precio):
        """Establece un nuevo precio para el producto."""
        self.precio = nuevo_precio

    def to_dict(self):
        """Convierte el producto a un diccionario para facilitar la serialización."""
        return {
            "id": self.id_producto,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

class Inventario:
    def __init__(self):
        """Inicializa el inventario como un diccionario que almacenará productos."""
        self.productos = {}

    def añadir_producto(self, producto):
        """Añade un producto al inventario utilizando su ID como clave."""
        self.productos[producto.obtener_id()] = producto

    def eliminar_producto(self, id_producto):
        """Elimina un producto del inventario por su ID."""
        if id_producto in self.productos:
            del self.productos[id_producto]

    def actualizar_cantidad(self, id_producto, nueva_cantidad):
        """Actualiza la cantidad de un producto específico."""
        if id_producto in self.productos:
            self.productos[id_producto].establecer_cantidad(nueva_cantidad)

    def actualizar_precio(self, id_producto, nuevo_precio):
        """Actualiza el precio de un producto específico."""
        if id_producto in self.productos:
            self.productos[id_producto].establecer_precio(nuevo_precio)

    def buscar_producto(self, nombre):
        """Busca productos que contengan el nombre especificado."""
        found = [producto.to_dict() for producto in self.productos.values() if nombre.lower() in producto.obtener_nombre().lower()]
        return found

    def mostrar_productos(self):
        """Devuelve una lista de todos los productos en el inventario."""
        return [producto.to_dict() for producto in self.productos.values()]

    def guardar_inventario(self, filename):
        """Guarda el inventario en un archivo JSON."""
        with open(filename, 'w') as file:
            json.dump({id: producto.to_dict() for id, producto in self.productos.items()}, file)

    def cargar_inventario(self, filename):
        """Carga el inventario desde un archivo JSON."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for id_producto, info in data.items():
                    producto = Producto(info['id'], info['nombre'], info['cantidad'], info['precio'])
                    self.añadir_producto(producto)
        except FileNotFoundError:
            print("El archivo no existe. Un nuevo archivo será creado al guardar.")

def menu():
    """Función principal que ejecuta el menú de la aplicación."""
    inventario = Inventario()
    inventario.cargar_inventario('inventario.json')  # Cargar inventario al inicio

    while True:
        print("\n--- Menú de Gestión de Inventario ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar cantidad")
        print("4. Actualizar precio")
        print("5. Buscar producto")
        print("6. Mostrar todos los productos")
        print("7. Guardar inventario")
        print("8. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id_producto = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad: "))
            precio = float(input("Ingrese precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)
            print("Producto añadido.")
        elif opcion == '2':
            id_producto = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
            print("Producto eliminado.")
        elif opcion == '3':
            id_producto = input("Ingrese ID del producto a actualizar cantidad: ")
            nueva_cantidad = int(input("Ingrese nueva cantidad: "))
            inventario.actualizar_cantidad(id_producto, nueva_cantidad)
            print("Cantidad actualizada.")
        elif opcion == '4':
            id_producto = input("Ingrese ID del producto a actualizar precio: ")
            nuevo_precio = float(input("Ingrese nuevo precio: "))
            inventario.actualizar_precio(id_producto, nuevo_precio)
            print("Precio actualizado.")
        elif opcion == '5':
            nombre = input("Ingrese nombre del producto a buscar: ")
            productos_encontrados = inventario.buscar_producto(nombre)
            if productos_encontrados:
                print("Productos encontrados:")
                for producto in productos_encontrados:
                    print(producto)
            else:
                print("No se encontraron productos.")
        elif opcion == '6':
            productos = inventario.mostrar_productos()
            if productos:
                print("Lista de productos en el inventario:")
                for producto in productos:
                    print(producto)
            else:
                print("El inventario está vacío.")
        elif opcion == '7':
            inventario.guardar_inventario('inventario.json')
            print("Inventario guardado.")
        elif opcion == '8':
            inventario.guardar_inventario('inventario.json')  # Guardar antes de salir
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, por favor seleccione de nuevo.")

if __name__ == "__main__":
    menu()