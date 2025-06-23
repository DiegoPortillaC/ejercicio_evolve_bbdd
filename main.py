import sqlite3
from functions import *

conn = sqlite3.connect("ejercicio_evolve.db")
conn.execute("PRAGMA foreign_keys = ON;")
cursor = conn.cursor()



while True:
    try:
        main_answer = main_menu()
        if main_answer == 1:
            #insert usuario
            insert_user(conn, cursor)

        if main_answer == 2:
            #select usuario por id
            selec_user(conn, cursor)

        if main_answer == 3:
            #insert factura
            print("Hasta la proxima")    
        if main_answer == 4:
            #select * usuarios
            print("Hasta la proxima")    
        if main_answer == 5:
            #select * from facturas where user_id = X
            print("Hasta la proxima")    
        if main_answer == 6:
            #select * from facturas group by usuario + sumatorios de cantidades
            print("Hasta la proxima")    
        if main_answer == 7:
            print("Hasta la proxima")    
            break
        else:
            print("\nElegiste una opcion no presnte")
    except ValueError:
        print("\nIntrodujiste un caracter no deseado")