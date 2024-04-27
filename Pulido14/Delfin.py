class Delfin:
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

   @property
   def especie(self):
       return self._especies

   @especie.setter
   def especie(self, nueva_especie):
       self._epecie = nueva_especie

   def comer(self):
        print(f"{self._nombre} está comiendo pescado fresco.")

   def nadar(self):
        print(f"{self._nombre} está nadando en el océano.")

   def alimentarse(self):
        print(f"{self._nombre} está alimentándose de peces pequeños.")

   def emitir_sonido(self):
        print(f"{self._nombre} está emitiendo sonidos de clics y silbidos.")

   def socializar(self):
        print(f"{self._nombre} está jugando con otros delfines.")

   def dormir(self):
        print(f"{self._nombre} está descansando en el agua.")
