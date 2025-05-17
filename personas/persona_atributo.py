class Persona:

    def __init__(self, nombre=None, edad=None):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, nueva_edad):
        self._edad = nueva_edad

    def mostrar(self):
        print(self.__dict__)

    def mayor_edad(self):
        if self._edad >=18:
            return True
        else:
            return False