from Gorilla import gorilla
from Jirafa import jirafa
from Nutria import  Nutria

class zoo:
    def __init__(self):
        self.animala=[]

    def AñadirAnimal(self, animalN):
        self.animala.append(animalN)

    def verAnimales(self):
        for animales in self.animala:
            print(animales)


adminzoo=zoo()

while True:
    opcion = int(input("1. Agregar animal  2. Ver los animales 3.Info animal 4. Salir  "))
    if opcion == 1:
        animal = int(input("Animal por agregar:  1. Gorilla  2. Jirafa  3. Nutria " ))
        if animal == 1:
            nombre = input("Ingresa el nombre: ")
            edad = input("Ingresa la edad: ")
            peso = input("Ingresa el peso: ")
            sexo = input("Ingresa el sexo: ")
            tamaño = input("Ingresa el tamaño: ")
            gorillaN=gorilla(nombre,edad,peso,sexo,tamaño)
            adminzoo.AñadirAnimal(gorillaN)
            print("Animal agregado exitosamente!")

        
        elif animal == 2:
            nombre = input("Ingresa el nombre: ")
            edad = input("Ingresa la edad: ")
            peso = input("Ingresa el peso: ")
            sexo = input("Ingresa el sexo: ")
            tamaño = input("Ingresa el tamaño: ")
            JirafaN=jirafa(nombre,edad,peso,sexo,tamaño)
            adminzoo.AñadirAnimal(JirafaN)
            print("Animal agregado exitosamente!")

        
        elif animal == 3:
            nombre = input("Ingresa el nombre: ")
            edad = input("Ingresa la edad: ")
            peso = input("Ingresa el peso: ")
            sexo = input("Ingresa el sexo: ")
            tamaño = input("Ingresa el tamaño: ")
            nutriaN=Nutria(nombre,edad,peso,sexo,tamaño)
            adminzoo.AñadirAnimal(nutriaN)
            print("Animal agregado exitosamente!")

        
        elif opcion == 2:
            adminzoo.verAnimales()
        elif opcion == 4:
            break