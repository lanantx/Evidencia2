class Ballena:
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
#aqui uso nueva_especie por que hay mas de una especia de ballenas
   @property
   def especie(self):
       return self._especies

   @especie.setter
   def especie(self, nueva_especie):
       self._epecie = nueva_especie

   def nadar(self):
        print(f"{self._nombre} está nadando.")

   def alimentarse(self):
        print(f"{self._nombre} está alimentándose de plancton.")

   def emitir_sonido(self):
        print(f"{self._nombre} está emitiendo sonidos de baja frecuencia.")

   def socializar(self):
        print(f"{self._nombre} está interactuando con otras ballenas.")

   def dormir(self):
        print(f"{self._nombre} está durmiendo en el océano.")