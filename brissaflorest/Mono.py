class Mono:
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
        return f"Mono | Nombre: {self.__nombre} | Edad: {self.__edad} | Tamaño: {self.__tamaño} | Peso: {self.__peso} | Altura: {self.__altura}."

    def comer(self):
        print("Los monos son omnívoros, es decir, que van a comer todo aquello que encuentren.")

    def aspecto(self):
        print("Los monos tienen un gran parecido a los humanos, tanto en forma de ser como en lo físico.")
    
    def trepar(self):
        print("Los monos cuentan con colas prensiles que utilizan para facilitar la atarea de trepar los árboles.")

    def jugar(self):
        print("Los monos lo consideran muy importante en sus vidas. Jugar les divierte y les hace disfrutar.")

    def dormir(self):
        print("Los monos duermen aproximadamente 9 o 10 horas y sus ciclos de sueño son de 80 minutos.")
