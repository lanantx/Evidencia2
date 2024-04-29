from Aguila import Aguila
from Caballo import Caballo
from Cotorro import Cotorro 

class Zoologico:
    def __init__(self):
        self.animales = []

    def añadirA(self, animalNuevo):
        self.animales.append(animalNuevo)

    def mostrarA(self):
        for animales in self.animales:
            print(animales)

adminZoo = Zoologico()
while True:
    opcion = int(input("\n1.Agregar animal \n2.Ver animales \n3.Salir"))
    if opcion == 1:
        animal = int(input("Que animal se desea agregar: \n1.Aguila \n2.Caballo \n3.Cotorro"))
        if animal == 1:
            nombre = input("Ingresa el nombre: ")
            sexo = input("Ingresa el sexo: ")
            edad = input("Ingresa la edad: ")
            peso = input("Ingresa el peso: ")
            altura = input("Ingresa la altura: ")
            aguilaNueva = Aguila(nombre, sexo, edad, peso, altura)
            adminZoo.añadirA(aguilaNueva)

        elif animal == 2:
            nombre = input("Ingresa el nombre: ")
            sexo = input("Ingresa el sexo: ")
            edad = input("Ingresa la edad: ")
            peso = input("Ingresa el peso: ")
            altura = input("Ingresa la altura: ")
            caballoNuevo = Caballo(nombre, sexo, edad, peso, altura)
            adminZoo.añadirA(caballoNuevo)
            
        elif animal == 3:
            nombre = input("Ingresa el nombre: ")
            sexo = input("Ingresa el sexo: ")
            edad = input("Ingresa la edad: ")
            peso = input("Ingresa el peso: ")
            altura = input("Ingresa la altura: ")
            cotorroNuevo = Cotorro(nombre, sexo, edad, peso, altura)
            adminZoo.añadirA(cotorroNuevo)

        elif opcion == 2:
            adminZoo.mostrarA()

        elif opcion == 3:
            break