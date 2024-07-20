class Libro:
    def __init__(self, titulo, autor, isbn, precio):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.precio = precio

    def __str__(self):
        return f"{self.titulo} por {self.autor} (ISBN: {self.isbn}) - ${self.precio}"


class Cliente:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.compras = []

    def comprar_libro(self, libro):
        self.compras.append(libro)

    def mostrar_compras(self):
        print(f"Compras de {self.nombre}:")
        for libro in self.compras:
            print(f"- {libro}")

    def __str__(self):
        return f"{self.nombre} (Email: {self.email})"


class Libreria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_disponibles = []
        self.clientes = []

    def agregar_libro(self, libro):
        self.libros_disponibles.append(libro)

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def mostrar_libros_disponibles(self):
        print(f"Libros disponibles en {self.nombre}:")
        for libro in self.libros_disponibles:
            print(f"- {libro}")

    def __str__(self):
        return f"Librería: {self.nombre}"


# Creación de objetos y demostración de interacción entre ellos
if __name__ == "__main__":
    # Crear libros
    libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "978-3-16-148410-0", 15.99)
    libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "978-1-23-456789-7", 12.99)

    # Crear cliente
    cliente1 = Cliente("Juan Pérez", "juan.perez@example.com")

    # Crear librería
    libreria = Libreria("Librería El Buen Lector")

    # Agregar libros a la librería
    libreria.agregar_libro(libro1)
    libreria.agregar_libro(libro2)

    # Registrar cliente en la librería
    libreria.registrar_cliente(cliente1)

    # Mostrar libros disponibles en la librería
    libreria.mostrar_libros_disponibles()

    # Cliente compra un libro
    cliente1.comprar_libro(libro1)

    # Mostrar compras del cliente
    cliente1.mostrar_compras()
