class Estudiante:
    def __init__(self, nombre, edad, curso):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso
        self.calificaciones = {}

    def asignar_calificacion(self, asignatura, calificacion):
        self.calificaciones[asignatura] = calificacion

    def ver_calificaciones(self):
        print(f"Calificaciones de {self.nombre}:")
        for asignatura, calificacion in self.calificaciones.items():
            print(f"- {asignatura}: {calificacion}")

    def __str__(self):
        return f"Estudiante: {self.nombre} (Edad: {self.edad}, Curso: {self.curso})"


class Profesor:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad

    def asignar_calificacion(self, estudiante, asignatura, calificacion):
        estudiante.asignar_calificacion(asignatura, calificacion)

    def __str__(self):
        return f"Profesor: {self.nombre} (Especialidad: {self.especialidad})"


class Asignatura:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

    def __str__(self):
        return f"Asignatura: {self.nombre} (Código: {self.codigo})"


class Escuela:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []
        self.profesores = []

    def registrar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def contratar_profesor(self, profesor):
        self.profesores.append(profesor)

    def asignar_calificacion(self, profesor, estudiante, asignatura, calificacion):
        profesor.asignar_calificacion(estudiante, asignatura, calificacion)

    def mostrar_estudiantes(self):
        print(f"Estudiantes en {self.nombre}:")
        for estudiante in self.estudiantes:
            print(f"- {estudiante}")

    def mostrar_profesores(self):
        print(f"Profesores en {self.nombre}:")
        for profesor in self.profesores:
            print(f"- {profesor}")

    def __str__(self):
        return f"Escuela: {self.nombre}"


# Creación de objetos y demostración de interacción entre ellos
if __name__ == "__main__":
    # Crear asignaturas
    asignatura1 = Asignatura("Matemáticas", "MAT101")
    asignatura2 = Asignatura("Ciencias", "CIE102")
    asignatura3 = Asignatura("Historia", "HIS103")

    # Crear estudiantes
    estudiante1 = Estudiante("Carlos Méndez", 15, "10º grado")
    estudiante2 = Estudiante("María López", 16, "11º grado")

    # Crear profesores
    profesor1 = Profesor("Juan García", "Matemáticas")
    profesor2 = Profesor("Ana Martínez", "Ciencias")

    # Crear escuela
    escuela = Escuela("Colegio Buen Conocimiento")

    # Registrar estudiantes en la escuela
    escuela.registrar_estudiante(estudiante1)
    escuela.registrar_estudiante(estudiante2)

    # Contratar profesores en la escuela
    escuela.contratar_profesor(profesor1)
    escuela.contratar_profesor(profesor2)

    # Asignar calificaciones por parte de los profesores
    escuela.asignar_calificacion(profesor1, estudiante1, asignatura1, 85)
    escuela.asignar_calificacion(profesor2, estudiante1, asignatura2, 90)
    escuela.asignar_calificacion(profesor1, estudiante2, asignatura1, 92)
    escuela.asignar_calificacion(profesor2, estudiante2, asignatura2, 88)
    escuela.asignar_calificacion(profesor1, estudiante1, asignatura3, 80)
    escuela.asignar_calificacion(profesor2, estudiante2, asignatura3, 85)

    # Mostrar estudiantes y sus calificaciones
    escuela.mostrar_estudiantes()
    estudiante1.ver_calificaciones()
    estudiante2.ver_calificaciones()
