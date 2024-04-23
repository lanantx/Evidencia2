from Koi import koi
from Panda_Rojo import panda_rojo
from Zorro import zorro

while True:
    print("Pez Koi: Inserte 1\nPanda Rojo: Inserte 2\nZorro: Inserte 3")
    opcion = input("¿Qué opción buscas?\n(Presiona enter para salir): ")

    if opcion == '1':
        koi()
    elif opcion == '2':
        panda_rojo()
    elif opcion == '3':
        zorro()
    else:
        print("Saliendo del programa...")
        break