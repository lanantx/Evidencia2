from Animal import Animal

class Koi(Animal):
    def __init__(self, nombre):
        super().__init__(nombre, "Koi")

    def hacer_sonido(self):
        return "glugluglu 私は魚です glu glu glu"
