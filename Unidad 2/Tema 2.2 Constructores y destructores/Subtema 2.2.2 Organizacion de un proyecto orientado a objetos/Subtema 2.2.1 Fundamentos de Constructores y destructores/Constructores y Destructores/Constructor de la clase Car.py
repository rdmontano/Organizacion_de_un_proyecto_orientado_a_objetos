class Car:
    def __init__(self, make, model, year):
        """
        Constructor de la clase Car.
        Inicializa los atributos del automóvil.

        :param make: Marca del automóvil.
        :param model: Modelo del automóvil.
        :param year: Año del automóvil.
        """
        self.make = make
        self.model = model
        self.year = year
        print(f"Automóvil creado: {self.year} {self.make} {self.model}")

    def display_info(self):
        """
        Método para mostrar la información del automóvil.
        """
        print(f"Marca: {self.make}")
        print(f"Modelo: {self.model}")
        print(f"Año: {self.year}")

    def __del__(self):
        """
        Destructor de la clase Car.
        Imprime un mensaje cuando el objeto es destruido.
        """
        print(f"Automóvil destruido: {self.year} {self.make} {self.model}")


# Ejemplo de uso de la clase Car

# Crear una instancia de Car
car1 = Car("Toyota", "Corolla", 2020)

# Mostrar la información del automóvil
car1.display_info()

# La instancia car1 será eliminada al final del script, llamando al destructor
