class Serpiente:
   def __init__(self, nombre, edad, longitud, peso, especie):
        self._nombre = nombre
        self._edad = edad
        self._longitud = longitud
        self._peso = peso
        self._especie = especie

   @property
   def nombre(self):
       return self._nombre

   @nombre.setter
   def nombre(self, Value):
       Value = self._nombre

   @property
   def edad(self):
       return self._edad

   @edad.setter
   def edad(self, nueva_edad):
       self._edad = nueva_edad

   @property
   def longitud(self):
       return self._longitud

   @longitud.setter
   def longitud(self, nueva_longitud):
       self._longitud = nueva_longitud

   @property
   def peso(self):
       return self._peso

   @peso.setter
   def peso(self, nuevo_peso):
       self._peso = nuevo_peso
#aqui uso nueva_especie por que hay mas de una especia de serpientes
   @property
   def especie(self):
       return self._especie

   @especie.setter
   def especie(self, nueva_especie):
       self._epecie = nueva_especie

   def cambiar_de_piel(self):
        print(f"{self._nombre} está en el proceso de mudar la piel.")

   def cazar(self):
        print(f"{self._nombre} esta buscando presas para cazar.")

   def siseos(self):
        print(f"{self._nombre} está emitiendo siseos para comunicarse.")

   def enroscarse(self):
        print(f"{self._nombre} se esta enroscando para descansar o camuflarse.")

   def tomar_sol(self):
        print(f"{self._nombre} está tomando el sol para calentar el cuerpo.")

   