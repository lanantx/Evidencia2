class Oso:
    def __init__(self, nombre, edad, sexo, peso, altura, pareja):
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = sexo
        self.__peso = peso
        self.__altura = altura
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
            print("La edad tiene que ser un numero positivo")
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
    def altura(self):
        return self.__altura
    
    @altura.setter
    def altura(self, value):
        self.__altura = value
    
    @property
    def pareja(self):
        return self.__pareja
    
    @pareja.setter
    def pareja(self, value):
        self.__pareja = value
    
    # Metodos: comer, color, altura_media, peso_medio, esperanza_vida
    def info_oso(self):
        # nombre, edad, sexo, peso, altura, pareja
        print(f"Nombre oso: {self.__nombre}\nEdad{self.__edad}\nSexo: {self.__sexo}\nPeso: {self.__peso}\nAltura: {self.__altura}\nPareja: {self.__pareja}")
    
    def comer(self):
        print(f"Comen cualquier cosa, desde hojas, raices, bayas y hasta insectos, carroña, carne fresca y pescado.")
    
    def color(self):
        print("Suelen ser de color cafe marron.")
    
    def altura_media(self):
        print("Miden entre 1 m y 2.8 m en promedio.")
    
    def peso_medio(self):
        print("Pueden pesar entre 27 y 780 kg en promedio, pero pueden llegar a pesar hasta 1 tonelada.")
    
    def esperanza_vida(self):
        print("Los osos tienen una esperanza de vida aproximadamente de 20 años")