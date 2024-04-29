#Programa principal
import lemur
import oso
import cebra

while True:
    print(f'MENU\n1. Agregar animal\n2. Ver todos los animales del mini-zoo\n3. Salir')
    opc = int(input('Elige una opcion: '))
    match(opc):
        case 1:
            pass
        case 2:
            pass
        case 3:
            break
        case _:
            print("ERROR. Ingrese una opcion valida.")