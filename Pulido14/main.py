import Ballena
import Delfin
import Serpiente

animales = []

while True:
    opcion = int(input("Elige una opción: \n 1. Agregar animal \n 2. Ver todos los animales del mini-zoo \n 3. Salir \n "))
    if opcion == 1:
        opcion_animal = int(input("¿Qué animal quieres agregar? \n 1. Serpiente \n 2. Ballena \n 3. Delfín \n "))
        nombre = input("¿Cuál es su nombre? \n")
        edad = input("¿Cuál es su edad? \n")
        especie = input("¿Cuál es su especie? \n")
        longitud = input("¿Cuál es su longitud? \n")
        peso = input("¿Cuál es su peso? \n")
        if opcion_animal == 1:
            nuevo_animal = Serpiente(nombre, edad, especie, longitud, peso)
            animales.append(nuevo_animal)
        elif opcion_animal == 2:
            nuevo_animal = Ballena(nombre, edad, especie, longitud, peso)
            animales.append(nuevo_animal)
        elif opcion_animal == 3:
            nuevo_animal = Delfin(nombre, edad, especie, longitud, peso)
            animales.append(nuevo_animal)
    
    