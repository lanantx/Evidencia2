class Tigre:
    def __init__(self, Nombre, Edad, Peso, Tamaño, Sonido):
        self.__Nombre=Nombre
        self.__Edad=Edad
        self.__Peso=Peso
        self.__Tamaño=Tamaño
        self.__Sonido=Sonido

    @property
    def nombre(self):
        return self.__Nombre
    @nombre.setter
    def nombre(self,valor):
        self.__Nombre=valor
    
    @property
    def edad(self):
        return self.__Edad
    @edad.setter
    def edad(self, valor):
        self.__Edad=valor

    @property
    def peso(self):
        return self.__Peso
    @peso.setter
    def peso(self,valor):
        self.__Peso=valor

    @property
    def tamaño(self):
        return self.__Tamaño
    @tamaño.setter
    def tamaño(self,valor):
        self.__Tamaño=valor

    @property
    def sonido(self):
        return self.__Sonido
    @sonido.setter
    def sonido(self,valor):
        self.__Sonido=valor
