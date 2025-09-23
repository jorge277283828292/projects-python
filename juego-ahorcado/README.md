# 🪢 Juego del Ahorcado

Este proyecto es una implementación del clásico juego del ahorcado en Python, donde el jugador debe adivinar una palabra letra por letra antes de que se complete el dibujo del ahorcado.

---

## 🎮 ¿Qué hace este proyecto?

✅ Selecciona aleatoriamente una palabra de una lista
✅ Muestra el progreso con guiones bajos para las letras no adivinadas
✅ Permite al jugador adivinar letras una por una
✅ Incluye un sistema de errores con dibujo del ahorcado
✅ Utiliza archivos JSON para las palabras y el personaje
✅ Finaliza el juego cuando se adivina la palabra o se agotan los intentos

---

## 📁 Estructura del Proyecto

```bash
juego-ahorcado/
├── main.py           # Juego principal del ahorcado
├── palabras.json     # Lista de palabras para adivinar
└── personaje.json    # Dibujos del ahorcado por etapas
```

---

## 🚀 Cómo ejecutar

1. Asegúrate de que los archivos `palabras.json` y `personaje.json` estén en el directorio
2. Ejecuta el archivo `main.py`
3. Adivina letras para descubrir la palabra secreta
4. ¡Gana adivinando la palabra completa o pierde al completar el ahorcado!

---

## 📸 Vista previa en consola

```plaintext
_ _ _ _ _ _ _ _ _ _

Adivina una letra de la palabra: A
_ _ _ _ _ _ _ _ _ _

Adivina una letra de la palabra: E
_ E _ _ _ _ _ _ _ _

Adivina una letra de la palabra: O
_ E _ _ _ O _ _ _ _

¡Felicidades! Adivinaste la palabra: DESARROLLO
```

---

## 🔍 Funcionalidad

**Componentes del juego:**
- **Palabras**: Lista de palabras en `palabras.json`
- **Progreso**: Se muestra con guiones bajos para letras no adivinadas
- **Errores**: Sistema de 6 intentos (0-5)
- **Dibujo**: Se muestra el personaje del ahorcado según los errores
- **Victoria**: Se adivina la palabra completa
- **Derrota**: Se agotan los 6 intentos

**Archivos JSON:**
- `palabras.json`: Contiene la lista de palabras disponibles
- `personaje.json`: Contiene los dibujos del ahorcado por etapas

**Nota:** El juego es completamente interactivo y utiliza archivos externos para mayor flexibilidad y personalización.
