#Crea un archivo vacio.
def crear(nombre_archivo):
    with open(nombre_archivo, 'w'):
        pass

crear('hola_mundo.py')