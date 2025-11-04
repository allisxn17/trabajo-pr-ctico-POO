import tkinter as tk
from tkinter import messagebox
from juego.juego import JuegoDetective

class JuegoGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Detective Psiquiátrico")
        self.juego = JuegoDetective()

        self.label_titulo = tk.Label(master, text="Detective Psiquiátrico", font=("Arial", 16))
        self.label_titulo.pack(pady=10)

        self.label_dia = tk.Label(master, text=f"Día actual: {self.juego.dia_actual}")
        self.label_dia.pack(pady=5)

        self.boton_investigar = tk.Button(master, text="Investigar", command=self.investigar)
        self.boton_investigar.pack(pady=5)

        self.boton_interrogar = tk.Button(master, text="Interrogar", command=self.interrogar)
        self.boton_interrogar.pack(pady=5)

        self.boton_saltar = tk.Button(master, text="Siguiente día", command=self.siguiente_dia)
        self.boton_saltar.pack(pady=10)

    def investigar(self):
        pista = self.juego.obtener_pista()
        messagebox.showinfo("Investigación", pista)

    def interrogar(self):
        resultado = self.juego.interrogar_personaje()
        messagebox.showinfo("Interrogatorio", resultado)

    def siguiente_dia(self):
        self.juego.avanzar_dia()
        self.label_dia.config(text=f"Día actual: {self.juego.dia_actual}")
        if self.juego.dia_actual > self.juego.dias_totales:
            messagebox.showinfo("Fin del juego", "El impostor se ha revelado.")
            self.master.quit()

def iniciar_gui():
    root = tk.Tk()
    app = JuegoGUI(root)
    root.mainloop()

if __name__ == "__main__":
    iniciar_gui()
