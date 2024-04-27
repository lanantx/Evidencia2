class Burro:
    def __init__(self, nombre, sexo, edad, peso, altura):
        self.__nombre = nombre
        self.__sexo = sexo
        self.__edad = edad
        self.__peso = peso
        self.__altura = altura

    @property 
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, value):
        self.__nombre = value
    
    @property 
    def sexo(self):
        return self.__sexo
    
    @sexo.setter
    def sexo(self, value):
        self.__sexo = value
    
    @property 
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, value):
        self.__edad = value

    @property 
    def peso(self):
        return self.__peso
    
    @peso.setter
    def peso(self, value):
        self.__peso = value
    
    @property 
    def altura(self):
        return self.__altura
    
    @altura.setter
    def altura(self, value):
        self.__altura = value

    def alimentar(self):
        print(f"Se está alimentando a {self.__nombre}.")

    def limpieza(self):
        print(f"Se está bañando a {self.__nombre}.")

    def pesar(self):
        print(f"Se pesó a {self.nombre}, y su peso es de {self.__peso}.")

    def paseo(self):
        print(f"Se sacó a pasear a {self.__nombre} por el zoológico.")

    def medicamento(self):
        print(f"Se está administrando medicina a {self.__nombre}.")

    def __str__(self):
        return f"Burro | Nombre: {self.__nombre} | Sexo: {self.__sexo} | Edad: {self.__edad} | Peso: {self.__peso} | Altura: {self.__altura}."