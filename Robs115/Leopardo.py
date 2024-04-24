class Leopardo:
    def __init__(self,Nombre,Peso,Edad,Tamaño,ComidaFav):
        self.__Nombre = Nombre
        self.__Peso = Peso
        self.__Edad = Edad
        self.__Tamaño = Tamaño
        self.__ComidaFav = ComidaFav
        
   
    

    def Comer(self):
        print(f"*{self.__Nombre} Come Pedazo de carne*")
        
    def NombreCientifico(self):
        print("Panthera pardus ")

    def MostrarNombre(self):
        print(self.__Nombre)
    
    def HacerTruco(self):
        print("Rueda en el suelo")
    
    def Rugir(self):
        print(f"*{self.__Nombre} Ruge*")

    