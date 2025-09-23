# 📄 Automatización de Documentos Word

Este proyecto automatiza la creación de documentos Word utilizando plantillas y datos externos, generando documentos personalizados de forma automática.

---

## 🔧 ¿Qué hace este proyecto?

✅ Utiliza plantillas de Word (`.docx`) para generar documentos
✅ Rellena la plantilla con datos personalizados (nombre, teléfono, correo, fecha)
✅ Procesa archivos Excel para obtener datos de alumnos
✅ Genera un documento individual para cada alumno con sus calificaciones
✅ Utiliza la biblioteca `docxtpl` para la manipulación de documentos

---

## 📁 Estructura del Proyecto

```bash
automatizar_word/
├── word.py           # Script principal de automatización
└── plantilla.docx    # Plantilla de Word para generar documentos
```

---

## 📋 Requisitos

- Python 3.x
- Bibliotecas: `pandas`, `docxtpl`, `python-docx`
- Archivos: `plantilla.docx` y `Alumnos.xlsx`

---

## 🚀 Cómo ejecutar

1. Asegúrate de tener instaladas las dependencias:
   ```bash
   pip install pandas docxtpl python-docx
   ```

2. Coloca el archivo `plantilla.docx` y `Alumnos.xlsx` en el directorio

3. Ejecuta el archivo `word.py`

4. Se generarán documentos Word personalizados para cada alumno

---

## 📸 Vista previa en consola

```plaintext
15/12/2023
{'nombre': 'Jorge Villarreal', 'telefono': '(123) 456-789', 'correo': 'jls@gmail.com', 'fecha': '15/12/2023', 'nombre_alumno': 'Ana García', 'nota_mat': 85, 'nota_fis': 92, 'nota_qui': 78}
