from listas import Tareas, Tareas_completadas, Tareas_eliminadas

def agregar_tareas():
    print(" ")
    new = input("Cual tarea desseas agregar? ")
    Tareas.append(new)
    print("Tarea agregada")
    print(" ")