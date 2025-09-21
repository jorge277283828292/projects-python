import pandas as pd

df = pd.read_json("juego-preguntas/preguntas.json")
df = df.sample(frac=1).reset_index(drop=True)

puntos = 0

for i, row in df.iterrows():
    print(f"\nPregunta {i+1}: {row['pregunta']}")
    for opcion in row['opciones']:
        print(opcion)

    # Pedir respuesta al usuario
    respuesta = input("Tu respuesta (A/B/C): ").upper().strip()

    # Comparar con la respuesta correcta
    if respuesta == row['respuesta']:
        print("¡Correcto!")
        puntos += 10
    else:
        print(f"Incorrecto. La respuesta era {row['respuesta']}")
        puntos -= 5

print(f"\nPuntaje final: {puntos}")