
from GARZA import GARZA
from PUMA import PUMA
from TUCAN import TUCAN

class mini_zoo:
    def __init__(self):
        self.animales = []

    def agregar_animal(self, animal):
        self.animales.append(animal)

    def mostrar_lista(self):
        print("Lista de animales en el mini-zoo:")
        for animal in self.animales:
            print(animal.nombre)  

if __name__ == "__main__":
    zoo = mini_zoo()

    while True:
        print("\nPROGRAMA DE MINI-ZOO")
        print("1. Agregar animal")
        print("2. Ver registro de animales")
        print("3. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            print("\nSELECCIÓN DE ANIMAL A AÑADIR")
            print("1. Garza")
            print("2. Puma")
            print("3. Tucán")
            tipo_animal = int(input("Seleccione el tipo de animal: "))

            if tipo_animal == 1:
                nombre = input("Escriba el nombre de la Garza: ")
                color = input("¿De qué color es la Garza?: ")
                edad = int(input("¿Cuántos años tiene?: "))
                peso = float(input("¿Cuánto pesa?: "))
                longitud_patas = float(input("Ingrese la medida de las patas en cm: "))
                garza = GARZA(nombre, color, edad, peso, longitud_patas)
                zoo.agregar_animal(garza)
                print("Garza agregada al mini-zoo.")

            elif tipo_animal == 2:
                nombre = input("Escriba el nombre del Puma: ")
                color = input("¿De qué color es el Puma?: ")
                edad = int(input("¿Cuántos años tiene?: "))
                peso = float(input("¿Cuánto pesa?: "))
                velocidad_max = float(input("Ingrese la velocidad máxima de carrera en km/h: "))
                puma = PUMA(nombre, color, edad, peso, velocidad_max)
                zoo.agregar_animal(puma)
                print("Puma agregado al mini-zoo.")

            elif tipo_animal == 3:
                nombre = input("Escriba el nombre del Tucán: ")
                color_plumas = input("¿De qué color son las plumas del Tucán?: ")
                longitud_pico = float(input("Ingrese la longitud del pico en cm: "))
                largo_alas = float(input("Ingrese el largo de las alas en cm: "))
                velocidad_vuelo = float(input("Ingrese la velocidad de vuelo en km/h: "))
                tucan = TUCAN(nombre, color_plumas, longitud_pico, largo_alas, velocidad_vuelo)
                zoo.agregar_animal(tucan)
                print("Tucán agregado al mini-zoo.")

        elif opcion == 2:
            zoo.mostrar_lista()

        elif opcion == 3:
            print("Saliendo del programa...")
            break

        else:
            print("¡Opción no válida! Por favor seleccione una opción válida.")


    

    