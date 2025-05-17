#Da el factorial del numero ingresado por el usuario.
def factorial():
    numero = int(input("Ingrese un numero: "))
    factorial = 1
    i = 1
    while i <= numero:
        factorial = factorial * i
        i = i + 1
    print(f"El factorial es: {factorial}")

factorial()
