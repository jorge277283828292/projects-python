                                                                                                                                                                                                                                                                                                                                                                                                                                     # 🔢 Elevación al Cuadrado con Map

Este proyecto eleva al cuadrado todos los elementos de una lista de números utilizando la función `map()` de Python.

---

## 📐 ¿Qué hace este proyecto?

✅ Eleva al cuadrado cada número de una lista
✅ Utiliza la función `map()` para aplicar la operación
✅ Convierte el resultado a lista para mostrarlo
✅ Ejemplo práctico de programación funcional en Python

---

## 📁 Estructura del Proyecto

```bash
elevacion-cuadrado/
└── cuadrado.py    # Calculadora de cuadrados
```

---

## 🚀 Cómo ejecutar

1. Ejecuta el archivo `cuadrado.py`
2. El programa procesa automáticamente la lista de números
3. Observa la lista original y los cuadrados resultantes

---

## 📸 Vista previa en consola

```plaintext
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

---

## 🔍 Funcionalidad

El programa utiliza la lista: `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`

**Proceso:**
1. **Define función**: `cuadrado(x)` que retorna `x ** 2`
2. **Aplica map**: `map(cuadrado, numeros)`
3. **Convierte a lista**: `list(map(cuadrado, numeros))`

**Ventajas de usar map():**
- ✅ Más eficiente que los bucles tradicionales
- ✅ Código más limpio y funcional
- ✅ Fácil de entender y mantener
- ✅ Puede aplicarse a cualquier iterable

**Nota:** La función `map()` retorna un iterador que debe convertirse a lista para ver todos los resultados.
