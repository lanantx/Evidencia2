import Cerdo, Conejo, Tortuga

op = 0
animal = ""
animales = []

print("Bienvenido al Zoologico")

while True:
    op = int(input("""

    Elige la opcion deseada:
    
    1) Agregar animal
    2) Ver animales
    3) Salir

    """)) 
    
    if op == 1:
        op2 = int(input("Elige un animal que quieras añadir: 1) Cerdo 2) Conejo 3) Tortuga: "))
        if op2 == 1:
            animal = "Cerdo"
            nombre = input("Ingresale un nombre: ")
            edad = int(input("Ingresa la edad: "))
            sexo = input("Ingresa el sexo: ")
            peso = int(input("Ingresa su peso: "))
            animales.append(animal)
            animales.append(nombre)
            animales.append(edad)
            animales.append(sexo)
            animales.append(peso)
            print(f"Se ha agregado el {animal}")
        elif op2 == 2:
            animal = "Conejo"
            nombre = input("Ingresale un nombre: ")
            edad = int(input("Ingresa la edad: "))
            sexo = input("Ingresa el sexo: ")
            peso = int(input("Ingresa su peso: "))
            animales.append(animal)
            animales.append(nombre)
            animales.append(edad)
            animales.append(sexo)
            animales.append(peso)
            print(f"Se ha agregado el {animal}")
        elif op2 == 3:
            animal = "Tortuga"
            nombre = input("Ingresale un nombre: ")
            edad = int(input("Ingresa la edad: "))
            sexo = input("Ingresa el sexo: ")
            peso = int(input("Ingresa su peso: "))
            animales.append(animal)
            animales.append(nombre)
            animales.append(edad)
            animales.append(sexo)
            animales.append(peso)
            print(f"Se ha agregado el {animal}")
        else:
            print("Tipo de animal no válido.")
    elif op == 2:
        print("\nAnimales:")
        for i in range(0, len(animales), 5):
            print("Nombre:", animales[i])
            print("Edad:", animales[i + 1])
            print("Sexo:", animales[i + 2])
            print("Peso:", animales[i + 3])
            print()

    elif op == 3:
        print("Saliendo del programa :D") 
        break
    else:
        print("Opcion incorrecta")


