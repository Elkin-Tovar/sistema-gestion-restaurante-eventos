# Sistema de Gestión de Restaurante - Módulo de Eventos y Roles

Desarrollado por **Elkin Tovar**

## 🎯 Propósito del Proyecto
Esta fase del sistema evoluciona la aplicación de escritorio hacia un modelo interactivo basado en el **manejo avanzado de eventos en Tkinter**, integrando la gestión administrativa de usuarios (CRUD), el control de acceso por roles y atajos de teclado sin alterar la arquitectura modular ni la separación de responsabilidades.

## 📈 Características y Módulos Principales
* **Gestión de Usuarios (CRUD):** Permite registrar, consultar, actualizar y eliminar usuarios de manera dinámica desde la interfaz gráfica.
* **Control de Acceso Basado en Roles:** Integración del atributo `rol` en el modelo `Usuario` (`Administrador`, `Empleado`, `Cliente`), restringiendo las operaciones administrativas y de inventario de forma lógica y segura.
* **Manejo Avanzado de Eventos y Callbacks:**
  * `<<TreeviewSelect>>` mediante `bind()` para la carga automática de datos desde las tablas hacia los formularios.
  * `<Return>` como atajo de teclado para confirmar registros de usuarios de forma rápida.
  * `<Escape>` para limpiar formularios y cancelar selecciones activas.
  * `<<ComboboxSelected>>` para la interacción con selectores de roles y opciones.
  * Uso de `command=` para los botones de acción principal.
* **Persistencia Centralizada:** Almacenamiento estructurado en archivos en formato JSON (`productos.json`, `usuarios.json`, `ventas.json`) gestionados exclusivamente a través de la capa de servicios.

## 🏗️ Estructura del Repositorio
```text
restaurante-gestion-eventos/
│
├── assets/             # Recursos visuales, logotipo institucional e íconos
├── datos/              # Archivos de persistencia JSON
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/            # Clases de entidad (Producto, Usuario, Venta)
├── servicios/          # Capa de lógica de negocio y gestión de archivos
├── ui/                 # Componentes gráficos (LoginView, MainView)
├── main.py             # Punto de entrada principal de la aplicación
└── README.md

Pasos para Ejecutar la Aplicación
Asegúrate de tener instalado Python 3.x en tu equipo.

Clona o descarga este repositorio en tu máquina local.

Abre una terminal y ubícate en la carpeta raíz del proyecto.

Ejecuta el sistema con el siguiente comando:

Bash
python main.py
🔑 Credenciales de Acceso por Defecto
Administrador (Acceso Total):

Correo: admin | Contraseña: 1234

(O correo: elkin@restaurante.com | Contraseña: 123456)

Empleados y Clientes:

Gestionados y almacenados de manera persistente en datos/usuarios.json.
