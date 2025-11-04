import tkinter as tk
from gui.main_gui import JuegoGUI


def main():
    root = tk.Tk()
    gui = JuegoGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
