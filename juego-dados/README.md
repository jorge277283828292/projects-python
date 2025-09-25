# Juego de Dados

Este es un juego simple de dados entre un usuario y la máquina. El objetivo es ser el primero en llegar a 10 puntos.

## Reglas del Juego

- En cada ronda, tanto el usuario como la máquina lanzan dos dados (números aleatorios del 1 al 6).
- Se suman los valores de los dos dados para obtener la puntuación de la ronda.
- El jugador con la suma más alta gana la ronda:
  - Gana +3 puntos.
  - El perdedor gana +1 punto.
- En caso de empate, nadie gana puntos.
- El juego continúa hasta que uno de los jugadores llegue a 10 puntos o más.

## Cómo Ejecutar

1. Asegúrate de tener Python instalado.
2. Ejecuta el archivo `main.py`:

   ```
   python main.py
   ```

3. El juego se ejecutará automáticamente, mostrando los resultados de cada ronda y los puntos acumulados.

## Ejemplo de Salida

```
Esta ronda la gano la maquina.
Resultado dados maquina: 8, puntos totales: 3
Resultado dados usuario: 5, puntos totales: 1
...
El juego a terminado, puntajes finales: 10, 7
```

## Dependencias

- Python 3.x
- Módulos estándar: `random`, `time`

## Notas

- El juego incluye un retraso de 1 segundo entre rondas para una mejor experiencia.
- Los dados se generan aleatoriamente en cada ronda.
