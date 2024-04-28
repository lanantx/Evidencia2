class Hipopotamo:
    def __init__(self,nombre,edad,tamaño,peso,altura):
        self.__nombre = nombre
        self.__edad = edad
        self.__tamaño = tamaño
        self.__peso = peso
        self.__altura = altura

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,valor):
        self.__nombre = valor   
    
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self,valor):
        self.__edad = valor   

    @property
    def tamaño(self):
        return self.__tamaño
    
    @tamaño.setter
    def tamaño(self,valor):
        self.__tamaño = valor   

    @property
    def peso(self):
        return self.__peso
    
    @peso.setter
    def peso(self,valor):
        self.__peso = valor

    @property
    def altura(self):
        return self.__altura
    
    @altura.setter
    def altura(self,valor):
        self.__altura = valor
    
    def __str__(self):
        return f"Hipopotamo | Nombre: {self.__nombre} | Edad: {self.__edad} | Tamaño: {self.__tamaño} | Peso: {self.__peso} | Altura: {self.__altura}."

    def comer(self):
        print("Los hipopotamos comen pasto corto. Pasan cinco o más horas de pastoreo cada noche.")

    def aspecto(self):
        print("Los hipopotamos tienen torsos redondos y cuerpos de color marrón rosáceo, con piel impermeable de cinco centímetros de grosor y patas cortas y robustas.")
    
    def velocidad(self):
        print("Los hipopotamos pueden alcanzar velocidades de hasta 35 kilómetros por hora en tierra en distancias cortas.")

    def correr(self):
        print("Los hipopótamos no saben nadar ni respirar bajo el agua, en su lugar, caminan o corren por el fondo del cauce.")

    def dormir(self):
        print("Los hipopotamos suelen dormir la siesta en el agua durante el día.")


