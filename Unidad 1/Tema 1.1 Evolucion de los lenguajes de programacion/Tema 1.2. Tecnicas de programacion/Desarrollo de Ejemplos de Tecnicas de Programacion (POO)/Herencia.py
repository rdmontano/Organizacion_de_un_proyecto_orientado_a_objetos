class Vehiculo:
    def __init__(self, velocidad):
        self.velocidad = velocidad

    def acelerar(self, incremento):
        self.velocidad += incremento

# Clase hija que hereda de Vehiculo
class Coche(Vehiculo):
    def __init__(self, velocidad, marca):
        super().__init__(velocidad)
        self.marca = marca

# Clase hija que hereda de Vehiculo
class Bicicleta(Vehiculo):
    def __init__(self, velocidad, tipo):
        super().__init__(velocidad)
        self.tipo = tipo

mi_coche = Coche(100, "Toyota")
mi_coche.acelerar(20)
print(mi_coche.velocidad)  # Salida: 120

mi_bicicleta = Bicicleta(25, "Montaña")
mi_bicicleta.acelerar(5)
print(mi_bicicleta.velocidad)  # Salida: 30
