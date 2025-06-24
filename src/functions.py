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

def main_menu():
    """
    Muestra el menú principal del sistema y obtiene la opción seleccionada por el usuario.
    """
    # Mostrar menú principal y obtener opción del usuario
    main_answer = int(input("\n === Sistema de Gestión de Usuarios y Facturas === \n"
                                "1. Registrar nuevo usuario \n" 
                                "2. Buscar usuario \n"
                                "3. Crear factura \n"
                                "4. Mostrar todos los usuarios \n"
                                "5. Mostrar facturas de un usuario \n"
                                "6. Resumen financiero por usuario \n"
                                "7. Salir \n"
                                "Seleccione una opción: \t"
                            ))
                        
    return main_answer

def second_menu():
    """
    Muestra el menú de selección de usuario y obtiene la opción seleccionada.
    """
    # Mostrar menú de selección de usuario
    sencond_aswer = int(input("\n====== Sistema de Gestión de Usuarios y Facturas ======"
                                             "\n =============== Selección de usuario ===============\n"
                                    "1. Selección por usuario_id \n" 
                                    "2. Selección por email  \n"
                                    "Seleccione una opción: \t"))
                    
    return sencond_aswer

def trird_menu():
    """
    Muestra el menú de resumen financiero y obtiene la opción seleccionada.
    """
    # Mostrar menú de resumen financiero
    sencond_aswer= int(input("\n====== Sistema de Gestión de Usuarios y Facturas ======"
                                             "\n =============== Resumen financiero ===============\n"
                                    "1. Resumen financiero por usuario \n" 
                                    "2. Resumen general \n"
                                    "Seleccione una opción: \t"))
                    
    return sencond_aswer

def insert_user(conn, cursor):
    """
    Solicita los datos del usuario y los inserta en la base de datos.
    """
    print("\n==== Sistema de Gestión de Usuarios y Facturas ====\n"     
              "=============== Creación de usuario ===============\n")
    
    # Solicitar datos del usuario
    name = input("Nombre:   ")
    surname = input("Apellido:   ")
    email = input("Email:   ")
    phone = input("Telefono:   ")
    adress = input("Dirección:   ")
    
    # Insertar usuario en la base de datos
    cursor.execute("""
            INSERT INTO usuario (nombre, apellidos, email, telefono, direccion)
            VALUES (?, ?, ?, ?, ?)""", 
            (name, surname, email, phone, adress))
    
    # Confirmar cambios en la base de datos
    conn.commit()
    print("\nUsuario creado correctamente.\n")

def select_user_id(conn, cursor):
    """
    Busca y muestra los datos de un usuario por su ID.
    """
    print("" "\n==== Sistema de Gestión de Usuarios y Facturas ====\n"
            "= Sistema de seleccion de usuario por user_id =\n")
    
    # Obtener ID del usuario a buscar
    usuario_id =  int(input("Sobre que id_usuario quiere realizar la consulta:   "))
    
    # Ejecutar consulta SQL para buscar el usuario
    cursor.execute("""SELECT * FROM usuario WHERE usuario_id = ?"""
                    ,(usuario_id,))
    usuario = cursor.fetchone()
    
    # Mostrar resultado de la búsqueda
    if usuario:
        print(f"\n Usuario encontrado: \n {usuario} ")
    else:
        print("\nNo se encontró un usuario con ese ID.")

    conn.commit()

def select_user_email(conn, cursor):
    """
    Busca y muestra los datos de un usuario por su email.
    """
    print("" "\n==== Sistema de Gestión de Usuarios y Facturas ====\n"
                                "= Sistema de seleccion de usuario por email =\n")
    
    # Obtener email del usuario a buscar
    email =  input("Sobre que email quiere realizar la consulta:   ")
    
    # Ejecutar consulta SQL para buscar el usuario
    cursor.execute("""SELECT * FROM usuario WHERE email = ?"""
                                        ,(email,))
    email = cursor.fetchone()
    
    # Mostrar resultado de la búsqueda
    if email:
        print(f"\n Usuario encontrado: \n {email} ")
    else:
        print("\nNo se encontró un usuario con ese email.")

    conn.commit()



