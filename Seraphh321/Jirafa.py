class jirafa:
    def __init__(self, nombre, edad, peso, sexo, tamaño):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.sexo = sexo
        self.tamaño = tamaño
        
    def comida(self):
            print( "come hiervas ademas de comer increiblemente 34kg de estas mismas!")
      
    def cuello(self):
            print( "su cuello es excepcionalmente grande alcanzando los soprendentes 3 metros y medio")

    def horario(self):
            print( "se mantiene activ@ durante el dia y descansa por las noches")

    def habitat(self):
            print(" esta comod@ en su habitat y no parece molestarle algo")
            
    def comportamiento(self): 
            print("su comportamiento es sereno y generalmente solo come")
           
     
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
    def peso(self): 
        return self.__peso
    @peso.setter
    def peso(self,valor):
            self.__peso = valor

    @property 
    def sexo(self):
            return self.__sexo
    @sexo.setter
    def sexo(self,valor):
            self.__sexo = valor
            
    @property 
    def tamaño(self):
            return self.__tamaño
    @tamaño.setter
    def tamaño(self,valor):
            self.__tamaño=valor


