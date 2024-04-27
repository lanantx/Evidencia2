import pinguino
import Coyote
import burro

while True:

    opc = input("Bienvenido/a.\nElige una opción:\n1. Agregar Animal\n2. Imprimir información de animales registrados\n3. Salir\n")

    if opc == "1":
        
        opc2 = input("¿Qué animal desea agregar?\n1. Pinguino\n2. Coyote\n3. Burro\n")

        if opc2 == "1":
            pass
        elif opc2 == "2":
            pass
        elif opc2 == "3":
            pass
        else:
            print(f"Opción {opc2} no válida.\n")

    elif opc == "2":
        pass

    elif opc == "3":
        break
    
    else:
        print(f"Opción {opc} no válida.\n")
