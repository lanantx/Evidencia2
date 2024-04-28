from Hipopotamo import Hipopotamo
from Koala import Koala
from Mono import Mono

class mi_zoologico:
    def __init__(self):
        self.mis_animales=[]

    def añadir_animales(self, animalNuevo):
        self.mis_animales.append(animalNuevo)

    def ver_animales(self):
        for animales in self.mis_animales:
            print(animales)

