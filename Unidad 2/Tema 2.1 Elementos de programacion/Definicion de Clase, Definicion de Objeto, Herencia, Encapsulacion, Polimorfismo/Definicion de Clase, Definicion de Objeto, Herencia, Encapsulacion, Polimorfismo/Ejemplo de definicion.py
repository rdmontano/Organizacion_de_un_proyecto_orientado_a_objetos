# Definición de la clase base Persona
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo público
        self.edad = edad  # Atributo público

    def mostrar_informacion(self):
        # Método para mostrar la información de la persona
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

# Definición de la clase derivada Empleado que hereda de Persona
class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base
        self.__salario = salario  # Atributo privado para encapsulación

    def mostrar_informacion(self):
        # Sobrescritura del método para demostrar polimorfismo
        super().mostrar_informacion()
        print(f"Salario: {self.__salario}")

    def obtener_salario(self):
        # Método getter para acceder al atributo privado __salario
        return self.__salario

    def establecer_salario(self, salario):
        # Método setter para modificar el atributo privado __salario
        if salario > 0:
            self.__salario = salario
        else:
            print("El salario debe ser positivo.")

# Función para demostrar polimorfismo
def mostrar_detalles(persona):
    # Este método acepta cualquier objeto que sea instancia de Persona o sus derivadas
    persona.mostrar_informacion()

# Crear instancias de las clases y utilizar sus métodos
persona1 = Persona("Juan", 30)
empleado1 = Empleado("Ana", 25, 50000)

# Demostración de Polimorfismo
mostrar_detalles(persona1)
mostrar_detalles(empleado1)

# Encapsulación: acceder y modificar el atributo privado a través de métodos públicos
print("\nSalario antes de modificar:", empleado1.obtener_salario())
empleado1.establecer_salario(55000)
print("Salario después de modificar:", empleado1.obtener_salario())
