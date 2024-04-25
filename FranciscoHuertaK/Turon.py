class Turon:
    def __init__(self,nombre,edad,sexo,largo,peso):
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = sexo
        self.__largo = largo
        self.__peso = peso

    def alimentacion(self):
        print("Los Turones comen carne.")

    def caracteristicas(self):
        print("Son mas robustos y compactos que otros miembros del genero Mustela.")

    def conservacion(self):
        print("No estan en peligro.")

    def distribucion(self):
        print("Se hallan en Europa.")

    def nombreCientifico(self):
        print("Mustela putorius")