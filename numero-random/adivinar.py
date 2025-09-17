#Genera un numero entre 1 al 10, y el usuario debe adiv
import random
numeroSecreto = random.randint(1,10)
intentos = 0

while True:
    intento = int(input("Adivinar el numero: "))
    intentos = intentos + 1
    
    if intento == numeroSecreto:
        print(f"Correcto adivinaste el numero : {numeroSecreto}, en {intentos} intentos.")
        break
    if not (1 <= intento <= 10):
        print(f"Error, numero de rango invalido")
        continue