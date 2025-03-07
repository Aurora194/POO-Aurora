class Libro:
    """
    Representa un libro en la biblioteca.

    Atributos:
        titulo (str): El título del libro.
        autor (str): El autor del libro.
        categoria (str): La categoría a la que pertenece el libro.
        isbn (str): El ISBN único del libro.
    """
    def __init__(self, titulo, autor, categoria, isbn):
        """
        Inicializa un nuevo libro.

        Parámetros:
            titulo (str): El título del libro.
            autor (str): El autor del libro.
            categoria (str): La categoría del libro.
            isbn (str): El ISBN del libro (debe ser único).
        """
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        """
        Retorna una representación legible del libro.
        """
        return f"Título: {self.titulo}, Autor: {self.autor}, Categoría: {self.categoria}, ISBN: {self.isbn}"


class Usuario:
    """
    Representa un usuario de la biblioteca.

    Atributos:
        nombre (str): El nombre del usuario.
        id_usuario (str): Un ID único para el usuario.
        libros_prestados (list): Una lista de los ISBNs de los libros que el usuario tiene prestados.
    """
    def __init__(self, nombre, id_usuario):
        """
        Inicializa un nuevo usuario.

        Parámetros:
            nombre (str): El nombre del usuario.
            id_usuario (str): Un ID único para el usuario.
        """
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista para almacenar los ISBNs de los libros prestados

    def __str__(self):
        """
        Retorna una representación legible del usuario.
        """
        return f"Nombre: {self.nombre}, ID Usuario: {self.id_usuario}, Libros Prestados: {self.libros_prestados}"


