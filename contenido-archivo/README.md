# 📄 Gestor de Archivos de Texto

Este proyecto permite crear archivos de texto con contenido personalizado y abrirlos automáticamente en el editor predeterminado del sistema.

---

## ✍️ ¿Qué hace este proyecto?

✅ Solicita al usuario el contenido del archivo
✅ Crea un archivo de texto (`.txt`) con el nombre especificado
✅ Escribe el contenido proporcionado en el archivo
✅ Abre automáticamente el archivo en el editor de texto del sistema
✅ Utiliza programación orientada a objetos para la gestión de archivos

---

## 📁 Estructura del Proyecto

```bash
contenido-archivo/
├── archivo.py              # Script principal
└── crear_leer_archivo.py   # Clase para manejo de archivos
```

---

## 🚀 Cómo ejecutar

1. Ejecuta el archivo `archivo.py`
2. Ingresa el texto que deseas que contenga el archivo
3. El archivo se creará y abrirá automáticamente

---

## 📸 Vista previa en consola

```plaintext
Ingrese el texto que quiere que haya en el documento: Este es mi contenido personalizado
```

---

## 🔍 Funcionalidad

El programa:

1. **Solicita contenido**: Pide al usuario que ingrese el texto
2. **Crea el archivo**: Genera `archivo.txt` con el contenido
3. **Abre automáticamente**: Usa `os.startfile()` para abrir el archivo
4. **Orientado a objetos**: Utiliza una clase `Archivo` para la gestión

**Nota:** El archivo se abrirá con la aplicación predeterminada del sistema para archivos `.txt`.
