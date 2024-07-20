# Programa para contar palabras en una frase

def contar_palabras(frase):
    """
    Función que cuenta la cantidad de palabras en una frase dada.
    :param frase: str, frase ingresada por el usuario
    :return: int, cantidad de palabras en la frase
    """
    palabras = frase.split()
    return len(palabras)

# Entrada de usuario
frase_ingresada = input("Ingresa una frase para contar la cantidad de palabras: ")

# Contar palabras en la frase ingresada
cantidad_palabras = contar_palabras(frase_ingresada)
print(f"La frase '{frase_ingresada}' tiene {cantidad_palabras} palabras.")
