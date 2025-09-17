from opciones import mostrar_opciones
from dinero import dineroTotal, historial
from dinero_inicial import *
from registro_gasto import *
from consultar_saldo import *
from depositar_dinero import *
from ver_grafica import *
from crear_factura import *
from ver_historial import *

while True: 
    mostrar_opciones()
    eleccion = input("Seleccione una opción: ")

    if eleccion == "1":
        dinero_inicial()
        continue #Listo
    elif eleccion == "2":
        dineroTotal, historial = depositar_dinero(dineroTotal, historial)
        continue
    elif eleccion == "3":
        dineroTotal, historial = definir_gasto(dineroTotal, historial)
        continue
    elif eleccion == "4":
        consultar_saldo()
        continue
    elif eleccion == "5":
        historial_dinero()
        continue
    elif eleccion == "6":
        ver_grafica()
        continue
    elif eleccion == "7":
        imprimir_reporte()  
        continue
    elif eleccion == "8":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Intente de nuevo.")