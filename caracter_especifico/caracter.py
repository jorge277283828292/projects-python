#Da la cantidad de veces que se repite un caracter en especifico en un String.
def Ocurrencias():
    cadena = "progrmacion orientada a objetos"
    ocurrencia = cadena.count('a')

    print(f"Ocurrencias {ocurrencia}")

    return ocurrencia

Ocurrencias()