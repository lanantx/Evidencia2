class Cocodrilo:
    def __init__(self,Nombre,Peso,Edad,Tamaño,ComidaFav):
        self.__Nombre = Nombre
        self.__Peso = Peso
        self.__Edad = Edad
        self.__Tamaño = Tamaño
        self.__ComidaFav = ComidaFav
        
   

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