#Solicita una palabra/frase al usuario y dice si es palindromo o no(Palindromo es cuando la palabra lleva el mismo orden de letras al derecho y al revez).
def esPalindromo():
    palabra = input(f"Elije una palabra: ").lower()

    esPa = palabra == palabra[::-1]

    print(f"Es palindromo: {esPa}")
    return esPa

esPalindromo()