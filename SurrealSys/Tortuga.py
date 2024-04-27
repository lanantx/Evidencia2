class Tortuga:
    def __init__(self, nombre, edad, sexo, peso, sonido):
        self._nombre = nombre
        self._edad = edad
        self._sexo = sexo
        self._peso = peso
        self._sonido = sonido

    # atributos: comer, Dormir, hacer_sonido, defecar

    def comer(self,comida):
        return f"{self._nombre} está comiendo {comida}."

    def dormir(self):
        return f"{self._nombre} está durmiendo zZzZz."

    def hacer_sonido(self):
            return f"{self._nombre} dice: {self._sonido}"
    
    def reproducirse(self):
        return f"{self._nombre} esta reproduciendose con el sexo opuesto"
    
    def defecar(self): 
        return f"{self._nombre} esta defecando" 

## Getters & Setters (nombre,edad,sexo,peso,sonido)

    # nombre
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    # edad
    def get_edad(self):
        return self._edad

    def set_edad(self, nueva_edad):
        if nueva_edad >= 0:
            self._edad = nueva_edad
        else:
            print("La edad no puede ser un número negativo.")

    # sexo
    def get_sexo(self):
        return self._sexo

    def set_sexo(self, nuevo_sexo):
        self._sexo = nuevo_sexo

    # peso
    def get_peso(self):
        return self._peso

    def set_peso(self, nuevo_peso):
        if nuevo_peso >= 0:
            self._peso = nuevo_peso
        else:
            print("El peso no puede ser un número negativo.")

    # sonido
    def get_sonido(self):
        return self._sonido

    def set_sonido(self, nuevo_sonido):
        self._sonido = nuevo_sonido


    def __str__(self):
        return f"Nombre: {self._nombre}, Edad: {self._edad}, Sexo: {self._sexo}, Peso: {self._peso}kg, Sonido: {self._sonido}"


