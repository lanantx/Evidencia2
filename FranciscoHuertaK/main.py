import Buitre, Turon, Pulpo

animales = []

while True:
    opcion = int(input("Elige una opcion: \n 1. Agregar animal \n 2. Ver todos los animales del mini-zoo \n 3. Salir \n "))
    if opcion == 1:
        opcionAnimal = int(input("¿Que animal quieres agregar? \n 1.Buitre \n 2.Turon \n 3.Pulpo \n "))
        nombre = input("¿Cual es su nombre?")
        edad = input("¿Cual es su edad?")
        sexo = input("¿Cual es su sexo?")
        tamaño = input("¿Cual es su tamaño?")
        peso = input("¿Cual es su peso?")
        if opcionAnimal == 1:
            nuevoAnimal = Buitre.Buitre(nombre,edad,sexo,tamaño,peso)
            animales.append(nuevoAnimal)
        elif opcionAnimal == 2:
            nuevoAnimal = Turon.Turon(nombre,edad,sexo,tamaño,peso)
            animales.append(nuevoAnimal)
        elif opcionAnimal == 3:
            nuevoAnimal = Pulpo.Pulpo(nombre,edad,sexo,tamaño,peso)
            animales.append(nuevoAnimal)
    elif opcion == 2:
        for x in animales:
            print(x)
    elif opcion == 3:
        break