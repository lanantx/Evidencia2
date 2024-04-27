class pato:
    def __init__(self, nombre,edad,peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso

    def sonido(self):
        print("CUACK")

    def vida (self):
        print(f"{self.nombre}, puede vivir hasta 10 años")

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,valor):
        self.__nombre=valor

    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self,valor):
        self.__edad=valor

    @property
    def peso(self):
        return self.__peso
    @peso.setter
    def peso(self,valor):
        self.__peso=valor

    



