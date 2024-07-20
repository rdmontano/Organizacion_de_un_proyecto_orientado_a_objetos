class Libro:
    def __init__(self, titulo, autor, genero):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero

    def obtener_info(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Género: {self.genero}"

# Crear un nuevo libro
mi_libro = Libro("El código Da Vinci", "Dan Brown", "Misterio")
print(mi_libro.obtener_info())  # Salida: Título: El código Da Vinci, Autor: Dan Brown, Género: Misterio
