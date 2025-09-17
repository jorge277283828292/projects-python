#Juego de Piedra, Papel o Tijera. Que a las 3 victorias sale el ganador.
import random

elecciones = ["piedra", "papel", "tijera"]
victorias_usuario = 0
victorias_computadora = 0

def determinar_ganador(usuario, computadora):
    if usuario == computadora:
        return "Empate"
    elif (usuario == "piedra" and computadora == "tijera") or \
         (usuario == "papel" and computadora == "piedra") or \
         (usuario == "tijera" and computadora == "papel"):
        return "Ganaste"
    else:
        return "Perdiste"
    
while True:
    print("="*50)
    print(f"Juego de Piedra, Papel o Tijera contra la computadora")
    print(f"¡El que gane 3 veces se lleva la victoria!")
    usuario = input("Elije tu jugada [Piedra] [Papel] [Tijera]: ").lower()
    print("="*50)
    print()

    if usuario not in elecciones:
        print("Eleccion invalida, no se puede usar esa jugada.")
    else:
        computadora = random.choice(elecciones)
        print(f"La computadora eligio: {computadora}")
        resultado = determinar_ganador(usuario, computadora)

        if resultado == "Ganaste":
            victorias_usuario += 1
            print(f"{resultado}, ¡haz ganado! |Marcador Computadora: {victorias_computadora}, Usuario: {victorias_usuario}|")
            print()
        else:
            victorias_computadora += 1
            print(f"{resultado} ¡Intentalo denuevo la computadora a ganado! |Marcador Computadora: {victorias_computadora}, Usuario: {victorias_usuario}|")
            print()
            print("-"*100)

        if victorias_computadora == 3:
            print("¡La computadora se a llevado la victoria mejor suerte para la proxima! ")
            print(f"Marcador final: |Computadora: {victorias_computadora}, Usuario: {victorias_usuario}|")
            break

        if victorias_usuario ==3:
            print("¡La vitoria es tuya!")
            print(f"Marcador final: |Computadora: {victorias_computadora}, Usuario: {victorias_usuario}|")
            break
pregun



        