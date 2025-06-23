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
    suername = input("Apellido:   ")
    email = input("Email:   ")
    phone = input("Telefono:   ")
    adress = input("Correo:   ")

    cursor.execute("""
            INSERT INTO usuario (nombre, apellidos, email, telefono, direccion)
            VALUES (?, ?, ?, ?, ?)""", 
            (name, suername, email, phone, adress))
    conn.commit()

def selec_user(conn, cursor):
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