class Capybara:
    def __init__(self,Nombre,Peso,Edad,Tamaño,ComidaFav):
        self.__Nombre = Nombre
        self.__Peso = Peso
        self.__Edad = Edad
        self.__Tamaño = Tamaño
        self.__ComidaFav = ComidaFav
        self.__Especie = "Capybara"
        
    @property
    def Especie(self):
        return self.__Especie
    @Especie.setter
    def Especie(self,value):
        self.__Especie = value

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
        print(f"*{self.__Nombre} Come {self.__ComidaFav}")
        
    def NombreCientifico(self):
        print("Hydrochoerus hydrochaeris")

    def MostrarNombre(self):
        print(self.__Nombre)
    
    def HacerTruco(self):
        print("Hacerse el Muerto")
    
    def Dormir(self):
        print(f"*{self.__Nombre}Se duerme*")

    def info(self):
        print(f"Nombre: {self.__Nombre}")
        print(f"Peso: {self.__Peso}")
        print(f"Edad: {self.__Edad}")
        print(f"Tamaño {self.__Tamaño}")
        print(f"Comida Favorita: {self.__ComidaFav}")
        print(f"Especie{self.__Especie}")
    