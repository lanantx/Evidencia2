class canguro:
    def __init__(self, nombre,edad,peso, color, sexo):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.color = color
        self.sexo = sexo

    def sonido(self):
        print("BOING BOING")

    def socializar(self):
        print(f"{self.__nombre}, puede que sea muy sociable ya que siempre anda en grupo")

    def comida(self):
        print(f"{self.__nombre}, es herbivoro asi que puede comer hierbas, flores, hojas hasta insectos")

    def hidratacion(self):
        print(f"Si estas preocupado porque {self.__nombre} no a tomado agua, no te preocupes los de su especie pueden sobrevivir sin tomar agua durante semanas")

    def tamaño (self):
        print("Los canguros son los marsupiales mas grandes del mundo")

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

    