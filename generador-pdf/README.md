# 📄 Generador de PDFs Personalizados

Este proyecto genera archivos PDF personalizados con títulos, contenido estructurado, encabezados, pies de página y la posibilidad de incluir imágenes.

---

## 🛠️ ¿Qué hace este proyecto?

✅ Genera PDFs con estructura profesional
✅ Incluye encabezados y pies de página personalizables
✅ Permite agregar múltiples capítulos con títulos
✅ Soporta la inserción de imágenes
✅ Utiliza la biblioteca `fpdf` para la generación

---

## 📁 Estructura del Proyecto

```bash
generador-pdf/
└── pdf.py    # Generador de PDFs
```

---

## 📋 Requisitos

- Python 3.x
- Biblioteca: `fpdf`

Instalación:
```bash
pip install fpdf
```

---

## 🚀 Cómo ejecutar

1. Instala la dependencia `fpdf` si no la tienes
2. Ejecuta el archivo `pdf.py`
3. Se generará automáticamente un archivo `ejemplo.pdf`
4. Abre el PDF generado para ver el resultado

---

## 📸 Vista previa en consola

```plaintext
PDF generado exitosamente.
```

---

## 🔍 Funcionalidad

**Características del PDF generado:**
- **Título del documento**: "Mi Documento PDF"
- **Autor**: Configurable
- **Encabezado**: Título del documento centrado
- **Pie de página**: Número de página
- **Capítulos**: Múltiples secciones con títulos y contenido
- **Formato**: PDF estándar legible por cualquier visor

**Estructura del código:**
1. **Clase PDF**: Hereda de FPDF con métodos personalizados
2. **Header**: Muestra el título del documento
3. **Footer**: Muestra el número de página
4. **Chapter methods**: Para títulos y contenido de capítulos
5. **Main function**: Configura y genera el PDF

**Nota:** Puedes personalizar el contenido, agregar más capítulos, cambiar el título, autor e incluso incluir imágenes en el PDF.
