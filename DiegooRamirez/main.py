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
            
adzoo=AdminZoo()

while True:
    op=int(input("1. Agregar animal \n2. Ver todos los animales del mini-zoo \n3. Salir\nElija el numero de opcion que desee: "))
    if op==1:
        opAnimal=int(input("1. Camaleon\n2. Pinguino\n3. Tigre\nElija el numero de opcion que desee: "))
        if opAnimal==1:
            nombre=input("Ingrese el nombre del Camaleon: ")
            edad=input("Ingrese la edad del Camaleon: ")
            peso=input("Ingrese el peso en kg del Camaleon: ")
            tamaño=input("Ingrese el tamaño del Camaleon en cm: ")
            color=input("Ingrese el color del Camaleon: ")
            nuevoCamaleon=Camaleon(nombre,edad,peso,tamaño,color)
            adzoo.agregarAnimal(nuevoCamaleon)
        elif opAnimal==2:
            nombre=input("Ingrese el nombre del Pinguino: ")
            edad=input("Ingrese la edad del Pinguino: ")
            peso=input("Ingrese el peso en kg del Pinguino: ")
            tamaño=input("Ingrese el tamaño del Pinguino en cm: ")
            vuela_novuela=input("Su pinguino vuela o no vuela: ")
            nuevoPinguino=Pinguino(nombre,edad,peso,tamaño,vuela_novuela)
            adzoo.agregarAnimal(nuevoPinguino)
        elif opAnimal==3:
            nombre=input("Ingrese el nombre del Pinguino: ")
            edad=input("Ingrese la edad del Pinguino: ")
            peso=input("Ingrese el peso en kg del Pinguino: ")
            tamaño=input("Ingrese el tamaño del Pinguino en cm: ")
            sexo=input("Ingrese el sexo del Tigre: ")
            nuevoTigre=Pinguino(nombre,edad,peso,tamaño,sexo)
            adzoo.agregarAnimal(nuevoTigre)
    elif op==2:
        pass
    elif op==3:
        break