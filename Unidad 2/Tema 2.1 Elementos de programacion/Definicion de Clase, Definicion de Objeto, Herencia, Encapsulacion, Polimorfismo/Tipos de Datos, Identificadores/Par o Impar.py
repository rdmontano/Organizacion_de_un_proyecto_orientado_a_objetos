# Programa para determinar si un número es par o impar

def es_par(numero):
    """
    Función que determina si un número dado es par o impar.
    :param numero: int, número entero a evaluar
    :return: bool, True si el número es par, False si es impar
    """
    if numero % 2 == 0:
        return True
    else:
        return False

# Entrada de usuario
numero_ingresado = int(input("Ingresa un número entero para verificar si es par o impar: "))

# Determinar si es par o impar
if es_par(numero_ingresado):
    print(f"El número {numero_ingresado} es par.")
else:
    print(f"El número {numero_ingresado} es impar.")
