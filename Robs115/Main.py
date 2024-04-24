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
    opcion = int(input(print("/////Bienvenido al ZOO///// \n 1.-Agregar Animal \n 2.- Ver Todos los Animales\n")))
    if opcion == 1 :
        Animal = int(input("Que animal desea Agregar \n1.-Capybara\n2.-Leopardo\n3.-Cocodrilo\n "))
        if Animal == 1:
            Nombre = input("Cual es el nombre de su Capybara ")
            Peso = input("Cual es el Peso de su Capybara ")
            Edad = input("Cual es el Edad de su Capybara ")
            Tamaño = input("Cual es el Tamaño de su Capybara ")
            ComidaFav = input("Cual es el Comida Favorita de su Capybara ")
            AnimalNuevo = Capybara(Nombre,Peso,Edad,Tamaño,ComidaFav)
            AdminZOO.Agregar_Animales(AnimalNuevo)
        elif Animal == 2:
            Nombre = input("Cual es el nombre de su Leopardo ")
            Peso = input("Cual es el Peso de su Leopardo ")
            Edad = input("Cual es el Edad de su Leopardo ")
            Tamaño = input("Cual es el Tamaño de su Leopardo ")
            ComidaFav = input("Cual es el Comida Favorita de su Leopardo ")
            AnimalNuevo = Leopardo(Nombre,Peso,Edad,Tamaño,ComidaFav)
            AdminZOO.Agregar_Animales(AnimalNuevo)
        elif Animal == 3:
            Nombre = input("Cual es el nombre de su Cocodrilo ")
            Peso = input("Cual es el Peso de su Cocodrilo ")
            Edad = input("Cual es el Edad de su Cocodrilo ")
            Tamaño = input("Cual es el Tamaño de su Cocodrilo ")
            ComidaFav = input("Cual es el Comida Favorita de su Cocodrilo ")
            AnimalNuevo = Cocodrilo(Nombre,Peso,Edad,Tamaño,ComidaFav)
            AdminZOO.Agregar_Animales(AnimalNuevo)
    elif opcion == 2:
        print(AdminZOO.Mostrar_todos())