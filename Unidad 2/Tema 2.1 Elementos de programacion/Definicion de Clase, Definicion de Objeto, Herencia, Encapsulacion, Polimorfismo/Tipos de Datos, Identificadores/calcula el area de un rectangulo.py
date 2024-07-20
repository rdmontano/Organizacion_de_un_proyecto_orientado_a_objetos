# Programa para calcular el área de un rectángulo
# Este programa pide al usuario la base y la altura del rectángulo
# y calcula el área utilizando la fórmula: área = base * altura

def calcular_area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.

    :param base: La base del rectángulo (float)
    :param altura: La altura del rectángulo (float)
    :return: El área del rectángulo (float)
    """
    return base * altura

def main():
    # Solicitar la base y la altura al usuario
    base = float(input("Introduce la base del rectángulo: "))
    altura = float(input("Introduce la altura del rectángulo: "))

    # Calcular el área
    area = calcular_area_rectangulo(base, altura)

    # Mostrar el resultado
    print(f"El área del rectángulo es: {area}")

if __name__ == "__main__":
    main()
