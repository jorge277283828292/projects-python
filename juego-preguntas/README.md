# ❓ Juego de Preguntas y Respuestas

Este proyecto es un juego de trivia que carga preguntas desde un archivo JSON, las presenta en orden aleatorio y calcula un puntaje basado en las respuestas correctas e incorrectas.

---

## 🧠 ¿Qué hace este proyecto?

✅ Carga preguntas desde un archivo JSON
✅ Mezcla las preguntas en orden aleatorio
✅ Presenta preguntas con opciones múltiples (A/B/C)
✅ Calcula puntaje: +10 por respuesta correcta, -5 por incorrecta
✅ Utiliza pandas para el manejo de datos
✅ Proporciona retroalimentación inmediata

---

## 📁 Estructura del Proyecto

```bash
juego-preguntas/
├── main.py           # Juego principal de preguntas
└── preguntas.json    # Base de datos de preguntas
```

---

## 📋 Requisitos

- Python 3.x
- Biblioteca: `pandas`

Instalación:
```bash
pip install pandas
```

---

## 🚀 Cómo ejecutar

1. Instala la dependencia `pandas` si no la tienes
2. Asegúrate de que el archivo `preguntas.json` esté en el directorio
3. Ejecuta el archivo `main.py`
4. Responde las preguntas con A, B o C
5. ¡Obtén tu puntaje final!

---

## 📸 Vista previa en consola

```plaintext
Pregunta 1: ¿Cuál es la capital de Francia?
A) Madrid
B) París
C) Roma

Tu respuesta (A/B/C): B
¡Correcto!

Pregunta 2: ¿En qué año llegó el hombre a la Luna?
A) 1969
B) 1972
C) 1957

Tu respuesta (A/B/C): A
¡Correcto!

Puntaje final: 20
```

---

## 🔍 Funcionalidad

**Sistema de puntuación:**
- ✅ **Correcta**: +10 puntos
- ❌ **Incorrecta**: -5 puntos
- 📊 **Final**: Suma total de todos los puntos

**Características técnicas:**
- **Orden aleatorio**: Las preguntas se mezclan usando `sample(frac=1)`
- **Manejo de datos**: Utiliza pandas DataFrame para las preguntas
- **Validación**: Acepta respuestas en mayúsculas y minúsculas
- **Retroalimentación**: Indica si la respuesta es correcta o no

**Formato de preguntas.json:**
```json
[
  {
    "pregunta": "¿Pregunta?",
    "opciones": ["A) Opción A", "B) Opción B", "C) Opción C"],
    "respuesta": "A"
  }
]
```

**Nota:** Puedes agregar más preguntas editando el archivo `preguntas.json` con el formato especificado.
