# 🎯 Juego de Adivinar el Número

Este proyecto es un juego simple donde el programa genera un número aleatorio entre 1 y 10, y el usuario debe adivinarlo con la menor cantidad de intentos posible.

---

## 🎲 ¿Qué hace este proyecto?

✅ Genera un número aleatorio entre 1 y 10
✅ Permite al usuario hacer múltiples intentos
✅ Cuenta el número de intentos realizados
✅ Valida que el número esté en el rango correcto
✅ Proporciona retroalimentación inmediata

---

## 📁 Estructura del Proyecto

```bash
numero-random/
└── adivinar.py    # Juego de adivinar número
```

---

## 🚀 Cómo ejecutar

1. Ejecuta el archivo `adivinar.py`
2. Ingresa números entre 1 y 10 para adivinar
3. El juego termina cuando adivinas correctamente
4. ¡Intenta hacerlo en la menor cantidad de intentos!

---

## 📸 Vista previa en consola

```plaintext
Adivinar el numero: 5
Adivinar el numero: 3
Adivinar el numero: 7
Correcto adivinaste el numero : 7, en 3 intentos.
```

---

## 🔍 Funcionalidad

**Rango del número:** 1 a 10 (inclusive)

**Validaciones:**
- ✅ Acepta números enteros
- ❌ Rechaza números fuera del rango 1-10
- 📊 Cuenta todos los intentos válidos

**Características del juego:**
- **Número aleatorio**: Se genera usando `random.randint(1, 10)`
- **Bucle infinito**: Continúa hasta que se adivine correctamente
- **Contador**: Lleva registro de intentos válidos
- **Mensaje final**: Muestra el número correcto y cantidad de intentos

**Estrategia óptima:**
- El número mínimo de intentos es 1 (adivinar en el primer try)
- El número máximo de intentos es 10 (probar todos los números)
- La estrategia más eficiente es probar sistemáticamente

