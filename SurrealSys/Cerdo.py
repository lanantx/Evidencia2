class Cerdo:
   def __init__(self, nombre, edad, color, peso, sonido):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.peso = peso
        self.sonido = sonido

    # atributos: comer, Dormir, hacer_sonido, defecar

    def comer(self,comida):
        return f"{self.nombre} está comiendo {comida}."

    def dormir(self):
        return f"{self.nombre} está durmiendo zZzZz."

    def hacer_sonido(self):
            return f"{self.nombre} dice: {self.sonido}"
    
    def reproducirse(self): #Agregar mas cosas para que esto pueda realizarse
        return f"{self.nombre} esta reproduciendose con el sexo opuesto"
    
    def defecar(self): # Agregar como requerimiento haber comido y que comio idk
        return f"{self.nombre} esta defecando" 








