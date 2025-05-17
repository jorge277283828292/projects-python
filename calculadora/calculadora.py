from Opciones import Opcion

def valor1():
    num1 = int(input("Ingrese el primer número: "))
    return num1

def valor2():
    num2 = int(input("Ingrese el segundo numero: "))
    return num2

a = valor1()
b = valor2()

while True:
    Opcion()
    try:
        Eleccion=int(input("Que operacion desea realizar: "))
        if Eleccion == 1:
            print(f"Resultado de la suma: {a + b}")
            continue
        elif Eleccion == 2:
            print(f"Resultado de la resta: {a - b}")
            continue
        elif Eleccion == 3:
            print(f"Resultado de la multiplicación: {a * b}")
        elif Eleccion == 4:
            if b != 0:
                print(f"Resultado de la división: {a / b}")
                continue
            else:
                print("Error: No se puede dividir entre cero.")
                continue
        elif Eleccion == 5:
            print(f"Resultado de la potencia: {a ** b}")
            continue
        elif Eleccion == 6:
            print("Saliendo del programa...")
            break
        else:
            print("Opcion Invalida!.")
            continue
    except ValueError:
        print("Porfavor ingrese un valor valido!")
        continue