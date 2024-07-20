class Plato:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f}"


class Cliente:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.pedidos = []

    def hacer_pedido(self, pedido):
        self.pedidos.append(pedido)

    def mostrar_pedidos(self):
        print(f"Pedidos de {self.nombre}:")
        for pedido in self.pedidos:
            print(f"- {pedido}")

    def __str__(self):
        return f"{self.nombre} (Email: {self.email})"


class Pedido:
    def __init__(self, cliente, platos):
        self.cliente = cliente
        self.platos = platos
        self.total = sum(plato.precio for plato in platos)

    def __str__(self):
        platos_descripcion = ", ".join(plato.nombre for plato in self.platos)
        return f"Pedido de {self.cliente.nombre}: {platos_descripcion} - Total: ${self.total:.2f}"


class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.menu = []
        self.clientes = []

    def agregar_plato(self, plato):
        self.menu.append(plato)

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def mostrar_menu(self):
        print(f"Menú de {self.nombre}:")
        for plato in self.menu:
            print(f"- {plato}")

    def __str__(self):
        return f"Restaurante: {self.nombre}"


# Creación de objetos y demostración de interacción entre ellos
if __name__ == "__main__":
    # Crear platos
    plato1 = Plato("Spaghetti Bolognese", 12.50)
    plato2 = Plato("Ensalada César", 8.00)
    plato3 = Plato("Pizza Margherita", 10.00)

    # Crear cliente
    cliente1 = Cliente("Ana Gómez", "ana.gomez@example.com")

    # Crear restaurante
    restaurante = Restaurante("Restaurante Buen Sabor")

    # Agregar platos al menú del restaurante
    restaurante.agregar_plato(plato1)
    restaurante.agregar_plato(plato2)
    restaurante.agregar_plato(plato3)

    # Registrar cliente en el restaurante
    restaurante.registrar_cliente(cliente1)

    # Mostrar menú del restaurante
    restaurante.mostrar_menu()

    # Cliente hace un pedido
    pedido1 = Pedido(cliente1, [plato1, plato3])
    cliente1.hacer_pedido(pedido1)

    # Mostrar pedidos del cliente
    cliente1.mostrar_pedidos()
