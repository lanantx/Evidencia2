class Nutria:
      def __init__(self, nombre, edad, peso, sexo, tamaño):
          self.nombre = nombre
          self.edad = edad
          self.peso = peso
          self.sexo = sexo
          self.tamaño = tamaño
            
      def comida(self):
            print("las nutrias son herbivoras")
      
      def horario(self):
            print(" se mantiene despiert@ y activ@ durante las mañanas y empieza a descansar en los atardeceres")

      def pasatiempos(self):
            print(" le gusta nadar en su habitad y disfruta de la compañia de los visitantes")

      def informacion(self):
            print(" tiene garras que puede usar para agarre o defenderse")
            
      def recinto(self): 
            print("esta en un recinto en el cual es relajante estar ademas de que se la pasa bien estando ahi")
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
            
     
