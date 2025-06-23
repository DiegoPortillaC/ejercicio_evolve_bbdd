import sqlite3
from functions import *

conn = sqlite3.connect("ejercicio_evolve.db")
conn.execute("PRAGMA foreign_keys = ON;")
cursor = conn.cursor()



while True:
    try:
        main_answer = main_menu()
        if main_answer == 1:
            insert_user(conn, cursor)

        elif main_answer == 2:
            select_user(conn, cursor)

        elif main_answer == 3:
            insert_factura(conn, cursor)

        elif main_answer == 4:
            show_all_users(cursor)
        
        elif main_answer == 5:
            user_bill_list(cursor)
          
        elif main_answer == 6:
            #select * from facturas group by usuario + sumatorios de cantidades
            print("Hasta la proxima")  
          
        elif main_answer == 7:
            print("Hasta la proxima")    
            break

        else:
            print("\nElegiste una opcion no presente")

    except ValueError:
        print("\nIntrodujiste un caracter no deseado")