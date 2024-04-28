class PUMA:
    def __init__(self, nombre, color, edad, peso, velocidad_max ):
        self.nombre = nombre
        self.color = color
        self.edad = edad
        self.peso = peso
        self.velocidad_max = velocidad_max
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
    
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, nuevo_color):
        self._color = nuevo_color
    
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, nueva_edad):
        self._edad = nueva_edad
    
    @property
    def peso(self):
        return self._peso
    
    @peso.setter
    def peso(self, nuevo_peso):
        self._peso = nuevo_peso
    
    @property
    def velocidad_max(self):
        return self._velocidad_max
    
    @velocidad_max.setter
    def velocidad_max(self, nueva_velocidad_max):
        self._velocidad_max = nueva_velocidad_max
        
    def comerP(self):
        print(f"{self.nombre} esta comiendo")
    
    def dormirP(self):
        print(f"{self.nombre} esta durmiendo ¡que tierno se ve su color {self.color}!")

    def correrP(self):
        print(f"{self.nombre} esta corriendo, su maximo de velocidad es de {self.velocidad_max}")
    
    def rugirP(self):
        print(f"{self.nombre} esta rugiendo muy fuerte, se nota imponente.")
    
    def jugarP(self):
        print(f"{self.nombre} esta jugando en un árbol.")
        