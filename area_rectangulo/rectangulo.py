#Calcular area de un rectangulo.
def area_rectangulo():
    base = int(input("Ingrese la base: "))
    altura = int(input("Ingrese la altura: "))
    area = base * altura
    print(f"El área es: {area}")
    return area

area_rectangulo()