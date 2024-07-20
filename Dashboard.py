import os
import subprocess

def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print(f"El archivo {ruta_script} no se encontró.")
    except PermissionError:
        print(f"No tienes permisos para leer el archivo {ruta_script}.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo {ruta_script}: {e}")

def abrir_pdf(ruta_pdf):
    ruta_pdf_absoluta = os.path.abspath(ruta_pdf)
    try:
        if os.name == 'posix':  # Para sistemas operativos tipo Unix (Linux, MacOS)
            subprocess.call(['open', ruta_pdf_absoluta])
        elif os.name == 'nt':  # Para Windows
            os.startfile(ruta_pdf_absoluta)
        else:
            print(f"No se puede abrir el archivo PDF en este sistema operativo: {os.name}")
    except Exception as e:
        print(f"Ocurrió un error al abrir el archivo PDF: {e}")

def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(os.path.abspath(__file__))

    opciones = {
        '1': 'Unidad 1/Tema 1.1 Evolucion de los lenguajes de programacion/Evolucion de los Lenguajes de Programacion.pdf',
        '2': 'Unidad 1/Tema 1.2. Tecnicas de programacion/Desarrollo de Ejemplos de Tecnicas de Programacion (POO)/Abstraccion.py',
        '3': 'Unidad 1/Tema 1.2. Tecnicas de programacion/Desarrollo de Ejemplos de Tecnicas de Programacion (POO)/Encapsulacion.py',
        '4': 'Unidad 1/Tema 1.2. Tecnicas de programacion/Desarrollo de Ejemplos de Tecnicas de Programacion (POO)/Herencia.py',
        '5': 'Unidad 1/Tema 1.2. Tecnicas de programacion/Desarrollo de Ejemplos de Tecnicas de Programacion (POO)/Polimorfismo.py',
        '6': 'Unidad 1/Tema 2 Conceptos orientados a objetos/Subtema 2.1 La POO frente a la programacion tradicional/Comparacion de la POO/Programacion Orientada a Objetos (POO).py',
        '7': 'Unidad 1/Tema 2 Conceptos orientados a objetos/Subtema 2.1 La POO frente a la programacion tradicional/Comparacion de la POO/Programacion Tradicional.py',
        '8': 'Unidad 1/Tema 2 Conceptos orientados a objetos/Subtema 2.2 Caracteristicas de la programacion orientada a objetos/EjemplosMundoReal_POO/Gestion de un restaurante.py',
        '9': 'Unidad 1/Tema 2 Conceptos orientados a objetos/Subtema 2.2 Caracteristicas de la programacion orientada a objetos/EjemplosMundoReal_POO/Gestion de una escuela.py',
        '10': 'Unidad 1/Tema 2 Conceptos orientados a objetos/Subtema 2.2 Caracteristicas de la programacion orientada a objetos/EjemplosMundoReal_POO/Gestion de una libreria.py',
        '11': 'Unidad 2/Tema 2.1 Elementos de programacion/Definicion de Clase, Definicion de Objeto, Herencia, Encapsulacion, Polimorfismo/Ejemplo de definicion.py',
        '12': 'Unidad 2/Tema 2.1 Elementos de programacion/Tipos de Datos, Identificadores/calcula el area de un rectangulo.py',
        '13': 'Unidad 2/Tema 2.1 Elementos de programacion/Tipos de Datos, Identificadores/Contar palabras.py',
        '14': 'Unidad 2/Tema 2.1 Elementos de programacion/Tipos de Datos, Identificadores/Par o Impar.py',
        '15': 'Unidad 2/Tema 2.2 Constructores y destructores/Subtema 2.2.1 Fundamentos de Constructores y destructores/Constructores y Destructores/Constructor de la clase Car.py',
        '16': 'Unidad 2/Tema 2.2 Constructores y destructores/Subtema 2.2.1 Fundamentos de Constructores y destructores/Constructores y Destructores/Constructor de la clase Person.py',
        '17': 'Unidad 2/Tema 2.2 Constructores y destructores/Subtema 2.2.2 Organizacion de un proyecto orientado a objetos/Dashboard.py'
    }

    while True:
        print(f"\n---------------------------------------------------------------------------\n")
        print("\nMENU PRINCIPAL")
        print(f"\n---------------------------------------------------------------------------\n")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {os.path.basename(opciones[key])}")
        print("0 - Salir")

        eleccion = input("ELIGE UNA OPCION PARA VER SU CONTENIDO o '0' PARA SALIR: ")
        print(f"\n---------------------------------------------------------------------------\n")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            if eleccion == '1':
                abrir_pdf(ruta_script)
            elif os.path.isfile(ruta_script):
                mostrar_codigo(ruta_script)
            else:
                print(f"El archivo {ruta_script} no es un archivo de texto legible o no existe.")
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()
