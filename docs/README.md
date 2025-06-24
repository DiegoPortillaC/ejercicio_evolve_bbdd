## 📋 Estructura del Proyecto

```
├── database/          # Scripts para crear la base de datos
├── src/              # Código fuente principal
├── ejercicio_evolve.db  # Base de datos SQLite
└── README.md         # Documentación del proyecto
```

## 📋 Requisitos

- Python 3.8 o superior
- sqlite3 (incluido con Python)

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

## 📝 Notas

- 🔐 Asegúrate de tener los permisos necesarios para crear archivos en el directorio donde clonas el repositorio.
- 💾 La base de datos se creará automáticamente al ejecutar `create_db.py`.
- 📱 La aplicación utiliza un menú interactivo para facilitar la gestión de usuarios.
