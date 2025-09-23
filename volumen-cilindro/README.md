# 🥫 Calculadora de Volumen de Cilindro

Este proyecto calcula el volumen de un cilindro utilizando la fórmula matemática estándar: volumen = π × radio² × altura.

---

## 📐 ¿Qué hace este proyecto?

✅ Calcula el volumen de un cilindro con radio y altura dados
✅ Utiliza la constante π del módulo `math` de Python
✅ Aplica la fórmula matemática correcta para cilindros
✅ Ejemplo práctico de funciones y operaciones matemáticas

---

## 📁 Estructura del Proyecto

```bash
volumen-cilindro/
└── cilindro.py    # Calculadora de volumen de cilindro
```

---

## 🚀 Cómo ejecutar

1. Ejecuta el archivo `cilindro.py`
2. Observa el volumen calculado con los valores predefinidos
3. El resultado se muestra automáticamente

---

## 📸 Vista previa en consola

```plaintext
4069.467575584499
```

---

## 🔍 Funcionalidad

**Fórmula del volumen de cilindro:**
```
V = π × r² × h
```

Donde:
- **V** = Volumen
- **π** = Constante pi (3.14159...)
- **r** = Radio de la base
- **h** = Altura del cilindro

**Valores del ejemplo:**
- Radio: 12 unidades
- Altura: 9 unidades
- Volumen: ≈ 4069.47 unidades³

**Características técnicas:**
- **Función definida**: `volumenCilindro(radio, altura)`
- **Constante π**: Importada del módulo `math`
- **Operaciones**: Multiplicación y potenciación
- **Valores fijos**: Radio=12, altura=9

**Algoritmo:**
1. **Definir función**: Recibe radio y altura como parámetros
2. **Calcular**: Multiplica π × radio² × altura
3. **Retornar**: Devuelve el resultado del cálculo
4. **Mostrar**: Imprime el volumen calculado

**Ejemplo de uso:**
```python
def volumenCilindro(radio, altura):
    return math.pi * radio ** 2 * altura

# Ejemplo con radio=5, altura=10
volumen = volumenCilindro(5, 10)  # Resultado: 785.398...
```

**Personalización:**
Para calcular diferentes cilindros, modifica los valores en la llamada a la función:
```python
resultado = volumenCilindro(tu_radio, tu_altura)
```

**Unidades:**
- El resultado está en las mismas unidades cúbicas que el radio y altura
- Ejemplo: si radio está en cm y altura en cm, volumen estará en cm³

**Nota:** Este programa demuestra el uso de funciones matemáticas en Python y puede extenderse para calcular volúmenes de múltiples cilindros o con entrada del usuario.
