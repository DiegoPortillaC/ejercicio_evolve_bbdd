import tkinter as tk
from tkinter import ttk, messagebox
import functions as func

class FacturasGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de Usuarios y Facturas")
        self.root.geometry("800x600")
        
        # Conectar a la base de datos
        self.conn, self.cursor = func.bd_connect()
        
        # Crear menú principal
        self.create_main_menu()
        
        # Crear frame para mostrar resultados
        self.result_frame = ttk.Frame(self.root)
        self.result_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Crear scrollbar para los resultados
        self.scrollbar = ttk.Scrollbar(self.result_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Crear text widget para mostrar resultados
        self.results_text = tk.Text(self.result_frame, wrap=tk.WORD, yscrollcommand=self.scrollbar.set)
        self.results_text.pack(fill=tk.BOTH, expand=True)
        self.scrollbar.config(command=self.results_text.yview)

    def create_main_menu(self):
        menu_frame = ttk.LabelFrame(self.root, text="Menú Principal", padding="10")
        menu_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Botones del menú principal
        buttons = [
            ("Registrar nuevo usuario", self.registrar_usuario),
            ("Buscar usuario", self.buscar_usuario),
            ("Crear factura", self.crear_factura),
            ("Mostrar todos los usuarios", self.mostrar_usuarios),
            ("Mostrar facturas de un usuario", self.mostrar_facturas_usuario),
            ("Resumen financiero por usuario", self.resumen_financiero_usuario),
            ("Resumen general", self.resumen_general)
        ]
        
        for text, command in buttons:
            btn = ttk.Button(menu_frame, text=text, command=command)
            btn.pack(fill=tk.X, pady=2)

    def clear_results(self):
        self.results_text.delete(1.0, tk.END)

    def registrar_usuario(self):
        def submit():
            try:
                success, message = func.insert_user(
                    self.conn, self.cursor,
                    entries["Nombre"].get(),
                    entries["Apellido"].get(),
                    entries["Email"].get(),
                    entries["Teléfono"].get(),
                    entries["Dirección"].get()
                )
                if success:
                    messagebox.showinfo("Éxito", message)
                else:
                    messagebox.showerror("Error", message)
            except Exception as e:
                messagebox.showerror("Error", str(e))
            finally:
                dialog.destroy()
        
        dialog = tk.Toplevel(self.root)
        dialog.title("Registrar Usuario")
        dialog.geometry("400x300")
        
        # Campos de entrada
        fields = ["Nombre", "Apellido", "Email", "Teléfono", "Dirección"]
        entries = {}
        
        for i, field in enumerate(fields):
            ttk.Label(dialog, text=field).grid(row=i, column=0, padx=5, pady=5)
            entries[field] = ttk.Entry(dialog)
            entries[field].grid(row=i, column=1, padx=5, pady=5)
        
        ttk.Button(dialog, text="Registrar", command=submit).grid(row=len(fields), column=0, columnspan=2, pady=10)

    def buscar_usuario(self):
        def submit():
            self.clear_results()
            try:
                if var.get() == 1:
                    user_id = id_entry.get()
                    usuario = func.select_user_id(self.conn, self.cursor, int(user_id))
                    if usuario:
                        self.results_text.insert(tk.END, f"Usuario encontrado:\n")
                        self.results_text.insert(tk.END, f"ID: {usuario[0]}\n")
                        self.results_text.insert(tk.END, f"Nombre: {usuario[1]}\n")
                        self.results_text.insert(tk.END, f"Apellidos: {usuario[2]}\n")
                        self.results_text.insert(tk.END, f"Email: {usuario[3]}\n")
                        self.results_text.insert(tk.END, f"Teléfono: {usuario[4]}\n")
                        self.results_text.insert(tk.END, f"Dirección: {usuario[5]}\n")
                    else:
                        messagebox.showinfo("No encontrado", "No se encontró un usuario con ese ID")
                else:
                    email = email_entry.get()
                    usuario = func.select_user_email(self.conn, self.cursor, email)
                    if usuario:
                        self.results_text.insert(tk.END, f"Usuario encontrado:\n")
                        self.results_text.insert(tk.END, f"ID: {usuario[0]}\n")
                        self.results_text.insert(tk.END, f"Nombre: {usuario[1]}\n")
                        self.results_text.insert(tk.END, f"Apellidos: {usuario[2]}\n")
                        self.results_text.insert(tk.END, f"Email: {usuario[3]}\n")
                        self.results_text.insert(tk.END, f"Teléfono: {usuario[4]}\n")
                        self.results_text.insert(tk.END, f"Dirección: {usuario[5]}\n")
                    else:
                        messagebox.showinfo("No encontrado", "No se encontró un usuario con ese email")
            except Exception as e:
                messagebox.showerror("Error", str(e))
            finally:
                dialog.destroy()
        
        dialog = tk.Toplevel(self.root)
        dialog.title("Buscar Usuario")
        dialog.geometry("300x200")
        
        var = tk.IntVar()
        ttk.Radiobutton(dialog, text="Buscar por ID", variable=var, value=1).pack(pady=5)
        ttk.Radiobutton(dialog, text="Buscar por Email", variable=var, value=2).pack(pady=5)
        
        id_frame = ttk.Frame(dialog)
        id_frame.pack(pady=5)
        ttk.Label(id_frame, text="ID Usuario:").pack(side=tk.LEFT, padx=5)
        id_entry = ttk.Entry(id_frame)
        id_entry.pack(side=tk.LEFT, padx=5)
        
        email_frame = ttk.Frame(dialog)
        email_frame.pack(pady=5)
        ttk.Label(email_frame, text="Email:").pack(side=tk.LEFT, padx=5)
        email_entry = ttk.Entry(email_frame)
        email_entry.pack(side=tk.LEFT, padx=5)
        
        ttk.Button(dialog, text="Buscar", command=submit).pack(pady=10)

    def crear_factura(self):
        def submit():
            try:
                success, message = func.insert_factura(
                    self.conn, self.cursor,
                    int(entries["ID Usuario"].get()),
                    entries["Descripción"].get(),
                    float(entries["Monto Total"].get()),
                    entries["Estado"].get()
                )
                if success:
                    messagebox.showinfo("Éxito", message)
                else:
                    messagebox.showerror("Error", message)
            except Exception as e:
                messagebox.showerror("Error", str(e))
            finally:
                dialog.destroy()

        dialog = tk.Toplevel(self.root)
        dialog.title("Crear Factura")
        dialog.geometry("400x200")

        # Campos de entrada
        fields = ["ID Usuario", "Descripción", "Monto Total", "Estado"]
        entries = {}

        for i, field in enumerate(fields):
            ttk.Label(dialog, text=field).grid(row=i, column=0, padx=5, pady=5)
            if field == "Estado":
                combo = ttk.Combobox(dialog, values=["Pagada", "Cancelada", "Pendiente"], state="readonly")
                combo.grid(row=i, column=1, padx=5, pady=5)
                combo.current(0)  # Seleccionar la primera opción por defecto
                entries[field] = combo
            else:
                entry = ttk.Entry(dialog)
                entry.grid(row=i, column=1, padx=5, pady=5)
                entries[field] = entry

        ttk.Button(dialog, text="Crear", command=submit).grid(row=len(fields), column=0, columnspan=2, pady=10)


    def mostrar_usuarios(self):
        self.clear_results()
        try:
            usuarios = func.show_all_users(self.cursor)
            if usuarios:
                self.results_text.insert(tk.END, "ID\tNombre\t\tApellidos\t\t\tEmail\n")
                self.results_text.insert(tk.END, "---------------------------------------------------------------------------------------\n")
                for user in usuarios:
                    self.results_text.insert(tk.END, f"{user[0]}\t{user[1]}\t\t{user[2]}\t\t\t{user[3]}\n")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def mostrar_facturas_usuario(self):
        def submit():
            self.clear_results()
            try:
                user_id = int(user_id_entry.get())
                facturas = func.user_bill_list(self.cursor, user_id)
                if facturas:
                    self.results_text.insert(tk.END, "Facturas encontradas:\n")
                    self.results_text.insert(tk.END, "ID\tFecha\tDescripción\tMonto\tEstado\n")
                    self.results_text.insert(tk.END, "-------------------------------------------------------------\n")
                    for factura in facturas:
                        self.results_text.insert(tk.END, f"{factura[0]}\t{factura[2]}\t{factura[3]}\t{factura[4]}\t{factura[5]}\n")
                else:
                    messagebox.showinfo("No encontrado", "No se encontraron facturas para este usuario")
            except Exception as e:
                messagebox.showerror("Error", str(e))
            finally:
                dialog.destroy()
        
        dialog = tk.Toplevel(self.root)
        dialog.title("Facturas por Usuario")
        dialog.geometry("400x150")
        
        ttk.Label(dialog, text="ID Usuario:").pack(pady=5)
        user_id_entry = ttk.Entry(dialog)
        user_id_entry.pack(pady=5)
        ttk.Button(dialog, text="Buscar", command=submit).pack(pady=10)

    def resumen_financiero_usuario(self):
        def submit():
            self.clear_results()
            try:
                user_id = int(user_id_entry.get())
                resumen = func.financial_user_sumary(self.cursor, user_id)
                if resumen:
                    self.results_text.insert(tk.END, "========= Resumen Financiero por Usuario ============\n")
                    self.results_text.insert(tk.END, f"ID: {resumen[0]}\n")
                    self.results_text.insert(tk.END, f"Nombre: {resumen[1]}\n")
                    self.results_text.insert(tk.END, f"Facturas: {resumen[2]}\n")
                    self.results_text.insert(tk.END, f"Total Facturado: {resumen[3]} €\n")
                else:
                    messagebox.showinfo("No encontrado", "No se encontró información financiera para este usuario")
            except Exception as e:
                messagebox.showerror("Error", str(e))
            finally:
                dialog.destroy()
        
        dialog = tk.Toplevel(self.root)
        dialog.title("Resumen Financiero")
        dialog.geometry("320x120")
        
        ttk.Label(dialog, text="ID Usuario:").pack(pady=5)
        user_id_entry = ttk.Entry(dialog)
        user_id_entry.pack(pady=5)
        ttk.Button(dialog, text="Generar Resumen", command=submit).pack(pady=10)

    def resumen_general(self):
        self.clear_results()
        try:
            resumen = func.financial_general_summary(self.cursor)
            if resumen:
                self.results_text.insert(tk.END, "========= RESUMEN GENERAL =========\n")
                self.results_text.insert(tk.END, f"Total usuarios: {resumen['total_usuarios']}\n")
                self.results_text.insert(tk.END, f"Total facturas emitidas: {resumen['total_facturas']}\n")
                self.results_text.insert(tk.END, f"Ingresos totales: {resumen['ingresos_totales']:.2f} €\n")
                self.results_text.insert(tk.END, f"Ingresos recibidos: {resumen['ingresos_recibidos']:.2f} €\n")
                self.results_text.insert(tk.END, f"Ingresos pendientes: {resumen['ingresos_pendientes']:.2f} €\n")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = FacturasGUI(root)
    root.mainloop()
