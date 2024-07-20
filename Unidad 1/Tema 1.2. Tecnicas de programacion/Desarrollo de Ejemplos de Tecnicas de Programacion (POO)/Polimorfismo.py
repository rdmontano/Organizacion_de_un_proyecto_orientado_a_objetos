class Animal:
    def hacerSonido(self):
        pass

class Perro(Animal):
    def hacerSonido(self):
        return "Guau!"

class Gato(Animal):
    def hacerSonido(self):
        return "¡Miau!"

def hacer_sonido_animal(animal):
    print(animal.hacerSonido())

mi_perro = Perro()
mi_gato = Gato()

hacer_sonido_animal(mi_perro)  # Salida: Guau!
hacer_sonido_animal(mi_gato)   # Salida: ¡Miau!
