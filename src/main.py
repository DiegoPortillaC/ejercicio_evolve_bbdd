from functions import *

def main ():
    
    conn, cursor = bd_connect()

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
                try:
                    sencond_aswer = second_menu()
                    if sencond_aswer == 1:
                        financial_user_sumary(cursor)
                    elif sencond_aswer ==2:
                        print("")
                    else:
                        print("Elegiste una opción no presente")     
                except ValueError:
                    print("Usaste un caracter erroneo")
            
            elif main_answer == 7:
                print("Hasta la proxima")
                conn.close()    
                break

            else:
                print("\nElegiste una opcion no presente")

        except ValueError:
            print("\nIntrodujiste un caracter no deseado.Inténtalo de nuevo.")


if __name__ == "__main__":
    main()