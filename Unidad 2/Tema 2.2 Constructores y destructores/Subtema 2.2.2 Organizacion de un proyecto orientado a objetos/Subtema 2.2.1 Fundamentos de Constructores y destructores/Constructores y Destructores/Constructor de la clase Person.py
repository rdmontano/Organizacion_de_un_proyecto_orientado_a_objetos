class Person:
    def __init__(self, name, age, address):
        """
        Constructor de la clase Person.
        Inicializa los atributos de la persona.

        :param name: Nombre de la persona.
        :param age: Edad de la persona.
        :param address: Dirección de la persona.
        """
        self.name = name
        self.age = age
        self.address = address
        print(f"Persona creada: {self.name}, {self.age} años, vive en {self.address}")

    def display_info(self):
        """
        Método para mostrar la información de la persona.
        """
        print(f"Nombre: {self.name}")
        print(f"Edad: {self.age}")
        print(f"Dirección: {self.address}")

    def __del__(self):
        """
        Destructor de la clase Person.
        Imprime un mensaje cuando el objeto es destruido.
        """
        print(f"Persona destruida: {self.name}, {self.age} años, vivía en {self.address}")


# Ejemplo de uso de la clase Person

# Crear una instancia de Person
person1 = Person("Ronny Montaño", 30, "123 - Calle Roberto Cervantes, San Lorenzo")

# Mostrar la información de la persona
person1.display_info()

# La instancia person1 será eliminada al final del script, llamando al destructor
