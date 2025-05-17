#Obtener la cantidad de ram del usuario.
import psutil

def obtener_ram():
    memoria = psutil.virtual_memory()
    memoria_total = memoria.total / (1024 ** 3)
    return memoria_total

memoria = obtener_ram()

print(f"Total de ram: {memoria} GB.")