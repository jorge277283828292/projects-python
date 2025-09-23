import json
import random as r

errores = 0
    
with open("juego-ahorcado/personaje.json", "r") as f:
    personaje = json.load(f)
    
with open("juego-ahorcado/palabras.json", "r") as f:
    palabras = json.load(f)["palabras"]

palabra = r.choice(palabras).upper()
progreso = ["_"] * len(palabra)

for l in progreso:
    print(f"{l}", end="")
print(" ")

while True:
    letra = str(input("Adivina una letra de la palabra: "))
    for i, l in enumerate(palabra):
        if l == letra:
            progreso[i] = letra
    print(" ".join(progreso))

    if errores == 5:
        print("Fin dle juego")
        break
    
    if letra not in palabra:
        errores += 1 
        print(personaje["stages"][errores]) 
        continue
    
    if "_" not in progreso:
        print("¡Felicidades! Adivinaste la palabra:", palabra)
        break
