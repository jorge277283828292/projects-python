from dinero import dineroTotal
import pandas as pd

def imprimir_reporte():
    df = pd.DataFrame(dineroTotal, columns=["Dinero Total:"])
    # Guardar en Excel
    df.to_excel("dinero.xlsx", index=False)