#Elimina los duplicados de una lista de datos int.
def listaDuplicados():
    lista = [1, 2, 3, 4, 5, 1, 2, 3, 6, 7, 8, 9, 10];
    sinDuplicados = list(set(lista));

    print(f"{sinDuplicados}");
    return sinDuplicados;

listaDuplicados();