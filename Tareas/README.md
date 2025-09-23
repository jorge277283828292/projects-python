# ✅ Gestor de Tareas en Python

Este proyecto es un sistema de gestión de tareas que permite agregar, eliminar, ver, marcar como completadas y restaurar tareas.

---

## 📋 ¿Qué hace este proyecto?

✅ Agrega nuevas tareas a la lista
✅ Elimina tareas existentes
✅ Muestra la lista de tareas activas
✅ Marca tareas como completadas
✅ Restaura tareas eliminadas
✅ Menú interactivo para seleccionar opciones

---

## 📁 Estructura del Proyecto

```bash
tareas/
├── main.py                  # Archivo principal que ejecuta el programa
├── opciones.py              # Define el menú de opciones
├── agregar.py               # Función para agregar tareas
├── quitar.py                # Función para eliminar tareas
├── ver.py                   # Función para ver tareas
├── completadas.py           # Función para marcar como completadas
├── restaurar.py             # Función para restaurar tareas
└── listas.py                # Define las listas de tareas
```

---

## 🚀 Cómo ejecutar

1. Ejecuta el archivo `main.py`
2. Selecciona una opción del menú (1-6)
3. Sigue las instrucciones para cada función
4. Elige '6' para salir

---

## 📸 Vista previa en consola

```plaintext
---------------------------------
Opciones: 
1. Agregar tarea
2. Eliminar tarea
3. Ver tareas
4. Marcar tarea como completada
5. Restaurar tarea eliminada
6. Salir
---------------------------------

Cual opcion deseas? 1
Ingrese la tarea: Comprar leche
Tarea agregada: Comprar leche

Cual opcion deseas? 3
Tareas activas:
- Comprar leche
