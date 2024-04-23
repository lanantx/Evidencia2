class Animal:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_especie(self):
        return self.especie

    def set_especie(self, especie):
        self.especie = especie

    def hacer_sonido(self):
        pass