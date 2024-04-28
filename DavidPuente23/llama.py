class llama:
    def __init__(self, nombre,edad,peso,color,sexo):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.color = color
        self.sexo = sexo

    def sonido(self):
        print("TE ESCUPE")

    def intelectual(self):
        print(f"{self.__nombre}, es demasiado inteligente al igual que todos los de su especie")

    def velocidad(self):
        print(f"{self.__nombre}, puede correr hasta 40 millas por hora eso les ayuda a escapar de sus presas")

    def tamaño(self):
        print("Si es hembra de estatura sera mas pequeña ya que los machos son mas altos")

    def piel(self):
        print("Su piel gruesa ayuda a que se mantengan calientes y tambien les ayuda a protegerser de las mordeduras de otros animales")

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
        return f"Llama: \n Nombre: {self.__nombre}\n Edad: {self.__edad}\n Peso: {self.__peso}\n Color: {self.__color}\n Sexo: {self.__sexo}"
