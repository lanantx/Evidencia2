class Delfin:
   def __init__(self, nombre, edad, longitud, peso, especie):
        self._nombre = nombre
        self._edad = edad
        self._longitud = longitud
        self._peso = peso
        self._especie = especie

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

   @property
   def nombre(self):
       return self._nombre

   @nombre.setter
   def nombre(self, Value):
       self._nombre = Value

   @property
   def edad(self):
       return self._edad

   @edad.setter
   def edad(self, Value):
       self._edad = Value

   @property
   def longitud(self):
       return self._longitud

   @longitud.setter
   def longitud(self, Value):
       self._longitud = Value

   @property
   def peso(self):
       return self._peso

   @peso.setter
   def peso(self, Value):
       self._peso = Value

   @property
   def especie(self):
       return self._especie

   @especie.setter
   def especie(self, Value):
       self._especie = Value

   def __str__(self):
        return f"Informacion de la Delfin: Nombre:{self.nombre}, Edad:{self.edad}, Longitud:{self.longitud}, Peso:{self.peso}, Especie:{self.especie}."
