from Hipopotamo import Hipopotamo
from Koala import Koala
from Mono import Mono

class mi_zoologico:
    def __init__(self):
        self.mis_animales=[]

    def añadir_animales(self,animalNuevo):
        self.mis_animales.append(animalNuevo)

    def ver_animales(self):
        for animales in self.mis_animales:
            print(animales)

admin_mizoo = mi_zoologico()

while True:
    print("1. Agregar animal")
    print("2. Ver animales")
    print("3. Salir")
    opcion = int(input("¿Que opcion desea esoger?: "))

    if opcion == 1:
        print("1. Hipopotamo")
        print("2. Koala")
        print("3. Mono")
        animal = int(input("¿Que animal deseas agregar?: ")

        if animal == 1:
            nombre = input("Ingresa el nombre del hipopotamo: ")
            edad = input("Ingresa la edad del hipopotamo: ")
            tamaño = input("Ingresa el tamaño del hipopotamo: ")
            peso = input("Ingresa el peso del hipopotamo: ")
            altura = input("Ingresa el altura del hipopotamo: ")
            hipopotamonuevo=hipopotamo(nombre,edad,tamaño,peso,altura)
            admin_mizoo.añadir_animales(hipopotamonuevo)

        elif animal == 2:
            nombre = input("Ingresa el nombre del koala: ")
            edad = input("Ingresa la edad del koala: ")
            tamaño = input("Ingresa el tamaño del koala: ")
            peso = input("Ingresa el peso del koala: ")
            altura = input("Ingresa el altura del koala: ")
            koalanuevo=koala(nombre,edad,tamaño,peso,altura)
            admin_mizoo.añadir_animales(koalanuevo)

        elif animal == 3:
            nombre = input("Ingresa el nombre del mono: ")
            edad = input("Ingresa la edad del mono: ")
            tamaño = input("Ingresa el tamaño del mono: ")
            peso = input("Ingresa el peso del mono: ")
            altura = input("Ingresa el altura del mono: ")
            monomonuevo=mono(nombre,edad,tamaño,peso,altura)
            admin_mizoo.añadir_animales(mononuevo)
        
    elif opcion == 2:
        admin_mizoo.ver_animales()
    