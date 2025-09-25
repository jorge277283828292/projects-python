import random as r
import time as t
#Los dados en cada ronda se suman el que la suma de los dados 
#sea mayor se le suman +3 y el que pierda +1, el que llegue a 10 puntos gana

puntosMaquina = 0
puntosUsuario = 0

while True: 
    dadoMaquina1 = r.randint(1, 6)
    dadoMaquina2 = r.randint(1, 6)

    dadaUsuario1 = r.randint(1, 6)
    dadoUsuario2 = r.randint(1, 6)
    
    sumaUsuario = (dadaUsuario1 + dadoUsuario2)
    sumaMaquina = (dadoMaquina1 + dadoMaquina2)

    if puntosMaquina >= 10 or puntosUsuario >= 10:
        print(f"El juego a terminado, puntajes finales: Usuario: {puntosUsuario}, Maquina: {puntosMaquina}")
        break
    
    if sumaMaquina > sumaUsuario:
        t.sleep(1)
        puntosMaquina += 3
        puntosUsuario += 1
        print(f"Esta ronda la gano la maquina.")
        print(f"Resultado dados maquina: {sumaMaquina}, puntos totales: {puntosMaquina}")
        print(f"Resultado dados usuario: {sumaUsuario}, puntos totales: {puntosUsuario} ")
        continue
    
    elif sumaUsuario > sumaMaquina:
        t.sleep(1)
        puntosMaquina += 1
        puntosUsuario += 3
        print(f"Esta ronda la gano el usuario.")
        print(f"Resultado dados maquina: {sumaMaquina}, puntos totales: {puntosMaquina}")
        print(f"Resultado dados usuario: {sumaUsuario}, puntos totales: {puntosUsuario} ")
        continue

    else:
        t.sleep(1)
        print(f"Empate en esta ronda.")
        print(f"Resultado dados maquina: {sumaMaquina}, puntos totales: {puntosMaquina}")
        print(f"Resultado dados usuario: {sumaUsuario}, puntos totales: {puntosUsuario} ")
        continue
