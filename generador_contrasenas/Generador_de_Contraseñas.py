import random as r
import string as s
caracteres = ""
contraseña = []
usar_letras = False
usar_numeros = False
usar_simbolos = False
texto = """ 
1. Letras
2. Numeros
3. Simbolos
4. Generar Contraseña
"""

print("Bienvenido aqui puedes generar tu constraseña")

num = int(input("Dame la longitud que desea que tenga la contraseña:"))
while True:
    print(texto)
    
    try:
        eleccion = int(input("Elige una opcion: "))
    except Exception as e:
        print(e)
        continue

    if eleccion == 1:
        usar_letras = True
    
    elif eleccion == 2:
        usar_numeros = True

    elif eleccion == 3:
        usar_simbolos = True

    elif eleccion == 4:
        if usar_letras:
            caracteres += s.ascii_letters  # Agrega letras
            contraseña.append(r.choice(s.ascii_letters)) 
        if usar_numeros:
            caracteres += s.digits  # Agrega números
            contraseña.append(r.choice(s.digits)) 
        if usar_simbolos:
            caracteres += s.punctuation  # Agrega símbolos
            contraseña.append(r.choice(s.punctuation)) 

        while len(contraseña) < num:
            contraseña.append(r.choice(caracteres))

        r.shuffle(contraseña)

        contraseña_final = ''.join(contraseña)
        print(f"\n🔐 Tu contraseña generada es:, {contraseña_final}")
        break
    else:
        print("Lo siento, opcion invalida")

 






    #for i in range(1, num):
        #lista.append(i)
        #print(i)