# ✂️ Juego de Piedra, Papel o Tijera

Este proyecto es una implementación del clásico juego de Piedra, Papel o Tijera contra la computadora, donde el primero en ganar 3 rondas se lleva la victoria.

---

## 🎮 ¿Qué hace este proyecto?

✅ Permite al usuario elegir entre piedra, papel o tijera
✅ La computadora elige una opción aleatoria
✅ Determina el ganador de cada ronda según las reglas clásicas
✅ Lleva un marcador de victorias (primero en 3 gana)
✅ Incluye validación de entrada del usuario
✅ Proporciona retroalimentación inmediata de cada ronda

---

## 📁 Estructura del Proyecto

```bash
piedra-papel-tijera/
└── juego.py    # Juego de piedra, papel o tijera
```

---

## 🚀 Cómo ejecutar

1. Ejecuta el archivo `juego.py`
2. Elige tu jugada: piedra, papel o tijera
3. Compite contra la computadora hasta que alguien gane 3 rondas
4. ¡Sé el primero en llegar a 3 victorias!

---

## 📸 Vista previa en consola

```plaintext
==================================================
Juego de Piedra, Papel o Tijera contra la computadora
¡El que gane 3 veces se lleva la victoria!
Elije tu jugada [Piedra] [Papel] [Tijera]: piedra
==================================================

La computadora eligio: papel
Perdiste ¡Intentalo denuevo la computadora a ganado! |Marcador Computadora: 1, Usuario: 0|

Elije tu jugada [Piedra] [Papel] [Tijera]: tijera
La computadora eligio: papel
Ganaste, ¡haz ganado! |Marcador Computadora: 1, Usuario: 1|
```

---

## 🔍 Funcionalidad

**Reglas del juego:**
- 🪨 **Piedra** gana a ✂️ Tijera
- 📄 **Papel** gana a 🪨 Piedra
- ✂️ **Tijera** gana a 📄 Papel
- 🤝 **Empate** si ambos eligen lo mismo

**Sistema de juego:**
- **Modo**: Mejor de 3 rondas
- **Entrada**: Acepta "piedra", "papel", "tijera" (case insensitive)
- **Validación**: Rechaza elecciones inválidas
- **Computadora**: Elige aleatoriamente usando `random.choice()`
- **Marcador**: Se actualiza después de cada ronda válida

**Características técnicas:**
- **Bucle principal**: Continúa hasta que alguien llegue a 3 victorias
- **Función ganadora**: Determina el resultado de cada ronda
- **Contadores**: Llevan registro de victorias de ambos jugadores
- **Mensajes**: Proporciona retroalimentación clara en cada ronda

**Estrategia:**
- El juego es completamente aleatorio
- No hay ventaja para ninguno de los jugadores
- La suerte juega un papel importante en rondas cortas
- En muchas rondas, la habilidad para elegir patrones puede ayudar

**Nota:** Este es un juego clásico que demuestra conceptos de programación como condicionales, bucles, funciones y manejo de entrada del usuario.
