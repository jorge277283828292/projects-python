from dinero import dineroTotal
def consultar_saldo():
    if dineroTotal <= 0:
        print("El saldo actual es: 0") 
    else:
        for saldo in dineroTotal:
            print(f"El saldo actual es: {float(saldo)}$")
            