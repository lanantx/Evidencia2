class Lemur:
    def __init__(self, nombre, edad, sexo, peso, largo, pareja):
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = sexo
        self.__peso = peso
        self.__largo = largo
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
            print("La edad NO puede ser negativo")
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
    def largo(self):
        return self.__largo
    
    @largo.setter
    def largo(self, value):
        self.__largo = value
    
    @property
    def pareja(self):
        return self.__pareja
    
    @pareja.setter
    def pareja(self, value):
        self.__pareja = value