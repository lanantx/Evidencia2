class Cebra:
    def __init__(self, nombre, edad, sexo, peso, longitud, especie, pareja):
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = sexo
        self.__peso = peso
        self.__longitud = longitud
        self.__especie = especie
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
        if value < 0:
            return "La edad NO puede ser negativo"
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
    def longitud(self):
        return self.__longitud
    
    @longitud.setter
    def longitud(self, value):
        self.__longitud = value
    
    @property
    def especie(self):
        return self.__especie
    
    @especie.setter
    def especie(self, value):
        self.__especie = value
    
    @property
    def pareja(self):
        return self.__pareja
    
    @pareja.setter
    def pareja(self, value):
        self.__pareja = value