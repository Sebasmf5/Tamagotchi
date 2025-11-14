# Tamagotchi - Proyecto de Modelamiento y Simulación

## Descripción
Este proyecto consiste en un **Tamagotchi virtual** desarrollado en Python, como parte de un ejercicio de **modelamiento y simulación**.  
El usuario puede interactuar con su mascota, cuidar sus necesidades y observar cómo sus acciones afectan el estado del Tamagotchi a lo largo del tiempo.

El proyecto incluye animaciones, eventos aleatorios y un sistema de estadísticas que simula la **salud**, **felicidad** y **hambre** de la mascota.

## Características
- Mascota virtual con estados variables (salud, felicidad, hambre).
- Animaciones básicas para distintas acciones.
- Eventos aleatorios que afectan al Tamagotchi.
- Interfaz interactiva con botones y paneles de información.
- Registro visual de las acciones y sus efectos sobre la mascota.

## Requisitos
- Python 3.9 o superior
- Librerías:
  - `pygame`

> Se recomienda usar un entorno virtual para instalar las dependencias.

## Instalación

1. Clona el repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_PROYECTO>
    python -m venv venv
# Linux/macOS
    source venv/bin/activate
# Windows
    venv\Scripts\activate
    
    pip install pygame
    Tamagotchi/
    │
    ├─ main.py                  # Archivo principal del juego
    ├─ Estados.py               # Definición de estados y sprites del Tamagotchi
    ├─ UIManager.py             # Gestión de la interfaz y botones
    ├─ abs_path.py              # Función para rutas absolutas de archivos
    ├─ assets/                  # Carpeta con imágenes, sprites y fuentes
    └─ README.md
    python main.py
