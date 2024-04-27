from pato import pato
from canguro import canguro
from llama import llama

class zoologico:
    def __init__(self):
        self.mianimal=[]

    def añadirAnimal(self, animalNuevo):
        self.mianimal.append(animalNuevo)

    def verAnimales(self):
        for animales in self.mianimal:
            print(animales)


adminzoo=zoologico()

while True:
    opcion = int(input("1. Agregar animal \n 2. Ver los animales \n 3. Salir \n "))
    if opcion == 1:
        animal = int(input("Que animal deseas agregar: \n 1. Pato \n 2. Canguro \n 3. Llama \n" ))
        if animal == 1:
            nombre = input("Ingresa el nombre del pato: ")
            edad = input("Ingresa la edad del pato: ")
            peso = input("Ingresa el peso del pato: ")
            patonuevo=pato(nombre,edad,peso)
            adminzoo.añadirAnimal(patonuevo)
        elif animal == 2:
            nombre = input("Ingresa el nombre del canguro: ")
            edad = input("Ingresa la edad del canguro: ")
            peso = input("Ingresa el peso del canguro: ")
            canguronuevo=canguro(nombre,edad,peso)
            adminzoo.añadirAnimal(canguronuevo)
        elif animal == 3:
            nombre = input("Ingresa el nombre de la llama: ")
            edad = input("Ingresa la edad de la llama: ")
            peso = input("Ingresa el peso de la llama: ")
            llamanueva=llama(nombre,edad,peso)
            adminzoo.añadirAnimal(llamanueva)

    elif opcion == 2:
        adminzoo.verAnimales()

    elif opcion == 3:
        break


                    
                           