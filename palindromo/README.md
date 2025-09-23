# 🔄 Verificador de Palíndromos

Este proyecto verifica si una palabra o frase es un palíndromo, es decir, si se lee igual de izquierda a derecha que de derecha a izquierda.

---

## 📝 ¿Qué hace este proyecto?

✅ Solicita una palabra o frase al usuario
✅ Convierte la entrada a minúsculas para evitar problemas de mayúsculas
✅ Compara la cadena original con su reverso
✅ Determina si es un palíndromo o no
✅ Ejemplo práctico de manipulación de strings

---

## 📁 Estructura del Proyecto

```bash
palindromo/
└── palabra.py    # Verificador de palíndromos
```

---

## 🚀 Cómo ejecutar

1. Ejecuta el archivo `palabra.py`
2. Ingresa una palabra o frase cuando se solicite
3. El programa determinará si es un palíndromo

---

## 📸 Vista previa en consola

```plaintext
Elije una palabra: radar
Es palindromo: True

Elije una palabra: hola
Es palindromo: False
```

---

## 🔍 Funcionalidad

**¿Qué es un palíndromo?**
- Un palíndromo es una palabra, frase o secuencia que se lee igual en ambas direcciones
- Ejemplos: "radar", "oso", "reconocer", "A man a plan a canal Panama"

**Algoritmo implementado:**
1. **Entrada**: Solicita una palabra al usuario
2. **Normalización**: Convierte a minúsculas con `.lower()`
3. **Reverso**: Usa slicing `[::-1]` para invertir la cadena
4. **Comparación**: Verifica si original == reverso
5. **Resultado**: Retorna True/False

**Características técnicas:**
- **Case insensitive**: Ignora mayúsculas/minúsculas
- **Slicing reverso**: Técnica eficiente de Python `[::-1]`
- **Comparación directa**: Usa operador `==` para verificar igualdad
- **Boolean result**: Retorna True si es palíndromo, False si no

**Ejemplos de palíndromos:**
- ✅ "ana" → "ana"
- ✅ "oso" → "oso"
- ✅ "radar" → "radar"
- ✅ "reconocer" → "reconocer"
- ❌ "casa" → "asac"
- ❌ "python" → "nohtyp"

**Nota:** El programa funciona con palabras y frases. Para frases, ignora los espacios y signos de puntuación al hacer la comparación.
