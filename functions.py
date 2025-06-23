import sqlite3


def main_menu():
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

def insert_user(conn, cursor):
    print("\n==== Sistema de Gestión de Usuarios y Facturas ====\n"     
              "=============== Creación de usuario ===============\n")
    name = input("Nombre:   ")
    surname = input("Apellido:   ")
    email = input("Email:   ")
    phone = input("Telefono:   ")
    adress = input("Dirección:   ")

    cursor.execute("""
            INSERT INTO usuario (nombre, apellidos, email, telefono, direccion)
            VALUES (?, ?, ?, ?, ?)""", 
            (name, surname, email, phone, adress))
    conn.commit()
    print("\nUsuario creado correctamente.")

def select_user(conn, cursor):
    print("" "\n==== Sistema de Gestión de Usuarios y Facturas ====\n"
            "========= Sistema de seleccion de usuario =========\n")
    usuario_id =  int(input("Sobre que id_usuario quiere realizar la consulta:   "))
    cursor.execute("""SELECT * FROM usuario WHERE usuario_id = ?"""
                    ,(usuario_id,))
    usuario = cursor.fetchone()
    if usuario:
        print(f"\n Usuario encontrado: \n {usuario} ")
    else:
        print("\nNo se encontró un usuario con ese ID.")

    conn.commit()

def insert_factura(conn, cursor):
    print("\n==== Sistema de Gestión de Usuarios y Facturas ====\n"     
              "=============== Creación de factura ===============\n")
    user_id = int(input("A que usuario_id asigar la factura:   "))
    description = input("Descripción:   ")
    quantity = int(input("Monto total:   "))
    estado = input("Estado ('Pendiente','Pagada', 'Cancelada'):   ")
    cursor.execute("""
                INSERT INTO factura (usuario_id, descripcion, monto_total, estado)
                VALUES (?, ?, ?, ?)""",
                (user_id,description,quantity,estado))
    conn.commit()
    print("\nFactura creada correctamente.")

def show_all_users(cursor):
    print("\n==== Sistema de Gestión de Usuarios y Facturas ====\n"     
              "=============== Listado de usuarios ===============\n")
    cursor.execute("""SELECT * FROM usuario""")
    usuario = cursor.fetchall()
    print("ID\tNombre\t\tEmail\t\tTeléfono")
    print("-------------------------------------------------------------")
    for user in usuario:
        print(f"{user[0]}\t{user[1]}\t{user[2]}\t{user[3]}")
    print()

def user_bill_list(cursor):
    print("" "\n====== Sistema de Gestión de Usuarios y Facturas ======\n"
            "===== Sistema de seleccion de facturas por usuario ====\n")
    usuario_id = int(input("Sobre que usuario_id quiere realizar la consulta:   "))
    cursor.execute("""SELECT * FROM factura WHERE usuario_id = ?""", (usuario_id,))
    facturas = cursor.fetchall()
            
    if not facturas:
        print("No se encontraron facturas para este usuario_id")
    else:
        print("\nFacturas encontradas:")
        for factura in facturas:
            print(f"ID: {factura[0]}, Fecha: {factura[2]}, Descripcion: {factura[3]}"+
            ", Monto: {factura[4]}, Estado: {factura[5]}")