from gui import FacturasGUI
import tkinter as tk

def main():
    root = tk.Tk()
    app = FacturasGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()