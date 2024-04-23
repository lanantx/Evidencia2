from Animal import Animal

class Panda_Rojo(Animal):
    def __init__(self, nombre):
        super().__init__(nombre, "Panda Rojo")

    def hacer_sonido(self):
        return "No comas mas domplings Poh"
