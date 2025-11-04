import sys, os
import tkinter as tk
# Asegurar que la carpeta raíz esté en el path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from gui.main_gui import JuegoGUI

def main():
    root = tk.Tk()
    gui = JuegoGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
