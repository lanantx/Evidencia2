class Capybara:
    def __init__(self,Nombre,Peso,Edad,Tamaño,ComidaFav):
        self.__Nombre = Nombre
        self.__Peso = Peso
        self.__Edad = Edad
        self.__Tamaño = Tamaño
        self.__ComidaFav = ComidaFav
        
   
    

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

    
    