# 🔢 Calculadora de Factorial

Este proyecto calcula el factorial de un número entero positivo ingresado por el usuario, utilizando un bucle while para realizar la multiplicación secuencial.

---

## 📐 ¿Qué hace este proyecto?

✅ Solicita un número entero al usuario
✅ Calcula el factorial usando un bucle while
✅ Muestra el resultado del cálculo factorial
✅ Ejemplo básico de algoritmos iterativos en Python

---

## 📁 Estructura del Proyecto

```bash
numero-factorial/
└── factorial.py    # Calculadora de factorial
```

---

## 🚀 Cómo ejecutar

1. Ejecuta el archivo `factorial.py`
2. Ingresa un número entero positivo cuando se solicite
3. Observa el factorial calculado

---

## 📸 Vista previa en consola

```plaintext
Ingrese un numero: 5
El factorial es: 120
```

---

## 🔍 Funcionalidad

**¿Qué es el factorial?**
- El factorial de un número n (n!) es el producto de todos los números enteros positivos desde 1 hasta n
- Fórmula: n! = 1 × 2 × 3 × ... × n

**Ejemplos de factoriales:**
- 0! = 1 (por definición matemática)
- 1! = 1
- 2! = 2
- 3! = 6
- 4! = 24
- 5! = 120
- 6! = 720

**Algoritmo implementado:**
1. **Entrada**: Solicita un número al usuario
2. **Inicialización**: factorial = 1, i = 1
3. **Bucle**: Mientras i <= número, multiplica factorial por i
4. **Incremento**: Aumenta i en 1 cada iteración
5. **Resultado**: Muestra el factorial calculado

**Nota:** El factorial crece muy rápidamente. Por ejemplo, 10! = 3,628,800 y 20! es un número con 19 dígitos.
