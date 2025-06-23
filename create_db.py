import sqlite3

def create_database():
    conn = sqlite3.connect('ejercicio_evolve.db')
    cursor = conn.cursor()
    
    # Leer el contenido del script SQL
    with open('script.sql', 'r', encoding='utf-8') as f:
        sql_script = f.read()
    
    # Ejecutar el script
    cursor.executescript(sql_script)
    
    # Confirmar los cambios
    conn.commit()
    
    # Cerrar la conexión
    conn.close()
    
    print("Base de datos creada exitosamente")

if __name__ == "__main__":
    create_database()
