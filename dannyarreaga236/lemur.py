class Lemur:
    def __init__(self, nombre, edad, sexo, peso, largo, pareja):
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = sexo
        self.__peso = peso
        self.__largo = largo
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
        if value <0:
            print("La edad NO puede ser negativo")
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
    def largo(self):
        return self.__largo
    
    @largo.setter
    def largo(self, value):
        self.__largo = value
    
    @property
    def pareja(self):
        return self.__pareja
    
    @pareja.setter
    def pareja(self, value):
        self.__pareja = value
    
    # Metodos: comer, color, longitud_media, peso_medio, esperanza_vida, correr
    def info_lemur(self):
        # nombre, edad, sexo, peso, longitud, especie, pareja
        print(f"Nombre lemur: {self.__nombre}\nEdad{self.__edad}\nSexo: {self.__sexo}\nPeso: {self.__peso}\nLargo: {self.__largo}\nPareja: {self.__pareja}")
    
    def comer(self):
        print(f"Se alimentan de frutas y hojas, principalmente de tamarindo.")
    
    def color(self):
        print("Son de color gris claro y una cola caracteristica de anillos negros y gris claro.")
    
    def largo_medio(self):
        print("Miden entre 95 y 110 cm en promedio.")
    
    def peso_medio(self):
        print("Los lemures tienen un peso promedio de 2.2 kg.")
    
    def esperanza_vida(self):
        print("Los lemures tienen una esperanza de vida entre 16 a 19 años")