 # 📏 Calculadora de Área de Rectángulo

Este proyecto calcula el área de un rectángulo solicitando al usuario la base y la altura, utilizando la fórmula matemática básica: área = base × altura.

---

## 🔢 ¿Qué hace este proyecto?

✅ Solicita la base del rectángulo al usuario
✅ Solicita la altura del rectángulo al usuario
✅ Calcula el área multiplicando base por altura
✅ Muestra el resultado del cálculo
✅ Ejemplo básico de entrada de usuario y operaciones matemáticas

---

## 📁 Estructura del Proyecto

```bash
area_rectangulo/
└── rectangulo.py    # Calculadora del área del rectángulo
```

---

## 🚀 Cómo ejecutar

1. Ejecuta el archivo `rectangulo.py`
2. Ingresa el valor de la base cuando se solicite
3. Ingresa el valor de la altura cuando se solicite
4. Observa el área calculada

---

## 📸 Vista previa en consola

```plaintext
Ingrese la base: 8
Ingrese la altura: 5
El área es: 40
```

---

## 🔍 Funcionalidad

**Fórmula del área de rectángulo:**
```
Área = base × altura
```

**Características técnicas:**
- **Entrada interactiva**: Solicita dos valores al usuario
- **Validación básica**: Acepta números enteros
- **Cálculo simple**: Multiplicación directa
- **Función definida**: `area_rectangulo()` para organización

**Algoritmo:**
1. **Solicitar base**: Pide el valor de la base al usuario
2. **Solicitar altura**: Pide el valor de la altura al usuario
3. **Calcular área**: Multiplica base por altura
4. **Mostrar resultado**: Imprime el área calculada
5. **Retornar valor**: Devuelve el área calculada

**Ejemplos de cálculo:**
- Base: 5, Altura: 3 → Área: 15
- Base: 10, Altura: 8 → Área: 80
- Base: 12, Altura: 6 → Área: 72
- Base: 7, Altura: 9 → Área: 63

**Tipos de rectángulos:**
- **Cuadrado**: Cuando base = altura (ej: 5×5 = 25)
- **Rectángulo horizontal**: Base > altura (ej: 10×4 = 40)
- **Rectángulo vertical**: Altura > base (ej: 4×10 = 40)

**Personalización:**
Para usar valores fijos en lugar de entrada del usuario:
```python
def area_rectangulo(base, altura):
    return base * altura

# Ejemplo de uso
area = area_rectangulo(12, 8)  # Área: 96
```

**Unidades:**
- El resultado está en las mismas unidades cuadradas que base y altura
- Ejemplo: si base está en metros y altura en metros, área estará en m²

**Nota:** Este programa es ideal para estudiantes que están aprendiendo conceptos básicos de geometría y programación.
