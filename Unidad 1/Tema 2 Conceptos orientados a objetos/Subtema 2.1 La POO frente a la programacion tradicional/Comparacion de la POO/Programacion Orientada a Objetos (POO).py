class ClimaDiario:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperaturas(self):
        for i in range(7):
            temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
            self.temperaturas.append(temp)

    def calcular_promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)

# Clase para coordinar el proceso y representar la semana completa
class PromedioSemanalClima:
    def __init__(self):
        self.clima_diario = ClimaDiario()

    def ejecutar(self):
        print("Programa para calcular el promedio semanal del clima")
        self.clima_diario.ingresar_temperaturas()
        promedio = self.clima_diario.calcular_promedio()
        print(f"El promedio semanal de las temperaturas es: {promedio:.2f}")

# Ejecución del programa
if __name__ == "__main__":
    promedio_semanal_clima = PromedioSemanalClima()
    promedio_semanal_clima.ejecutar()
