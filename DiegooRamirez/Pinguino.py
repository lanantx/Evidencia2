class Pinguino:
    def __init__(self, Nombre, Edad, Peso, Tamaño, Vuela_novuela):
        self.__Nombre=Nombre
        self.__Edad=Edad
        self.__Peso=Peso
        self.__Tamaño=Tamaño
        self.__Vuela_novuela=Vuela_novuela

    def vuelaNovuela(self):
        if self.__Vuela_novuela=="si":
            print("Lamento decirte que los pinguinos no vuelan, lo que tu observaste probablemente es un Frailecillo")
        elif self.__Vuela_novuela=="no":
            print("Se cree que los pinguinos perdieron la capacidad de volar para poder mejorar su eficacia de nado")

    def nadar(self):
        print("La velocidad media de los pinguinos en el agua suele rondar entre 4 y 10 kilómetros por hora pero hay tramos en los que pueden duplicar y triplicar su velocidad sacando el aire atrapado entre sus plumas en forma de burbujas")
    
    def saltar(self):
        print("A la hora de salir del agua pueden propulsarse con un salto hasta llegar a los 2 metros de altura")
    
    def comer(self):
        print("Los pingüinos y su dieta incluye pequeños crustáceos como krill, parecidos a las gambas, calamares y peces")

    def se_enamora (self):
        print("Los pingüinos son fieles a su pareja ya que sus relaciones son monógamas, permanecen siempre con la misma pareja durante toda la vida y sólo se reproducen con ella")

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
    @tamaño.setter
    def tamaño(self,valor):
        self.__Tamaño=valor

    @property
    def Vuela_novuela(self):
        return self.__Vuela_novuela
    @Vuela_novuela.setter
    def peso(self,valor):
        self.__Vuela_novuela=valor
