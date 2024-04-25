class Camaleon:
    def __init__(self, Nombre, Edad, Peso, Tamaño, Color):
        self.__Nombre=Nombre
        self.__Edad=Edad
        self.__Peso=Peso
        self.__Tamaño=Tamaño
        self.__Color=Color

    def comer(self):
        print("La lengua de los camaleones pueden llegar a medir el doble que su cuerpo, siendo capaces de capturar a una presa en menos de un segundo.")
    
    def observar(self):
        print("Los ojos de los camaleones giran de manera independiente en un ángulo de 180 grados, lo que les permite aumentar su campo de visión hasta en 360 grados")
    
    def longitud(self):
        print(f"Los camañeones mas pequeños llegan a medir 26 milimetro y los mas grande 70 centimetros, en este caso el camaleon mide: {self.__Tamaño}")

    def color(self):
        print(f"Los camaleones usan un fibras de melanina para cambiar de color, ahora el color es: {self.__Color}")
    
    def trepar(self):
        print("Los camaleones pueden moverse por los árboles con gran facilidad, ya que sus pies tienen forma de pinza")

    @property
    def nombre(self):
        return self.__Nombre
    @nombre.setter
    def nombre(self,valor):
        self.__Nombre=valor
    
    @property
    def edad(self):
        return self.__Edad
    @edad.setter
    def edad(self, valor):
        self.__Edad=valor

    @property
    def peso(self):
        return self.__Peso
    @peso.setter
    def peso(self,valor):
        self.__Peso=valor

    @property
    def tamaño(self):
        return self.__Tamaño
    @peso.setter
    def peso(self,valor):
        self.__Tamaño=valor

    @property
    def color(self):
        return self.__Color
    @peso.setter
    def peso(self,valor):
        self.__Color=valor