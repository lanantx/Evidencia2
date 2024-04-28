class gorilla:
      def __init__(self, nombre, edad, peso, sexo, tamaño):
          self.nombre = nombre
          self.edad = edad
          self.peso = peso
          self.sexo = sexo
          self.tamaño = tamaño
      def comida(self):
            print(" puede comer hasta 30kg de plantas ya que es muy grande")
      
      def horario(self):
            print(" se mantiene despierto y activo durante las mañanas y empieza a descansar en los atardeceres")

      def comportamiento(self):
            print(" no es agresivo, usalmente se mantiene sereno pero se llega a estresar cuando hay demasiada gente hablando")

      def masa_muscular(self):
            print(" esta lleno de musculos por lo tanto tiene demasiada fuerza")
            
      def recinto(self): 
            print("al tener tanta fuerza, su recinto es un poco... especial")
            
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
            


            
      