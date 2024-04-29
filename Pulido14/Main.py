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
    nombre = input("¿Cuál es su nombre? \n")
    edad = input("¿Cuál es su edad? \n")
    sexo = input("¿Cuál es su especie? \n")
    tamaño = input("¿Cuál es su longitud? \n")
    peso = input("¿Cuál es su peso? \n")

    if tipo_animal == "Ballena":
      nuevo_animal = Ballena(nombre, edad, sexo, tamaño, peso)
    elif tipo_animal == "Delfín":
      nuevo_animal = Delfin(nombre, edad, sexo, tamaño, peso)
    elif tipo_animal == "Serpiente":
      nuevo_animal = Serpiente(nombre, edad, sexo, tamaño, peso)
    else:
      print("Animal no reconocido. Favor de elegir entre Ballena, Delfín o Serpiente.")
      continue

    animales.append(nuevo_animal)

  elif opcion == 2:
    for animal in animales:
      print(animal)

  elif opcion == 3:
    break


  
