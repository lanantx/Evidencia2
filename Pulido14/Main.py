import Ballena
import Delfin
import Serpiente

animales = []

while True:
  opcion = int(input("Elige una opción: \n"
                      "1. Agregar animal (Ballena, Delfín o Serpiente) \n"
                      "2. Ver todos los animales del mini-zoo \n"
                      "3. Salir \n"))

  if opcion == 1:
    tipo_animal = input("¿Qué animal quieres agregar? (Ballena, Delfín o Serpiente): ")

    if tipo_animal == "ballena":
      nombre = input("¿Cuál es su nombre? \n")
      edad = int(input("¿Cuál es su edad? \n"))
      longitud = float(input("Ingrese la longitud del animal: "))
      peso = float(input("Ingrese el peso del animal: "))
      especie = input("Ingrese la especie del animal: ")
      nuevo_animal = Ballena(nombre, edad, longitud, peso, especie)
      animales.append(nuevo_animal)
      print(f"Se ha agregado la ballena {nombre} a la lista de animales.")

    elif tipo_animal == "delfin":
      nombre = input("¿Cuál es su nombre? \n")
      edad = int(input("¿Cuál es su edad? \n"))
      longitud = float(input("Ingrese la longitud del animal: "))
      peso = float(input("Ingrese el peso del animal: "))
      especie = input("Ingrese la especie del animal: ")
      nuevo_animal = Delfin(nombre, edad, longitud, peso, especie)
      animales.append(nuevo_animal)
      print(f"Se ha agregado el delfín {nombre} a la lista de animales.")

    elif tipo_animal == "serpiente":
      nombre = input("¿Cuál es su nombre? \n")
      edad = int(input("¿Cuál es su edad? \n"))
      longitud = float(input("Ingrese la longitud del animal: "))
      peso = float(input("Ingrese el peso del animal: "))
      especie = input("Ingrese la especie del animal: ")
      nuevo_animal = Serpiente(nombre, edad, longitud, peso, especie)
      animales.append(nuevo_animal)
      print(f"Se ha agregado la serpiente {nombre} a la lista de animales.")

    else:
      print("El animal invalido. Favor de elejir uno de los 3 animales de la lista")

  elif opcion == 2:
    if not animales:
      print("No hay niungun animal registrado en el mini-zoo.")
    else:
      print("Animales registrados:")
      for animal in animales:
        print(f"{animal.tipo}: {animal.nombre}")

  elif opcion == 3:
    print("Saliendo del programa...")
    break

  else:
    print("Opción no válida. Favor de seleccionar una opción válida.")

