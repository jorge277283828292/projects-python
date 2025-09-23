# 💰 Gestor de Dinero en Python

Este proyecto es un sistema de gestión de dinero que permite manejar saldos, depósitos, gastos, historial y generar reportes.

---

## 🏦 ¿Qué hace este proyecto?

✅ Define un saldo inicial
✅ Permite depositar dinero
✅ Registra gastos y actualiza el saldo
✅ Consulta el saldo actual
✅ Muestra el historial de movimientos
✅ Genera gráficas de los datos
✅ Imprime reportes de facturas
✅ Menú interactivo para seleccionar opciones

---

## 📁 Estructura del Proyecto

```bash
gestor-dinero/
├── main.py                  # Archivo principal que ejecuta el programa
├── opciones.py              # Define el menú de opciones
├── dinero.py                # Maneja el saldo total e historial
├── dinero_inicial.py        # Función para definir saldo inicial
├── registro_gasto.py        # Registra gastos
├── consultar_saldo.py       # Consulta el saldo actual
├── depositar_dinero.py      # Deposita dinero
├── ver_grafica.py           # Genera gráficas
├── crear_factura.py         # Crea facturas
└── ver_historial.py         # Muestra historial de movimientos
```

---

## 🚀 Cómo ejecutar

1. Ejecuta el archivo `main.py`
2. Selecciona una opción del menú (1-8)
3. Sigue las instrucciones para cada función
4. Elige '8' para salir

---

## 📸 Vista previa en consola

```plaintext
1. Definir saldo inicial
2. Depositar dinero
3. Registrar gasto
4. Consultar saldo actual
5. Ver historial de movimientos
6. Ver gráficas
7. Imprimir reporte
8. Salir

Seleccione una opción: 1
Ingrese el saldo inicial: 1000
Saldo inicial definido: 1000

Seleccione una opción: 4
Saldo actual: 1000
