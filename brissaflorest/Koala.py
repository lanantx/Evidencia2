class Koala:
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
        return f"Koala | Nombre: {self.__nombre} | Edad: {self.__edad} | Tamaño: {self.__tamaño} | Peso: {self.__peso} | Altura: {self.__altura}."

    def comer(self):
        print("Los koalas se alimentan de las hojas de eucalipto, no beben mucha agua, por lo que su hidratación proviene de las mismas hojas.")

    def aspecto(self):
        print("Los koalas se caracterizan por tener un cuerpo robusto y sin cola, con una cabeza considerablemente grande y con orejas peludas.")
    
    def olfato(self):
        print("Los koalas tienen como distintiva su nariz y esta les permite percibir y evaluar el peculiar alimento que consumen.")

    def significado(self):
        print("La palabra koala proviene del dharug, la lengua indígena de la zona de Sídney, y significa -no bebe-.")

    def dormir(self):
        print("Los koalas pueden dormir hasta 18 horas al día, sujetos en las ramas y rincones de los árboles.")
