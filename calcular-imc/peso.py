#Calcula el IMC(IMG: Es como una medida entre altura y peso de la persona que determina si su peso es saludable, sobrepeso o otras medidas.)
def calcularIMC(peso, altura):
    peso = 70
    altura = 1.75
    imc = peso / (altura ** 2)
    print(f"Total de IMC: {imc}")

    return imc

IMC = calcularIMC()

if IMC < 18.5:
    print(f"Bajo peso.")
elif IMC < 25:
    print(f"Peso normal.")
elif IMC < 30:
    print(f"Sobrepeso.")
elif IMC < 35:
    print(f"Obesidad grado I.")
elif IMC < 40:
    print(f"Obesidad grado II.")
else:
    print(f"Obesidad grado III")