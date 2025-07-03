class Persona:
    def __init__(self, nombre, edad, altura, contrasena):
        self.nombre = nombre 
        self.edad = edad
        self.altura = altura
        self.__contrasena = contrasena

    def saludar(self):
        print(f"Hola, soy {self.nombre}")

class Etnia(Persona):
    def __init__(self, nombre, edad, altura, contrasena, etnia):
        super().__init__(nombre, edad, altura, contrasena)

        self.etnia = etnia

    def decirEtnia(self):
        print(f"La etnia de {self.nombre} es: {self.etnia}")


abner = Etnia("Abner", 22, 1.75, "1234", "Gringo")

print(abner.etnia)
