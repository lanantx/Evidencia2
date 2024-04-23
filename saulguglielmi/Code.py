from Koi import Koi
from Panda_Rojo import Panda_Rojo
from Zorro import Zorro

def agregar_animal(mini_zoo):
    print("Seleccione el tipo de animal a agregar:")
    print("1. Koi")
    print("2. Panda Rojo")
    print("3. Zorro")
    opcion = int(input())

    nombre = input("Ingrese el nombre del animal: ")

    if opcion == 1:
        animal = Koi(nombre)
    elif opcion == 2:
        animal = Panda_Rojo(nombre)
    elif opcion == 3:
        animal = Zorro(nombre)
    else:
        print("Opción no válida")
        return

    mini_zoo.append(animal)
    print("Animal agregado con éxito!")

def ver_animales(mini_zoo):
    print("Animales en el mini-zoo:")
    for animal in mini_zoo:
        print(f"Nombre: {animal.get_nombre()}, Especie: {animal.get_especie()}, Sonido: {animal.hacer_sonido()}")

def menu():
    mini_zoo = []

    while True:
        print("Opciones del programa:")
        print("1. Agregar animal")
        print("2. Ver todos los animales del mini-zoo")
        print("3. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            agregar_animal(mini_zoo)
        elif opcion == 2:
            ver_animales(mini_zoo)
        elif opcion == 3:
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    menu()

