from pinguino import Pinguino
from Coyote import Coyote
from burro import Burro

animales = {
    "Pingüino": [],
    "Coyote": [],
    "Burro": []
}

def agregar_animal(valor, tipo_animal):

    animal = None
    nombre = input(f"Nombre del {tipo_animal}: ")
    sexo = input(f"Sexo del {tipo_animal}: ")
    edad = input(f"Edad del {tipo_animal}: ")
    peso = input(f"Peso del {tipo_animal}: ")
    altura = input(f"Altura del {tipo_animal}: ")

    if valor == "1":
        animal = Pinguino(nombre, sexo, edad, peso, altura)
        animales["Pingüino"].append(animal)
    elif valor == "2":
        animal = Coyote(nombre, sexo, edad, peso, altura)
        animales["Coyote"].append(animal)
    else:
        animal = Burro(nombre, sexo, edad, peso, altura)
        animales["Burro"].append(animal)

    print(f"El {tipo_animal} {nombre} fue agregado.")

while True:

    opc = input("Bienvenido/a.\nElige una opción:\n1. Agregar Animal\n2. Imprimir información de animales registrados\n3. Salir\n")

    if opc == "1":
        
        opc2 = input("¿Qué animal desea agregar?\n1. Pingüino\n2. Coyote\n3. Burro\n")

        if opc2 == "1":
            agregar_animal(opc2, "Pingüino")
        elif opc2 == "2":
            agregar_animal(opc2, "Coyote")
        elif opc2 == "3":
            agregar_animal(opc2, "Burro")
        else:
            print(f"Opción {opc2} no válida.\n")

    elif opc == "2":
        pass

    elif opc == "3":
        break
    
    else:
        print(f"Opción {opc} no válida.\n")
