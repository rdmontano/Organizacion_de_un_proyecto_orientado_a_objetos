class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial  # Utilizamos doble guion bajo para hacer el atributo privado

    def depositar(self, cantidad):
        self.__saldo += cantidad

    def retirar(self, cantidad):
        if self.__saldo >= cantidad:
            self.__saldo -= cantidad
        else:
            print("Saldo insuficiente")

    def obtener_saldo(self):
        return self.__saldo

# Crear una nueva cuenta bancaria
mi_cuenta = CuentaBancaria(1000)
mi_cuenta.depositar(500)
mi_cuenta.retirar(200)
print(mi_cuenta.obtener_saldo())  # Salida: 1300
