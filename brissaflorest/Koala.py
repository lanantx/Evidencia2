class koala:
    def __init__(self,nombre,edad,tamaño,peso):
        self.__nombre = nombre
        self.__edad = edad
        self.__tamaño = tamaño
        self.__peso = peso

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,valor):
        self.__nombre = valor   
    
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self,valor):
        self.__edad = valor   

    @property
    def tamaño(self):
        return self.__tamaño
    
    @tamaño.setter
    def tamaño(self,valor):
        self.__tamaño = valor   

    @property
    def peso(self):
        return self.__peso
    
    @peso.setter
    def peso(self,valor):
        self.__peso = valor
