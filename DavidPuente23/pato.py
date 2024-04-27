class pato:
    def __init__(self, nombre,edad,peso, color, sexo):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.color = color
        self.sexo = sexo

    def sonido(self):
        print("CUACK")

    def vida (self):
        print(f"{self.nombre}, puede vivir hasta 10 años")

    def comida(self):
        print(f"{self.__nombre}, puede comer plantas, larvas, peces pequeños etc")

    def reproduccion(self):
        print("Los patos pueden tener entre 12 y 20 huevos cuando se reproducen")

    def pico(self):
        print(f"El color del pico de {self.__nombre} puede ser color naranja, amarillo, rosa o azul")

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

    @property
    def color(self):
        return self.__color
    @peso.setter
    def color(self,valor):
        self.__color=valor

    @property
    def sexo(self):
        return self.__sexo
    @peso.setter
    def sexo(self,valor):
        self.__sexo=valor
    
    def __str__(self):
        return f"Pato: \n Nombre: {self.__nombre}\n Edad: {self.__edad}\n Peso: {self.__peso}\n Color: {self.__color}\n Sexo: {self.__sexo}"

    



