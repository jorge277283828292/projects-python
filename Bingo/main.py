from carton_usuario import carton_bingo_usuario
import random

# Lista para llevar control de números ya usados
numeros_usados = []

# Función que genera un número aleatorio único
def numero_aleatorio(usados):
    while True:
        numero = random.randint(1, 50)
        if numero not in usados:
            usados.append(numero)
            print(f"\n🎲 Número generado: {numero}")
            return numero

# Función para marcar el número en el cartón si el usuario lo tiene
def marcar_numero_en_carton(matriz, numero, input_usuario):
    encontrado = False
    for i in range(5):
        for j in range(5):
            if matriz[i][j] == numero:
                encontrado = True
                if input_usuario.upper() == "X":
                    matriz[i][j] = "X"
    if input_usuario.upper() == "X" and not encontrado:
        print("🚫 Ese número no está en tu cartón.")

# Función para verificar si el cartón está completo
def carton_completo(matriz):
    for fila in matriz:
        for elemento in fila:
            if elemento != "X":
                return False
    return True

# Obtener el cartón del usuario
carton_usuario = carton_bingo_usuario()

# Juego principal
while not carton_completo(carton_usuario):
    print("\n📋 Cartón Usuario:")
    for fila in carton_usuario:
        print(" | ".join(f"{e:2}" for e in fila))

    numero = numero_aleatorio(numeros_usados)
    
    respuesta = input("¿Tenés ese número en tu cartón? (X / NO): ")
    while respuesta.upper() not in ["X", "NO"]:
        respuesta = input("Por favor escribí 'X' o 'NO': ")

    marcar_numero_en_carton(carton_usuario, numero, respuesta)

# Al salir del bucle, el cartón está completo
print("\n🏆 ¡Cartón completo! ¡GANASTE!")
for fila in carton_usuario:
    print(" | ".join(f"{e:2}" for e in fila))
