import tkinter as tk
from tkinter import messagebox, simpledialog
from Juego.Juego import JuegoDetective
from Juego.SaltoTemporal import SaltoTemporal


class JuegoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🧠 Juego del Impostor - Psiquiátrico ")
        self.juego = JuegoDetective()
        self.juego.inicializar_juego()
        self.salto_temporal = SaltoTemporal()
        self.crear_interfaz()
        self.investigado_hoy = False
        self.interrogado_hoy = False

    def crear_interfaz(self):
        from gui.widgets import crear_boton

        self.texto = tk.Text(self.root, width=80, height=25, wrap="word", bg="#f9f9f9")
        self.texto.pack(pady=10)

        self.boton_investigar = crear_boton(self.root, "🔍 Investigar", self.investigar)
        self.boton_interrogar = crear_boton(self.root, "❓ Interrogar", self.interrogar, "disabled")
        self.boton_siguiente = crear_boton(self.root, "⏭ Siguiente Día", self.siguiente_dia, "disabled")
        self.boton_tiempo = crear_boton(self.root, "⏳ Regresar en el tiempo", self.regresar_tiempo)

        self.mostrar_intro()

    def mostrar_intro(self):
        self.texto.insert(tk.END, "=== INVESTIGACIÓN PSIQUIÁTRICA ===\n")
        self.texto.insert(tk.END, "Hay 3 pacientes, pero uno es un impostor con graves problemas psicológicos.\n")
        self.texto.insert(tk.END, f"Tienes {self.juego.total_dias} días para descubrirlo.\n\n")
        self.mostrar_estado_dia()

    def mostrar_estado_dia(self):
        self.texto.insert(tk.END, f"\n🗓 DÍA {self.juego.dia_actual}\n{'=' * 40}\n")
        self.boton_investigar.config(state="normal")
        self.boton_interrogar.config(state="disabled")
        self.boton_siguiente.config(state="disabled")
        self.investigado_hoy = False
        self.interrogado_hoy = False
        self.salto_temporal.guardar_estado(self.juego)

    def investigar(self):
        try:
            ubicaciones = [u for u in self.juego.ubicaciones if u.tiene_pistas()]
            if not ubicaciones:
                raise ValueError("No quedan ubicaciones con pistas.")

            nombres = [str(u) for u in ubicaciones]
            eleccion = simpledialog.askinteger(
                "Investigar",
                "Elige una ubicación:\n" + "\n".join([f"{i + 1}. {n}" for i, n in enumerate(nombres)])
            )

            if eleccion is None:
                raise TypeError("No seleccionaste ninguna opción.")
            if eleccion < 1 or eleccion > len(ubicaciones):
                raise IndexError("Selección fuera del rango permitido.")

            ubicacion = ubicaciones[eleccion - 1]
            pista = ubicacion.obtener_pista()

            if pista:
                self.texto.insert(tk.END, f"\n🎯 {pista}\n")
                self.juego.pistas_encontradas.append(pista)
            else:
                self.texto.insert(tk.END, "\nNo encontraste nada nuevo aquí.\n")

            self.declaraciones(ubicacion.nombre)
            self.investigado_hoy = True
            self.boton_investigar.config(state="disabled")
            self.boton_interrogar.config(state="normal")

        except ValueError as e:
            messagebox.showinfo("Sin pistas", str(e))
        except (TypeError, IndexError) as e:
            messagebox.showwarning("Selección inválida", str(e))
        except Exception as e:
            messagebox.showerror("Error inesperado", f"Ocurrió un error: {e}")

    def declaraciones(self, ubicacion_nombre):
        self.texto.insert(tk.END, "\n📝 DECLARACIONES DEL DÍA:\n")
        for p in self.juego.personajes:
            declaracion = p.declarar_dia(self.juego.pistas_encontradas, ubicacion_nombre)
            p.agregar_comportamiento(declaracion)
            self.texto.insert(tk.END, f"- {p.get_nombre()}: {declaracion}\n")

    def interrogar(self):
        try:
            if not self.investigado_hoy:
                raise PermissionError("Debes investigar antes de interrogar.")

            nombres = [p.get_nombre() for p in self.juego.personajes]
            eleccion = simpledialog.askinteger(
                "Interrogatorio",
                "¿A quién deseas interrogar?\n" + "\n".join([f"{i + 1}. {n}" for i, n in enumerate(nombres)]) +
                "\n4. No interrogar a nadie"
            )

            if eleccion is None:
                raise TypeError("No seleccionaste ninguna opción.")

            if eleccion in [1, 2, 3]:
                personaje = self.juego.personajes[eleccion - 1]
                respuesta = personaje.interrogar(self.juego.pistas_encontradas)
                self.texto.insert(tk.END, f"\n❓ {personaje.get_nombre()}: \"{respuesta}\"\n")
            else:
                self.texto.insert(tk.END, "\nNo interrogarás a nadie hoy.\n")

            self.interrogado_hoy = True
            self.boton_interrogar.config(state="disabled")
            self.boton_siguiente.config(state="normal")

        except PermissionError as e:
            messagebox.showwarning("Acción no permitida", str(e))
        except TypeError as e:
            messagebox.showwarning("Selección inválida", str(e))
        except Exception as e:
            messagebox.showerror("Error inesperado", f"Ocurrió un error: {e}")

    def siguiente_dia(self):
        if not self.interrogado_hoy:
            messagebox.showwarning("Acción no permitida",
                                   "Debes interrogar a alguien (o decidir no hacerlo) antes de pasar al siguiente día.")
            return

        self.juego.dia_actual += 1
        if self.juego.dia_actual > self.juego.total_dias:
            self.fase_acusacion()
        else:
            self.mostrar_estado_dia()

    def fase_acusacion(self):
        try:
            self.texto.insert(tk.END, "\n⏰ FASE FINAL - ACUSACIÓN\n")
            self.texto.insert(tk.END, "\n📊 Pistas encontradas:\n")

            for i, pista in enumerate(self.juego.pistas_encontradas, 1):
                self.texto.insert(tk.END, f"{i}. {pista}\n")

            nombres = [p.get_nombre() for p in self.juego.personajes]
            eleccion = simpledialog.askinteger(
                "Acusación",
                "¿Quién es el impostor?\n" + "\n".join([f"{i + 1}. {n}" for i, n in enumerate(nombres)])
            )

            if eleccion is None:
                raise TypeError("No seleccionaste ninguna opción.")
            if eleccion < 1 or eleccion > len(self.juego.personajes):
                raise IndexError("Selección fuera del rango permitido.")

            elegido = self.juego.personajes[eleccion - 1]
            if elegido.es_impostor():
                messagebox.showinfo("🎉 ¡Correcto!", f"{elegido.get_nombre()} era el impostor.")
            else:
                messagebox.showerror("💀 Incorrecto",
                                     f"{elegido.get_nombre()} era inocente.\nEl impostor era {self.juego.impostor_real.get_nombre()}.")

            self.root.destroy()

        except (TypeError, IndexError) as e:
            messagebox.showwarning("Selección inválida", str(e))
        except Exception as e:
            messagebox.showerror("Error inesperado", f"Ocurrió un error: {e}")

    def regresar_tiempo(self):
        if self.salto_temporal.regresar_en_el_tiempo(self.juego):
            self.texto.insert(tk.END, "\n⏳ ¡Has regresado en el tiempo! El día vuelve a su estado anterior.\n")
            self.mostrar_estado_dia()
            self.boton_tiempo.config(state="disabled")
        else:
            messagebox.showinfo("No disponible", "Ya usaste tu poder de regresar en el tiempo.")
