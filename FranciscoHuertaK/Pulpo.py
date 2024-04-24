class Pulpo:
    def __init__(self,nombre,edad,sexo,largo,peso):
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = sexo
        self.__largo = largo
        self.__peso = peso

    def alimentacion(self):
        print("Los pulpos comen carne.")

    def caracteristicas(self):
        print("Los pulpos tienen 8 extremidades.")

    def conservacion(self):
        print("Se cree no estan en peligro.")

    def distribucion(self):
        print("Los pulpos se hallan en todos los oceanos.")

    def orden(self):
        print("Pertenecen al orden Octopoda")
