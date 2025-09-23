# 📅 Verificador de Año Bisiesto

Este proyecto determina si un año específico es bisiesto o no, aplicando las reglas del calendario gregoriano para años bisiestos.

---

## 🗓️ ¿Qué hace este proyecto?

✅ Verifica si un año es divisible por 4
✅ Aplica la excepción de años divisibles por 100
✅ Incluye la regla especial de años divisibles por 400
✅ Determina si el año tiene 365 o 366 días
✅ Ejemplo práctico de condicionales compuestos

---

## 📁 Estructura del Proyecto

```bash
bisiesto/
└── bisieto.py    # Verificador de año bisiesto
```

---

## 🚀 Cómo ejecutar

1. Ejecuta el archivo `bisieto.py`
2. Observa si el año predefinido es bisiesto o no
3. El resultado se muestra automáticamente

---

## 📸 Vista previa en consola

```plaintext
No es año Bisieto
```

---

## 🔍 Funcionalidad

**Reglas para año bisiesto:**
1. ✅ **Regla principal**: El año debe ser divisible por 4
2. ❌ **Excepción**: Si es divisible por 100, NO es bisiesto
3. ✅ **Excepción a la excepción**: Si es divisible por 400, SÍ es bisiesto

**Fórmula lógica:**
```python
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    return "Es bisiesto"
else:
    return "No es bisiesto"
```

**Ejemplos de años bisiestos:**
- ✅ 2000: Divisible por 400
- ✅ 2004: Divisible por 4, no por 100
- ✅ 2008: Divisible por 4, no por 100
- ✅ 2012: Divisible por 4, no por 100
- ❌ 1900: Divisible por 100, no por 400
- ❌ 2025: No divisible por 4

**Año del ejemplo:** 2025
- 2025 ÷ 4 = 506.25 (no divisible por 4)
- **Resultado**: No es año bisiesto

**Características técnicas:**
- **Año fijo**: Usa el año 2025 como ejemplo
- **Condicionales anidados**: Implementa las reglas del calendario gregoriano
- **Operadores lógicos**: Usa `and`, `or` y `not` para las condiciones
- **Módulo**: Utiliza el operador `%` para verificar divisibilidad

**Historia del calendario:**
- **Calendario juliano**: Introducido por Julio César en el 46 a.C.
- **Calendario gregoriano**: Reformado por el Papa Gregorio XIII en 1582
- **Años bisiestos**: Compensan la diferencia entre el año solar (365.2425 días) y el año calendario (365 días)

**Personalización:**
Para verificar diferentes años, modifica la variable `anio`:
```python
def es_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    return False

# Ejemplos
print(es_bisiesto(2024))  # True
print(es_bisiesto(2025))  # False
```

**Nota:** Los años bisiestos son importantes para mantener sincronizado el calendario con las estaciones del año.
