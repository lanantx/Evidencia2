import Camaleon
import Pinguino
import Tigre

class AdminZoo:
    def __init__(self):
        self.misanimales=[]
    
    def agregarAnimal(self,nuevoAnimal):
        self.misanimales.append(nuevoAnimal)
    
    def info(self):
        for animales in self.misanimales:
            print(animales)

while True:
    op=int(input("1. Agregar animal \n2. Ver todos los animales del mini-zoo \n3. Salir"))
    if op==1:
        pass
    elif op==2:
        pass
    elif op==3:
        pass