class Cocodrilo:
    def __init__(self,Nombre,Peso,Edad,Tamaño,ComidaFav):
        self.__Nombre = Nombre
        self.__Peso = Peso
        self.__Edad = Edad
        self.__Tamaño = Tamaño
        self.__ComidaFav = ComidaFav
        
    @property
    def ComidaFav (self):
        return self.__ComidaFav
    @ComidaFav.getter
    def ComidaFav (self,Value):
        Value = self.__ComidaFav
    
    @property
    def Nombre (self):
        return self.__Nombre
    @Nombre.getter
    def Nombre (self,Value):
        Value = self.__Nombre
    
    @property
    def Edad (self):
        return self.__Edad
    @Edad.getter
    def ComidaFav (self,Value):
        Value = self.__Edad
    
    @property
    def Peso (self):
        return self.__Peso
    @Peso.getter
    def Peso (self,Value):
        Value = self.__Peso
    
    @property
    def Tamaño (self):
        return self.__Tamaño
    @Tamaño.getter
    def ComidaFav (self,Value):
        Value = self.__Tamaño

    def Comer(self):
        print(f"*{self.__Nombre} Come un pescado*")
        
    def NombreCientifico(self):
        print("Crocodylidae")

    def MostrarNombre(self):
        print(self.__Nombre)
    
    def HacerTruco(self):
        print("Salta al agua")
    
    def Chapotear(self):
        print(f"*{self.__Nombre} Chapotea en el agua*")