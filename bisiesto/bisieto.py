#Da si un año es Bisiesto o no.
def Bisieto():
    anio = 2025

    if(anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        print(f"Es un año Bisiesto")
    else:
        print(f"No es año Bisieto")

    return

Bisieto()