class Libro:
    def __init__(self, titulo, autor, anio_publicacion):
        """
        Constructor que inicializa los atributos del libro.

        :param titulo: Título del libro
        :param autor: Autor del libro
        :param anio_publicacion: Año de publicación del libro
        """
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        print(f"Libro '{self.titulo}' creado.")

    def __del__(self):
        """
        Destructor que se llama cuando el objeto se destruye.
        Limpiamos recursos o imprimos un mensaje.
        """
        print(f"Libro '{self.titulo}' destruido.")

    def detalles(self):
        """
        Método que muestra los detalles del libro.
        """
        return f"{self.titulo} de {self.autor}, publicado en {self.anio_publicacion}."

    # Ejemplo de uso de la clase Libro


if __name__ == "__main__":
    # Crear una instancia de la clase Libro
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)

    # Mostrar los detalles del libro
    print(libro1.detalles())

    # Eliminar la referencia al libro para activar el destructor
    del libro1