def insert_factura(conn, cursor):
    """
    Solicita los datos de una factura y la inserta en la base de datos.
    """
    print("\n==== Sistema de Gestión de Usuarios y Facturas ====\n"     
              "=============== Creación de factura ===============\n")
    
    # Solicitar datos de la factura
    user_id = int(input("A que usuario_id asigar la factura:   "))
    description = input("Descripción:   ")
    quantity = int(input("Monto total:   "))
    status = input("Estado ('Pendiente','Pagada', 'Cancelada'):   ")
    
    # Insertar factura en la base de datos
    cursor.execute("""
                INSERT INTO factura (usuario_id, descripcion, monto_total, estado)
                VALUES (?, ?, ?, ?)""",
                (user_id,description,quantity,status))
    conn.commit()
    print("\nFactura creada correctamente.")

def show_all_users(cursor):
    """
    Muestra todos los usuarios registrados en la base de datos.
    """

    print("\n==== Sistema de Gestión de Usuarios y Facturas ====\n"     
              "=============== Listado de usuarios ===============\n")
    
    # Ejecutar consulta SQL para obtener todos los usuarios
    cursor.execute("""SELECT * FROM usuario""")
    usuario = cursor.fetchall()
    
    # Mostrar encabezados de la tabla
    print("ID\tNombre\tApellidos\tEmail")
    print("-------------------------------------------------------------")
    
    # Mostrar cada usuario en la tabla
    for user in usuario:
        print(f"{user[0]}\t{user[1]}\t{user[2]}\t{user[3]}")
    print()

def user_bill_list(cursor):
    """
    Muestra todas las facturas asociadas a un usuario específico.
    """
    print("\n====== Sistema de Gestión de Usuarios y Facturas ======\n"
            "===== Sistema de seleccion de facturas por usuario ====\n")
    
    # Obtener ID del usuario para buscar sus facturas
    usuario_id = int(input("Sobre que usuario_id quiere realizar la consulta:   "))
    
    # Ejecutar consulta SQL para obtener las facturas del usuario
    cursor.execute("""SELECT * FROM factura WHERE usuario_id = ?""", (usuario_id,))
    facturas = cursor.fetchall()
            
    # Mostrar resultados de la búsqueda
    if not facturas:
        print("No se encontraron facturas para este usuario_id")
    else:
        print("\nFacturas encontradas:")
        for factura in facturas:
            print(f"ID: {factura[0]}, Fecha: {factura[2]}, Descripcion: {factura[3]}"+
            f", Monto: {factura[4]}, Estado: {factura[5]}")

def financial_user_sumary(cursor):
    """
    Muestra un resumen financiero por cada usuario, incluyendo el número de facturas y el total facturado.
    """
    # Ejecutar consulta SQL para obtener el resumen financiero por usuario
    cursor.execute("""
                        SELECT 
                            u.usuario_id,
                            u.nombre,
                            COUNT(f.numero_factura) as cantidad_facturas,
                            SUM(f.monto_total) as total_facturado
                        FROM usuario u
                        INNER JOIN factura f ON u.usuario_id = f.usuario_id
                        GROUP BY u.usuario_id, u.nombre
                        ORDER BY u.usuario_id
                        """)
    busquedas = cursor.fetchall()
             
    # Mostrar resumen para cada usuario               
    print("\n========= Resumen Financiero por Usuario ============\n "
                        "ID\tNombre\t\tFacturas\tTotal Facturado\n"
                        "-------------------------------------------------------------------")
    for busqueda in busquedas:
        print(f"{busqueda[0]}\t{busqueda[1]}\t\t{busqueda[2]}\t\t{busqueda[3]} €")

def financial_general_summary(cursor):
    """
    Muestra un resumen general de la base de datos, incluyendo:
    - Total de usuarios
    - Total de facturas emitidas
    - Ingresos totales
    - Ingresos recibidos
    - Ingresos pendientes
    """
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
    
    print(f"========= RESUMEN GENERAL ========= \n"
    f"Total usuarios: {total_usuarios}\n"
    f"Total facturas emitidas: {total_facturas}\n"
    f"Ingresos totales: {ingresos_totales:.2f} €\n"
    f"Ingresos recibidos: {ingresos_recibidos:.2f} €\n"
    f"Ingresos pendientes: {ingresos_pendientes:.2f} €\n")
