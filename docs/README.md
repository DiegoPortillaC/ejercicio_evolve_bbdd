# 📚 Sistema de Gestión de Usuarios

Sistema de gestión de usuarios con base de datos SQLite y una interfaz de línea de comandos interactiva.

## 📋 Estructura del Proyecto

```
ejercicio_evolve_bbdd/
├── database/
│   ├── create_db.py   # Script para crear la base de datos
│   └── __pycache__    # Archivos compilados de Python
├── docs/
│   └── README.md      # Documentación del proyecto
├── src/
    ├── main.py        # Punto de entrada de la aplicación
    └── functions.py   # Funciones principales del sistema

```

## 📋 Requisitos

- Python 3.8 o superior
- sqlite3 (incluido con Python por defecto)

## 🚀 Instalación y Ejecución

1. **Clonar el repositorio**
```bash
git clone https://github.com/DiegoPortillaC/ejercicio_evolve_bbdd.git
cd ejercicio_evolve_bbdd
```

2. **Crear la base de datos**
```bash
python database/create_db.py
```

3. **Ejecutar la aplicación**
```bash
python src/main.py
```

## 🛠️ Funcionalidades

- 📝 Registro de nuevos usuarios
- 🔍 Consulta de usuarios existentes por ID o email
- 🔄 Interfaz de usuario interactiva
- 📝 Validación de datos de entrada
- 🔐 Almacenamiento seguro en SQLite

## 📝 Notas

- 🔐 Asegúrate de tener los permisos necesarios para crear archivos en el directorio donde clonas el repositorio.
- 💾 La base de datos SQLite se creará automáticamente en el directorio raíz del proyecto.
- 📱 La aplicación utiliza un menú interactivo con opciones claras y fáciles de usar.
- 🔄 El sistema de validación asegura la integridad de los datos ingresados.
