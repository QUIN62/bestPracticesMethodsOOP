class Alumno:
    def __init__(self, nombre, apellido_paterno, apellido_materno, no_control, semestre):
        # Atributos privados
        self.__nombre = nombre
        self.__apellido_paterno = apellido_paterno
        self.__apellido_materno = apellido_materno
        self.__no_control = no_control
        self.__semestre = semestre

    # Métodos para establecer los valores (setters)
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido_paterno(self, apellido_paterno):
        self.__apellido_paterno = apellido_paterno

    def set_apellido_materno(self, apellido_materno):
        self.__apellido_materno = apellido_materno

    def set_no_control(self, no_control):
        self.__no_control = no_control

    def set_semestre(self, semestre):
        self.__semestre = semestre

    # Métodos para obtener los valores (getters)
    def get_nombre(self):
        return self.__nombre

    def get_apellido_paterno(self):
        return self.__apellido_paterno

    def get_apellido_materno(self):
        return self.__apellido_materno

    def get_no_control(self):
        return self.__no_control

    def get_semestre(self):
        return self.__semestre

# Ejemplo de uso
alumno1 = Alumno("Juan", "Pérez", "Gómez", "12345678", 3)

# Obtener valores
print(alumno1.get_nombre())          # Juan
print(alumno1.get_apellido_paterno())  # Pérez
print(alumno1.get_apellido_materno())  # Gómez
print(alumno1.get_no_control())        # 12345678
print(alumno1.get_semestre())          # 3

# Modificar valores
alumno1.set_nombre("Carlos")
alumno1.set_semestre(4)

# Obtener los valores modificados
print(alumno1.get_nombre())          # Carlos
print(alumno1.get_semestre())        # 4
