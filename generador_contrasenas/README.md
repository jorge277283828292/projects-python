# 🔐 Generador de Contraseñas Seguras

Este proyecto genera contraseñas seguras y personalizables con diferentes tipos de caracteres según las preferencias del usuario.

---

## 🛡️ ¿Qué hace este proyecto?

✅ Genera contraseñas con longitud personalizable
✅ Permite elegir entre letras, números y símbolos
✅ Utiliza el módulo `random` para aleatoriedad
✅ Incluye validación de entrada del usuario
✅ Genera contraseñas seguras y únicas

---

## 📁 Estructura del Proyecto

```bash
generador_contrasenas/
└── Generador_de_Contraseñas.py    # Generador de contraseñas
```

---

## 🚀 Cómo ejecutar

1. Ejecuta el archivo `Generador_de_Contraseñas.py`
2. Ingresa la longitud deseada para la contraseña
3. Selecciona los tipos de caracteres a incluir:
   - 1: Letras (mayúsculas y minúsculas)
   - 2: Números
   - 3: Símbolos
   - 4: Generar contraseña
4. Obtén tu contraseña segura generada

---

## 📸 Vista previa en consola

```plaintext
Bienvenido aqui puedes generar tu constraseña
Dame la longitud que desea que tenga la contraseña: 12

1. Letras
2. Numeros
3. Simbolos
4. Generar Contraseña

Elige una opcion: 1
Elige una opcion: 2
Elige una opcion: 3
Elige una opcion: 4

🔐 Tu contraseña generada es:, A5k#9mZ2@1pL
```

---

## 🔍 Funcionalidad

**Caracteres disponibles:**
- **Letras**: `s.ascii_letters` (a-z, A-Z)
- **Números**: `s.digits` (0-9)
- **Símbolos**: `s.punctuation` (!@#$%^&*(), etc.)

**Proceso de generación:**
1. **Selecciona tipos**: Elige qué caracteres incluir
2. **Longitud mínima**: Asegura al menos un carácter de cada tipo seleccionado
3. **Rellena longitud**: Completa con caracteres aleatorios hasta la longitud deseada
4. **Mezcla**: Usa `shuffle()` para randomizar el orden
5. **Genera**: Une todos los caracteres en una cadena final

