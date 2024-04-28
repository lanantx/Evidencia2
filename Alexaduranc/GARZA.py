class GARZA:
    def __init__(self, nombre, color, edad, peso, longitud_de_patas):
        self.nombre = nombre
        self.color = color
        self.edad= edad
        self.peso= peso
        self.longitud_de_patas= longitud_de_patas
    
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
    def longitud_de_patas(self):
        return self._longitud_de_patas
    
    @longitud_de_patas.setter
    def longitud_de_patas(self, nueva_longitud):
        self._longitud_de_patas = nueva_longitud

    def volarG(self):
        print(f"{self.nombre} esta volando a todas direcciones.")
    
    def pescarG(self):
        print(f"{self.nombre} esta pescando en el agua con sus patas de {self.longitud_de_patas} cm.")
    
    def comerG(self):
        print(f"{self.nombre} esta comiendo un pescado que pudo cazar.")

    def dormirG(self):
        print(f"{self.nombre} esta durmiendo.")
    
    def aletearG(self):
        print(f"{self.nombre} esta moviendo sus alas que son de color {self.color}.")

