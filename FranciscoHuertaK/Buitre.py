class Buitre:
    def __init__(self,nombre,edad,sexo,altura,peso):
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = sexo
        self.__altura = altura
        self.__peso = peso

    def alimentacion(self):
        print("Los buitres se alimentan de carroña.")

    def caracteristicas(self):
        print("Una de las caracteristicas de los buitres es que no tienen plumas en la cabeza.")

    def conservacion(self):
        print("Alrededor de la mitad de especies estan en peligro de extincion.")

    def distribucion(self):
        print("Los buitres se hallan en Europa, Africa, Asia y America")

    def curiosidad(self):
        print("Los buitres del viejo y nuevo mundo no estan tan emparentados y su parentezco es resultado de evolucion convergente.")

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,value):
        self.__nombre = value

    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self,value):
        self.__edad = value

    @property
    def sexo(self):
        return self.__sexo
    
    @sexo.setter
    def sexo(self,value):
        self.__sexo = value

    @property
    def altura(self):
        return self.__altura
    
    @altura.setter
    def altura(self,value):
        self.__altura = value

    @property
    def peso(self):
        return self.__peso
    
    @peso.setter
    def peso(self,value):
        self.__peso = value

        