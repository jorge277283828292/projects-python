from dinero import dineroTotal, historial

def definir_gasto(dineroTotal, historial):
    if dineroTotal <= 0:
        print("No hay saldo disponible para registrar un gasto.")
        return dineroTotal, historial
    gasto = int(input("Ingrese el monto del gasto: "))
    dineroTotal -= gasto
    historial.append({"gasto": gasto})
    print(f"Gasto de {gasto} registrado. Saldo actual: {dineroTotal}$")
    return dineroTotal, historial