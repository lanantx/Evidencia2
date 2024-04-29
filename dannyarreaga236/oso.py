class Oso:
    def __init__(self, nombre, edad, sexo, peso, altura, pareja):
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = sexo
        self.__peso = peso
        self.__altura = altura
        self.__pareja = pareja
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, value):
        self.__nombre = value
    
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, value):
        if value <0:
            print("La edad tiene que ser un numero positivo")
        self.__edad = value
    
    @property
    def sexo(self):
        return self.__sexo
    
    @sexo.setter
    def sexo(self, value):
        self.__sexo = value
    
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
    
    @property
    def pareja(self):
        return self.__pareja
    
    @pareja.setter
    def pareja(self, value):
        self.__pareja = value