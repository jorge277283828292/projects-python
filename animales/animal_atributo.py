class Animal:

    def __init__(self, especie, nombre):
        self.especie = especie
        self.nombre = nombre 

    def hablar(self):
        if self.especie == "perro":
            print(f"Guau")
        elif self.especie == "gato":
            print("Miau")
        else:
            print("Aniaml no valido")
