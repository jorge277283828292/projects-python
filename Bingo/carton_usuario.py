import random

def carton_bingo_usuario():
    matriz = []

    for _ in range(5):
        fila = []
        for _ in range(5):
            numero = random.randint(1, 50)
            fila.append(numero)
        matriz.append(fila)

    return matriz
