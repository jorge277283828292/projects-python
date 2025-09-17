from dinero import dineroTotal
import matplotlib.pyplot as plt


def ver_grafica():
    plt.plot(dineroTotal, marker="o")   # gráfico de línea
    plt.title("Gráfico de una lista")
    plt.xlabel("Índice")
    plt.ylabel("Valor")
    plt.show()