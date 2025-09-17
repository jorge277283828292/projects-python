#Calcula el volumen de un cilindro.
import math

def volumenCilindro(radio, altura):
    return math.pi * radio ** 2 * altura

resultado = volumenCilindro(12, 9)
print(resultado)