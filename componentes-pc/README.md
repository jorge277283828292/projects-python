# 💾 Monitor de Memoria RAM del Sistema                                                           
Este proyecto obtiene y muestra información sobre la memoria RAM del sistema utilizando la biblioteca `psutil`, mostrando la cantidad total de RAM instalada.

---

## 🖥️ ¿Qué hace este proyecto?

✅ Obtiene información de la memoria RAM del sistema
✅ Utiliza la biblioteca `psutil` para acceso al hardware
✅ Convierte bytes a gigabytes para mejor legibilidad
✅ Muestra la cantidad total de RAM instalada
✅ Ejemplo práctico de monitoreo del sistema

---

## 📁 Estructura del Proyecto

```bash
componentes-pc/
└── computadora.py    # Monitor de RAM del sistema
```

---

## 📋 Requisitos

- Python 3.x
- Biblioteca: `psutil`

Instalación:
```bash
pip install psutil
```

---

## 🚀 Cómo ejecutar

1. Instala la dependencia `psutil` si no la tienes
2. Ejecuta el archivo `computadora.py`
3. Observa la cantidad total de RAM del sistema
4. El resultado se muestra automáticamente

---

## 📸 Vista previa en consola

```plaintext
Total de ram: 15.8 GB.
```

---

## 🔍 Funcionalidad

**Información obtenida:**
- **Memoria total**: Cantidad total de RAM instalada
- **Unidad**: Resultado en Gigabytes (GB)
- **Precisión**: Valor decimal para mayor exactitud

**Características técnicas:**
- **Biblioteca psutil**: Acceso a información del sistema
- **Conversión de unidades**: Bytes a GB (1024³)
- **Método virtual_memory()**: Obtiene datos de memoria RAM
- **Formato legible**: Resultado redondeado y claro

**Algoritmo:**
1. **Importar psutil**: Carga la biblioteca del sistema
2. **Obtener memoria**: Usa `psutil.virtual_memory()`
3. **Extraer total**: Obtiene el valor total en bytes
4. **Convertir unidades**: Divide por 1024³ para obtener GB
5. **Mostrar resultado**: Imprime la cantidad de RAM

**Ejemplo de uso:**
```python
import psutil

def obtener_ram():
    memoria = psutil.virtual_memory()
    memoria_total = memoria.total / (1024 ** 3)
    return memoria_total

# Resultado varía según el sistema
ram_total = obtener_ram()
print(f"Total de RAM: {ram_total:.1f} GB")
```

**Información del sistema:**
- **RAM total**: Memoria física instalada en el sistema
- **Disponible**: Memoria no utilizada por el sistema
- **Usada**: Memoria actualmente en uso
- **Porcentaje**: Uso de memoria en porcentaje

**Aplicaciones prácticas:**
- **Diagnóstico**: Verificar especificaciones del hardware
- **Monitoreo**: Seguimiento del uso de recursos
- **Requisitos**: Verificar si el sistema cumple con mínimos
- **Optimización**: Identificar necesidades de actualización

**Consideraciones importantes:**
- **Unidades**: 1 GB = 1024 MB = 1024³ bytes
- **Precisión**: Los valores pueden variar ligeramente
- **Sistema operativo**: Compatible con Windows, Linux, macOS
- **Permisos**: No requiere permisos especiales

**Personalización:**
Para obtener más información de memoria:
```python
import psutil

memoria = psutil.virtual_memory()
print(f"Total: {memoria.total / (1024**3):.1f} GB")
print(f"Disponible: {memoria.available / (1024**3):.1f} GB")
print(f"Usada: {memoria.used / (1024**3):.1f} GB")
print(f"Porcentaje: {memoria.percent}%")
```

