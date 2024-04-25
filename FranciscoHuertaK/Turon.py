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

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,value):
        self.__nombre = value

    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self,value):
        self.__edad = value

    @property
    def sexo(self):
        return self.__sexo
    
    @sexo.setter
    def sexo(self,value):
        self.__sexo = value

    @property
    def largo(self):
        return self.__largo
    
    @largo.setter
    def largo(self,value):
        self.__largo = value

    @property
    def peso(self):
        return self.__peso
    
    @peso.setter
    def peso(self,value):
        self.__peso = value