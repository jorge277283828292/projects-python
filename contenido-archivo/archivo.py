#Crea un documento .txt, de acuerdo a la informacion ingresada por el usuario y luego abre el editor de texto.
from crear_leer_archivo import Archivo
import os 

file = Archivo()
file.set_nombre_archivo('archivo.txt')
contenido = input("Ingrese el texto que quiere que haya en el documento: ")
file.set_contenido(contenido)
file.crear_archivo()
file.escribir()
os.startfile('archivo.txt')