print("""
----------------------------------------------------
|    Adivina el numero en el que estoy pensando    |
----------------------------------------------------
      """)

print("Vamos a jugar a algo, voy a pensar en un numero y tu lo adivinas, ¿De acuerdo?");
Nombre = str(input("Pero primero, ¿cual es tu nombre?"))

Numero_secreto = 50;
intentos = 0;
while True:
    Num_Ingresado = int(input(f"Dime un numero entre 1 a 100 {Nombre}: "))
    intentos +=1;

    if Numero_secreto < Num_Ingresado:
        print("Te equivocaste, el numero es mayor que el secreto")
        

    elif Numero_secreto > Num_Ingresado:
        print("Te equivocaste, el numero es menor que el secreto")
    
    else:
        print(f"Bieeen, le atinaste, el numero secrto es {Numero_secreto}, solo te tomo {intentos} intentos");
        break