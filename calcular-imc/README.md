# ⚖️ Calculadora de Índice de Masa Corporal (IMC)

Este proyecto calcula el Índice de Masa Corporal (IMC) de una persona y determina su categoría de peso según los estándares médicos internacionales.

---

## 🏥 ¿Qué hace este proyecto?

✅ Calcula el IMC usando la fórmula: peso / (altura)²
✅ Clasifica el resultado en categorías de peso
✅ Utiliza valores predefinidos para demostración
✅ Proporciona diagnóstico según estándares médicos
✅ Ejemplo práctico de condicionales múltiples

---

## 📁 Estructura del Proyecto

```bash
calcular-imc/
└── peso.py    # Calculadora de IMC
```

---

## 🚀 Cómo ejecutar

1. Ejecuta el archivo `peso.py`
2. Observa el IMC calculado y la categoría
3. El resultado se muestra automáticamente

---

## 📸 Vista previa en consola

```plaintext
Total de IMC: 22.857142857142858
Peso normal.
```

---

## 🔍 Funcionalidad

**Fórmula del IMC:**
```
IMC = peso (kg) / (altura (m))²
```

**Valores del ejemplo:**
- Peso: 70 kg
- Altura: 1.75 m
- IMC: ≈ 22.86

**Categorías de IMC según OMS:**
- 🟢 **Bajo peso**: IMC < 18.5
- 🟢 **Peso normal**: 18.5 ≤ IMC < 25
- 🟡 **Sobrepeso**: 25 ≤ IMC < 30
- 🔴 **Obesidad grado I**: 30 ≤ IMC < 35
- 🔴 **Obesidad grado II**: 35 ≤ IMC < 40
- 🔴 **Obesidad grado III**: IMC ≥ 40

**Características técnicas:**
- **Valores fijos**: Peso=70kg, altura=1.75m
- **Cálculo preciso**: Usa fórmula matemática correcta
- **Condicionales múltiples**: Clasifica en 6 categorías
- **Formato decimal**: Muestra resultado con precisión

**Algoritmo:**
1. **Definir valores**: Peso y altura preestablecidos
2. **Calcular IMC**: Dividir peso por altura al cuadrado
3. **Mostrar resultado**: Imprimir el valor del IMC
4. **Clasificar**: Usar condicionales para determinar categoría
5. **Mostrar diagnóstico**: Imprimir la categoría correspondiente

**Ejemplos de cálculo:**
- Peso: 50kg, Altura: 1.60m → IMC: 19.53 (Peso normal)
- Peso: 80kg, Altura: 1.70m → IMC: 27.68 (Sobrepeso)
- Peso: 90kg, Altura: 1.65m → IMC: 33.06 (Obesidad grado I)

**Interpretación médica:**
- **Bajo peso**: Puede indicar desnutrición o problemas de salud
- **Normal**: Peso saludable, menor riesgo de enfermedades
- **Sobrepeso**: Aumenta riesgo de diabetes, hipertensión
- **Obesidad**: Mayor riesgo de enfermedades cardiovasculares

**Personalización:**
Para calcular IMC de diferentes personas:
```python
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# Ejemplo de uso
mi_imc = calcular_imc(65, 1.68)  # IMC: 23.03
```

**Unidades importantes:**
- **Peso**: Siempre en kilogramos (kg)
- **Altura**: Siempre en metros (m)
- **Resultado**: kg/m² (índice, no una unidad de medida)

**Nota:** El IMC es una herramienta de screening, no un diagnóstico médico. Consulta a un profesional de la salud para una evaluación completa.
