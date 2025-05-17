#Da el area de un circulo.
import math

def area_circulo():
    radio = float(input("Ingrese el radio del círculo: "))
    area = math.pi * radio ** 2
    print(f"El área del círculo es: {area}")
    return area

area_circulo()