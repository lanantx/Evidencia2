class Cebra:
    def __init__(self, nombre, edad, sexo, peso, longitud, especie, pareja):
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = sexo
        self.__peso = peso
        self.__longitud = longitud
        self.__especie = especie
        self.__pareja = pareja
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, value):
        self.__nombre = value
    
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, value):
        if value < 0:
            return "La edad NO puede ser negativo"
        self.__edad = value
    
    @property
    def sexo(self):
        return self.__sexo
    
    @sexo.setter
    def sexo(self, value):
        self.__sexo = value
    
    @property
    def peso(self):
        return self.__peso
    
    @peso.setter
    def peso(self, value):
        self.__peso = value
    
    @property
    def longitud(self):
        return self.__longitud
    
    @longitud.setter
    def longitud(self, value):
        self.__longitud = value
    
    @property
    def especie(self):
        return self.__especie
    
    @especie.setter
    def especie(self, value):
        self.__especie = value
    
    @property
    def pareja(self):
        return self.__pareja
    
    @pareja.setter
    def pareja(self, value):
        self.__pareja = value
    
    # Metodos: comer, color, longitud_media, peso_medio, esperanza_vida, correr
    def info_cebra(self):
        # nombre, edad, sexo, peso, longitud, especie, pareja
        print(f"Nombre cebra: {self.__nombre}\nEdad{self.__edad}\nSexo: {self.__sexo}\nPeso: {self.__peso}\nLongitud: {self.__longitud}\nEspecie: {self.__especie}\n Pareja: {self.__pareja}")
    
    def comer(self):
        print(f"Son herbivoros. Se alimentan de hierba tosca, hojas, brotes, corteza y ramas.")
    
    def color(self):
        print("Las cebras son de color blanco con rayas negras; dependiendo la especie cambia la direccion de las rayas.")
    
    def longitud_media(self):
        print("Las cebras tienen una longitud promedio de 2.3 m y de altura 1.5 m promedio.")
    
    def peso_medio(self):
        print("El peso medio de las cebras es aproximadamente 300 kg, pero pueden llegar a pesar hasta 450 kg.")
    
    def esperanza_vida(self):
        print("Las cebras llegan a vivir 30 años; y en cautivero pueden vivir hasta 40 años.")
    
    def correr(self):
        print("Las cebras pueden alcanzar una velocidad de 55 km/h a galope.")