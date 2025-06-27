import sqlite3

def bd_connect():
    """
    Establece la conexión a la base de datos SQLite y habilita las claves foráneas.
    """
    # Crear conexión a la base de datos
    conn = sqlite3.connect("ejercicio_evolve.db")
    
    # Habilitar claves foráneas para mantener la integridad referencial
    conn.execute("PRAGMA foreign_keys = ON;")
    
    # Crear cursor para ejecutar consultas
    cursor = conn.cursor()
    
    return conn,cursor

def insert_user(conn, cursor, name, surname, email, phone, address):
    """
    Inserta un nuevo usuario en la base de datos.
    """
    try:
        cursor.execute("""
            INSERT INTO usuario (nombre, apellidos, email, telefono, direccion)
            VALUES (?, ?, ?, ?, ?)""", 
            (name, surname, email, phone, address))
        conn.commit()
        return True, "Usuario creado correctamente"
    except Exception as e:
        return False, str(e)

def select_user_id(conn, cursor, user_id):
    """
    Busca un usuario por su ID.
    """
    try:
        cursor.execute("""SELECT * FROM usuario WHERE usuario_id = ?""", (user_id,))
        usuario = cursor.fetchone()
        return usuario
    except Exception as e:
        return None

def select_user_email(conn, cursor, email):
    """
    Busca un usuario por su email.
    """
    try:
        cursor.execute("""SELECT * FROM usuario WHERE email = ?""", (email,))
        usuario = cursor.fetchone()
        return usuario
    except Exception as e:
        return None



def insert_factura(conn, cursor, user_id, description, quantity, status):
    """
    Inserta una nueva factura en la base de datos.
    """
    try:
        cursor.execute("""
                INSERT INTO factura (usuario_id, descripcion, monto_total, estado)
                VALUES (?, ?, ?, ?)""",
                (user_id, description, quantity, status))
        conn.commit()
        return True, "Factura creada correctamente"
    except Exception as e:
        return False, str(e)

def show_all_users(cursor):
    """
    Obtiene todos los usuarios registrados en la base de datos.
    """
    try:
        cursor.execute("""SELECT * FROM usuario""")
        usuarios = cursor.fetchall()
        return usuarios
    except Exception as e:
        return None

def user_bill_list(cursor, user_id):
    """
    Obtiene todas las facturas asociadas a un usuario específico.
    """
    try:
        cursor.execute("""SELECT * FROM factura WHERE usuario_id = ?""", (user_id,))
        facturas = cursor.fetchall()
        return facturas
    except Exception as e:
        return None

def financial_user_sumary(cursor, user_id):
    """
    Obtiene un resumen financiero para un usuario específico.
    """
    try:
        cursor.execute("""
                        SELECT 
                            u.usuario_id,
                            u.nombre,
                            COUNT(f.numero_factura) as cantidad_facturas,
                            SUM(f.monto_total) as total_facturado
                        FROM usuario u
                        INNER JOIN factura f ON u.usuario_id = f.usuario_id
                        WHERE u.usuario_id = ?
                        GROUP BY u.usuario_id, u.nombre
                        ORDER BY u.usuario_id
                        """, (user_id,))
        resumen = cursor.fetchone()
        return resumen
    except Exception as e:
        return None

def financial_general_summary(cursor):
    """
    Obtiene un resumen general de la base de datos.
    """
    try:
        # Obtener total de usuarios
        cursor.execute("SELECT COUNT(*) FROM usuario")
        total_usuarios = cursor.fetchone()[0]
        
        # Obtener total de facturas
        cursor.execute("SELECT COUNT(*) FROM factura")
        total_facturas = cursor.fetchone()[0]
        
        # Obtener ingresos totales
        cursor.execute("SELECT SUM(monto_total) FROM factura")
        ingresos_totales = cursor.fetchone()[0] or 0
        
        # Obtener ingresos recibidos
        cursor.execute("SELECT SUM(monto_total) FROM factura WHERE estado = 'Pagada'")
        ingresos_recibidos = cursor.fetchone()[0] or 0
        
        # Calcular ingresos pendientes
        ingresos_pendientes = ingresos_totales - ingresos_recibidos
        
        return {
            'total_usuarios': total_usuarios,
            'total_facturas': total_facturas,
            'ingresos_totales': ingresos_totales,
            'ingresos_recibidos': ingresos_recibidos,
            'ingresos_pendientes': ingresos_pendientes
        }
    except Exception as e:
        return None
