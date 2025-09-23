from dinero import dineroTotal, historial

def depositar_dinero(dineroTotal, historial):
    deposito = int(input("Ingrese el monto a depositar: "))
    dineroTotal += deposito
    historial.append({"deposito": deposito})
    print(f"Depósito de {deposito} realizado. Saldo actual: {dineroTotal}$")
    return dineroTotal, historial