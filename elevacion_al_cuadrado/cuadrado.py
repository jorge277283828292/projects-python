#Elevacion al cuadrado una lista de numeros utlizando map().
def cuadrado(x):
    return x ** 2

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cuadrados = list(map(cuadrado, numeros))

print(numeros)
print(cuadrados)