from Animal import Animal

class Zorro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre, "Zorro")

    def hacer_sonido(self):
        return "WHAT THE FOX SAY"
