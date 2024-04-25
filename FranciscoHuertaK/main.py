import Buitre, Turon, Pulpo

animales = []

while True:
    opcion = int(input("Elige una opcion: \n 1. Agregar animal \n 2. Ver todos los animales del mini-zoo \n 3. Salir \n "))
    if opcion == 1:
        opcionAnimal = int(input("¿Que animal quieres agregar? \n 1.Buitre \n 2.Turon \n 3.Pulpo \n "))
        nombre = input("¿Cual es su nombre? \n")
        edad = input("¿Cual es su edad? \n")
        sexo = input("¿Cual es su sexo? \n")
        tamaño = input("¿Cual es su tamaño? \n")
        peso = input("¿Cual es su peso? \n")
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