class Biblioteca:
    """
    Gestiona los libros, usuarios y préstamos de la biblioteca.

    Atributos:
        libros (dict): Un diccionario de libros, con el ISBN como clave.
        usuarios (set): Un conjunto de IDs de usuario únicos.
        registro_usuarios (dict): Un diccionario que mapea los IDs de usuario a los objetos Usuario.
    """
    def __init__(self):
        """
        Inicializa la biblioteca con diccionarios y conjuntos vacíos para libros y usuarios.
        """
        self.libros = {}  # ISBN -> Libro
        self.usuarios = set()  # Conjunto de IDs de usuario
        self.registro_usuarios = {}  # ID Usuario -> Usuario

    def añadir_libro(self, libro):
        """
        Añade un libro a la biblioteca.

        Parámetros:
            libro (Libro): El objeto Libro a añadir.
        """
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.titulo}' añadido.")
        else:
            print(f"Error: Ya existe un libro con el ISBN '{libro.isbn}'.")

    def quitar_libro(self, isbn):
        """
        Quita un libro de la biblioteca.

        Parámetros:
            isbn (str): El ISBN del libro a quitar.
        """
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN '{isbn}' eliminado.")
        else:
            print(f"Error: No se encontró un libro con el ISBN '{isbn}'.")

    def registrar_usuario(self, usuario):
        """
        Registra un nuevo usuario en la biblioteca.

        Parámetros:
            usuario (Usuario): El objeto Usuario a registrar.
        """
        if usuario.id_usuario not in self.usuarios:
            self.usuarios.add(usuario.id_usuario)
            self.registro_usuarios[usuario.id_usuario] = usuario
            print(f"Usuario '{usuario.nombre}' registrado con ID '{usuario.id_usuario}'.")
        else:
            print(f"Error: Ya existe un usuario con el ID '{usuario.id_usuario}'.")

    def dar_baja_usuario(self, id_usuario):
        """
        Da de baja a un usuario existente de la biblioteca.

        Parámetros:
            id_usuario (str): El ID del usuario a dar de baja.
        """
        if id_usuario in self.usuarios:
            self.usuarios.remove(id_usuario)
            del self.registro_usuarios[id_usuario]
            print(f"Usuario con ID '{id_usuario}' dado de baja.")
        else:
            print(f"Error: No se encontró un usuario con el ID '{id_usuario}'.")

    def prestar_libro(self, id_usuario, isbn):
        """
        Presta un libro a un usuario.

        Parámetros:
            id_usuario (str): El ID del usuario que pide el libro prestado.
            isbn (str): El ISBN del libro a prestar.
        """
        if id_usuario in self.usuarios and isbn in self.libros:
            usuario = self.registro_usuarios[id_usuario]
            libro = self.libros[isbn]
            if isbn not in usuario.libros_prestados:
                usuario.libros_prestados.append(isbn)
                print(f"Libro '{libro.titulo}' prestado a '{usuario.nombre}'.")
            else:
                print(f"Error: El usuario '{usuario.nombre}' ya tiene prestado el libro '{libro.titulo}'.")
        else:
            print("Error: Usuario o libro no encontrado.")

    def devolver_libro(self, id_usuario, isbn):
        """
        Permite a un usuario devolver un libro.

        Parámetros:
            id_usuario (str): El ID del usuario que devuelve el libro.
            isbn (str): El ISBN del libro a devolver.
        """
        if id_usuario in self.usuarios:
            usuario = self.registro_usuarios[id_usuario]
            if isbn in usuario.libros_prestados:
                usuario.libros_prestados.remove(isbn)
                print(f"Libro con ISBN '{isbn}' devuelto por '{usuario.nombre}'.")
            else:
                print(f"Error: El usuario '{usuario.nombre}' no tiene prestado el libro con ISBN '{isbn}'.")
        else:
            print("Error: Usuario no encontrado.")

    def buscar_libros(self, criterio, valor):
        """
        Busca libros por título, autor o categoría.

        Parámetros:
            criterio (str): El criterio de búsqueda ('titulo', 'autor', 'categoria').
            valor (str): El valor a buscar.

        Retorna:
            list: Una lista de libros que coinciden con el criterio de búsqueda.
        """
        resultados = []
        for libro in self.libros.values():
            if criterio == 'titulo' and valor.lower() in libro.titulo.lower():
                resultados.append(libro)
            elif criterio == 'autor' and valor.lower() in libro.autor.lower():
                resultados.append(libro)
            elif criterio == 'categoria' and valor.lower() in libro.categoria.lower():
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, id_usuario):
        """
        Lista los libros prestados a un usuario específico.

        Parámetros:
            id_usuario (str): El ID del usuario para el cual se listarán los libros prestados.

        Retorna:
            list: Una lista de los libros prestados al usuario.
        """
        if id_usuario in self.usuarios:
            usuario = self.registro_usuarios[id_usuario]
            libros_prestados = [self.libros[isbn] for isbn in usuario.libros_prestados if isbn in self.libros]
            return libros_prestados
        else:
            print("Error: Usuario no encontrado.")
            return []

# Ejemplo de uso
biblioteca = Biblioteca()

# Crear libros
libro1 = Libro("El Señor de los Anillos", "J.R.R. Tolkien", "Fantasía", "978-0618260264")
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo Mágico", "978-0307474728")
libro3 = Libro("1984", "George Orwell", "Ciencia Ficción", "978-0451524935")

# Añadir libros a la biblioteca
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)
biblioteca.añadir_libro(libro3)

# Crear usuarios
usuario1 = Usuario("Alice Smith", "AS123")
usuario2 = Usuario("Bob Johnson", "BJ456")

# Registrar usuarios en la biblioteca
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar libros
biblioteca.prestar_libro("AS123", "978-0618260264")
biblioteca.prestar_libro("BJ456", "978-0451524935")

# Listar libros prestados a un usuario
print("\nLibros prestados a Alice:")
for libro in biblioteca.listar_libros_prestados("AS123"):
    print(libro)

# Buscar libros por autor
print("\nLibros de Gabriel García Márquez:")
for libro in biblioteca.buscar_libros("autor", "García Márquez"):
    print(libro)

# Devolver un libro
biblioteca.devolver_libro("AS123", "978-0618260264")

# Listar libros prestados a un usuario después de la devolución
print("\nLibros prestados a Alice después de la devolución:")
for libro in biblioteca.listar_libros_prestados("AS123"):
    print(libro)