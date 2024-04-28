class Aguila:
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
            self.__altura = altura

    
    def __str__(self):
        return (f"Aguila: \n Nombre: {self.__nombre}\n Sexo: {self.__sexo}\n Edad: {self.__edad}\n Peso: {self.__peso}\n Altura: {self.__altura}")