class TUCAN:
    def __init__(self, nombre, color_plumas, longitud_pico, largo_alas, velocidad_vuelo):
        self.nombre= nombre
        self.color_plumas= color_plumas
        self.longitud_pico= longitud_pico
        self.largo_alas= largo_alas
        self.velocidad_vuelo= velocidad_vuelo

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
    
    @property
    def color_plumas(self):
        return self._color_plumas
    
    @color_plumas.setter
    def color_plumas(self, nuevo_color):
        self._color_plumas = nuevo_color
    
    @property
    def longitud_pico(self):
        return self._longitud_pico
    
    @longitud_pico.setter
    def longitud_pico(self, nueva_longitud):
        self._longitud_pico = nueva_longitud
    
    @property
    def largo_alas(self):
        return self._largo_alas
    
    @largo_alas.setter
    def largo_alas(self, nuevo_largo):
        self._largo_alas = nuevo_largo
    
    @property
    def velocidad_vuelo(self):
        return self._velocidad_vuelo
    
    @velocidad_vuelo.setter
    def velocidad_vuelo(self, nueva_velocidad):
        self._velocidad_vuelo = nueva_velocidad

    def comert(self):
        print(f"{self.nombre} esta comiendo semillas de la mano del cuidador.")
    
    def volart(self):
        print(f"{self.nombre} esta volando, el largo de sus alas es de {self.largo_alas}.")

    def jugart(self):
        print(f"{self.nombre} esta jugando en los arboles, ¡que bonito se ve con su color {self.color_plumas}.!")
    
    def rascar(self):
        print(f"{self.nombre} tiene un pico de {self.longitud_pico} de largo con el que se rasca muy seguido.")

    def dormirt(self):
        print(f"{self.nombre} esta durmiendo.")