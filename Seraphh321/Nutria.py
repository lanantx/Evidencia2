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
            print(f"{self.__nombre} se mantiene despiert@ y activ@ durante las mañanas y empieza a descansar en los atardeceres")

      def pasatiempos(self):
            print(f"{self.__nombre} le gusta nadar en su habitad y disfruta de la compañia de los visitantes")

      def informacion(self):
            print(f"{self.__nombre} tiene garras que puede usar para agarre o defenderse")
            
      def recinto(self): 
            print("esta en un recinto en el cual es relajante estar ademas de que se la pasa bien estando ahi")
