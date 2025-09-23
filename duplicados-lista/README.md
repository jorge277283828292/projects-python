# 🔄 Eliminador de Duplicados en Lista

Este proyecto elimina los elementos duplicados de una lista de números enteros, manteniendo solo los valores únicos.

---

## 🧹 ¿Qué hace este proyecto?

✅ Elimina elementos duplicados de una lista
✅ Utiliza la función `set()` para obtener valores únicos
✅ Convierte el resultado de vuelta a lista
✅ Ejemplo práctico de manejo de datos en Python

---

## 📁 Estructura del Proyecto

```bash
duplicados-lista/
└── eliminar_duplicados.py    # Eliminador de duplicados
```

---

## 🚀 Cómo ejecutar

1. Ejecuta el archivo `eliminar_duplicados.py`
2. El programa procesa automáticamente la lista con duplicados
3. Observa la lista resultante sin elementos repetidos

---

## 📸 Vista previa en consola

```plaintext
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

---

## 🔍 Funcionalidad

El programa utiliza la lista original: `[1, 2, 3, 4, 5, 1, 2, 3, 6, 7, 8, 9, 10]`

**Proceso:**
1. **Convierte a set**: `set([1, 2, 3, 4, 5, 1, 2, 3, 6, 7, 8, 9, 10])`
2. **Elimina duplicados**: `{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}`
3. **Convierte a lista**: `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`

**Nota:** Los sets no mantienen el orden original y no permiten elementos duplicados. Esta es una forma eficiente de eliminar duplicados en Python.
