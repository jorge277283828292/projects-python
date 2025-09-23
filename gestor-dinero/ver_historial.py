from dinero import dineroTotal, historial

def historial_dinero():
    if not historial:
        print("No hay movimientos registrados.")
    else:
        for movimiento in historial:
            for tipo, monto in movimiento.items():
                print(f"{tipo.capitalize()}: {monto}")
