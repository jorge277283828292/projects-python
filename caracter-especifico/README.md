# 🔤 Contador de Caracteres Específicos                                                                                                                                                                                                       
Este proyecto cuenta cuántas veces aparece un carácter específico en una cadena de texto, demostrando el uso del método `count()` de Python.

---

## 📊 ¿Qué hace este proyecto?

✅ Define una cadena de texto preestablecida
✅ Cuenta las ocurrencias de un carácter específico
✅ Utiliza el método `count()` de strings de Python
✅ Muestra el resultado del conteo
✅ Ejemplo básico de manipulación de cadenas

---

## 📁 Estructura del Proyecto

```bash
caracter-especifico/
└── caracter.py    # Contador de caracteres
```

---

## 🚀 Cómo ejecutar

1. Ejecuta el archivo `caracter.py`
2. Observa el conteo de ocurrencias del carácter
3. El resultado se muestra automáticamente

---

## 📸 Vista previa en consola

```plaintext
Ocurrencias 2
```

---

## 🔍 Funcionalidad

**Cadena del ejemplo:**
```
"progrmacion orientada a objetos"
```

**Caracter a contar:** 'a'

**Resultado:** 2 ocurrencias

**Características técnicas:**
- **Cadena fija**: Texto predefinido para demostración
- **Método count()**: Función built-in de Python para contar
- **Caracter específico**: Cuenta solo la letra 'a' (minúscula)
- **Retorno de valor**: Devuelve el número de ocurrencias

**Algoritmo:**
1. **Definir cadena**: Texto de ejemplo preestablecido
2. **Seleccionar carácter**: Elige el carácter a contar ('a')
3. **Contar ocurrencias**: Usa `cadena.count('a')`
4. **Mostrar resultado**: Imprime el número de ocurrencias
5. **Retornar valor**: Devuelve el conteo para uso posterior

**Ejemplos de conteo:**
- "programación" → 'a': 2, 'o': 1, 'i': 1
- "banana" → 'a': 3, 'n': 2, 'b': 1
- "Python" → 'P': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1

**Método count() en Python:**
```python
cadena = "texto de ejemplo"
ocurrencias = cadena.count('e')  # Cuenta 'e'
print(ocurrencias)  # Muestra: 3
```

**Personalización:**
Para contar diferentes caracteres o usar otras cadenas:
```python
def contar_caracter(cadena, caracter):
    return cadena.count(caracter)

# Ejemplos de uso
texto = "Hola mundo"
print(contar_caracter(texto, 'o'))  # 2
print(contar_caracter(texto, 'l'))  # 1
```

**Aplicaciones prácticas:**
- **Análisis de texto**: Contar frecuencia de letras
- **Validación**: Verificar caracteres especiales
- **Estadísticas**: Análisis de frecuencia en textos
- **Búsqueda**: Encontrar patrones repetitivos

**Case sensitivity:**
- El método `count()` distingue entre mayúsculas y minúsculas
- 'a' ≠ 'A' (cuenta solo minúsculas)
- Para conteo case-insensitive, convertir a minúsculas primero

