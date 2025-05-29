# 🏍️ Proyecto Catálogo de Motos

Este proyecto es un sistema web de gestión de un catálogo de motos desarrollado con **Python Flask** y **MySQL**, pensado para permitir a un administrador gestionar información detallada sobre diferentes modelos de motocicletas: especificaciones, rendimiento, mantenimiento e historial.

## 🚀 Tecnologías usadas

- Python 3
- Flask
- SQLAlchemy
- MySQL / HeidiSQL
- HTML5, CSS3
- Bootstrap
- Jinja2
- Git y GitHub

## 📂 Estructura del proyecto

Proyecto-Catalogo-de-Motos/

│
├── app/
│ ├── static/ # Archivos CSS, JS, imágenes
│ ├── templates/ # HTMLs con Jinja
│ ├── models.py # Modelos SQLAlchemy
│ ├── routes/ # Rutas organizadas por módulo
│ └── init.py # Inicialización del proyecto Flask
│
├── config.py # Configuraciones (BD, debug, etc)
├── requirements.txt # Dependencias del proyecto
├── README.md # Este archivo
└── run.py # Script principal para ejecutar la app


## 🧩 Funcionalidades

✅ Registrar motos con sus datos técnicos  
✅ Consultar historial de mantenimiento  
✅ Agregar especificaciones y rendimiento  
✅ Interfaz amigable para la gestión del catálogo  
✅ Sistema de roles: administrador, usuarios comunes (en desarrollo)

## 🛠️ Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Dreamzxd/Proyecto-Catalogo-de-Motos.git
   cd Proyecto-Catalogo-de-Motos

Crea un entorno virtual e instálalo:
   ```bash
   python -m venv venv
   source venv/bin/activate     # En Linux/macOS
   venv\Scripts\activate        # En Windows
   pip install -r requirements.txt


