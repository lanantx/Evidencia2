from Capybara import Capybara
from Cocodrilo import Cocodrilo
from Leopardo import Leopardo

class ZOO:
    def __init__(self):
        self.__Lista_Animales = []
    
    def Agregar_Animales(self,Animal_Nuevo):
        self.__Lista_Animales.append(Animal_Nuevo)
    
    def Mostrar_todos(self):
        for i in self.__Lista_Animales:
            i.info()
            print("////////////")

AdminZOO = ZOO()

while True:
    print("/////Bienvenido al ZOO///// \n 1.-Agregar Animal \n 2.- Ver Todos los Animales")
