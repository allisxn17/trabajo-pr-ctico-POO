import random
import tkinter as tk
from tkinter import messagebox, simpledialog
from abc import ABC, abstractmethod

class Jugador(ABC):
    def __init__(self, nombre):
        self._nombre = nombre
        self._es_impostor = False
        self._comportamientos_dia = []

    @abstractmethod
    def get_nombre(self):
        pass

    @abstractmethod
    def es_impostor(self):
        pass

    @abstractmethod
    def set_impostor(self, valor):
        pass

    @abstractmethod
    def agregar_comportamiento(self, comportamiento):
        pass

    @abstractmethod
    def get_ultimo_comportamiento(self):
        pass

    @abstractmethod
    def declarar_dia(self, pistas_encontradas, ubicacion_investigada):
        pass

    @abstractmethod
    def interrogar(self, pistas_encontradas):
        pass


class Detective(Jugador):
    def __init__(self, nombre):
        super().__init__(nombre)
        self._pistas = []

    def get_nombre(self):
        return self._nombre

    def es_impostor(self):
        return self._es_impostor

    def set_impostor(self, valor):
        self._es_impostor = valor

    def agregar_comportamiento(self, comportamiento):
        self._comportamientos_dia.append(comportamiento)

    def get_ultimo_comportamiento(self):
        return self._comportamientos_dia[-1] if self._comportamientos_dia else "No hay registro"

    def declarar_dia(self, pistas_encontradas, ubicacion_investigada):
        return f"Estoy investigando en {ubicacion_investigada} con las pistas {', '.join(pistas_encontradas) if pistas_encontradas else 'ninguna'}."

    def interrogar(self, pistas_encontradas):
        return f"Estoy analizando las pistas: {', '.join(pistas_encontradas) if pistas_encontradas else 'sin pistas por ahora'}."

    def agregar_pista(self, pista):
        self._pistas.append(pista)

    def get_pistas(self):
        return self._pistas


class Paciente(Jugador):
    def __init__(self, nombre):
        super().__init__(nombre)

    def get_nombre(self):
        return self._nombre

    def es_impostor(self):
        return self._es_impostor

    def set_impostor(self, valor):
        self._es_impostor = valor

    def agregar_comportamiento(self, comportamiento):
        self._comportamientos_dia.append(comportamiento)

    def get_ultimo_comportamiento(self):
        return self._comportamientos_dia[-1] if self._comportamientos_dia else "No hay registro"

    def declarar_dia(self, pistas_encontradas, ubicacion_investigada):
        if self._es_impostor:
            return self._declarar_impostor(pistas_encontradas, ubicacion_investigada)
        else:
            return self._declarar_paciente_normal(pistas_encontradas, ubicacion_investigada)

    def _declarar_impostor(self, pistas, ubicacion):
        declaraciones = [
            f"Estuve en {ubicacion} haciendo mis ejercicios de relajación",
            f"Pasé el día en {ubicacion} meditando sobre mi recuperación",
            f"En {ubicacion} practiqué mis técnicas de control mental",
            f"Dediqué el día en {ubicacion} a organizar mis pensamientos"
        ]
        if any("labial" in pista.lower() for pista in pistas):
            declaraciones.extend([
                f"En {ubicacion} noté que alguien había estado maquillándose",
                f"Vi algo rojo en {ubicacion} pero no le presté atención"
            ])
        if any("reloj" in pista.lower() for pista in pistas):
            declaraciones.extend([
                f"En {ubicacion} me fijé en la hora frecuentemente",
                f"El tiempo pasa lento aquí, lo noté en {ubicacion}"
            ])
        if any("llave" in pista.lower() for pista in pistas):
            declaraciones.extend([
                f"En {ubicacion} pensé en lo importante que son las cerraduras",
                f"{ubicacion} me recordó que debemos mantener todo seguro"
            ])
        return random.choice(declaraciones)

    def _declarar_paciente_normal(self, pistas, ubicacion):
        declaraciones = [
            f"Estuve en {ubicacion} viendo la televisión",
            f"En {ubicacion} conversé con otros pacientes",
            f"Pasé el día en {ubicacion} leyendo revistas",
            f"En {ubicacion} ayudé a ordenar algunas cosas",
            f"Dediqué la tarde en {ubicacion} a escribir en mi diario",
            f"En {ubicacion} participé en actividades grupales"
        ]
        if any("labial" in pista.lower() for pista in pistas):
            declaraciones.extend([
                f"En {ubicacion} noté que había cosas de maquillaje",
                f"Vi colores llamativos en {ubicacion} durante el día"
            ])
        return random.choice(declaraciones)

    def interrogar(self, pistas_encontradas):
        if self._es_impostor:
            respuestas = [
                "No recuerdo nada fuera de lo normal hoy",
                "Estuve concentrado en mi terapia todo el día",
                "Solo hice lo que normalmente hacemos aquí",
                "Me sentí un poco ansioso pero es normal en mi condición"
            ]
            if any("labial" in pista.lower() for pista in pistas_encontradas):
                respuestas.extend([
                    "¿Maquillaje? No, yo no uso esas cosas",
                    "No sé nada sobre productos de belleza"
                ])
            if any("reloj" in pista.lower() for pista in pistas_encontradas):
                respuestas.extend([
                    "Siempre pierdo la noción del tiempo aquí",
                    "Los relojes me ponen nervioso, evito mirarlos"
                ])
        else:
            respuestas = [
                "Hoy fue un día como cualquier otro",
                "Me sentí bastante bien durante el día",
                "Participé en todas las actividades programadas",
                "Conversé con varios compañeros hoy",
                "Estuve un poco distraído pero nada grave"
            ]
            if any("labial" in pista.lower() for pista in pistas_encontradas):
                respuestas.extend([
                    "Vi a alguien con las manos manchadas hoy",
                    "Noté un olor peculiar en el aire"
                ])
        return random.choice(respuestas)


def asignar_impostor(pacientes):
    impostor = random.choice(pacientes)
    impostor.set_impostor(True)
    return impostor


class Ubicacion:
    def __init__(self, nombre, pistas):
        self.nombre = nombre
        self.pistas = pistas
        self.pistas_restantes = pistas.copy()

    def obtener_pista(self):
        if self.pistas_restantes:
            return self.pistas_restantes.pop(0)
        return None

    def tiene_pistas(self):
        return len(self.pistas_restantes) > 0

    def __str__(self):  
        pistas_restantes = len(self.pistas_restantes)
        return f"{self.nombre} ({pistas_restantes} pista{'s' if pistas_restantes != 1 else ''})"


class JuegoDetective:
    def __init__(self):
        self.personajes = []
        self.ubicaciones = []
        self.dia_actual = 1
        self.total_dias = 5
        self.pistas_encontradas = []
        self.impostor_real = None

    def inicializar_juego(self):
        nombres = ["Carlos", "Ana", "Miguel", "Laura", "David"]
        random.shuffle(nombres)
        self.personajes = [Paciente(nombre) for nombre in nombres[:3]]
        self.impostor_real = random.choice(self.personajes)
        self.impostor_real.set_impostor(True)
        self.ubicaciones = [
            Ubicacion("Dormitorio", [
                "Encontraste un labial rojo escondido entre las sábanas",
                "Hay un reloj con la hora detenida en las 3:15",
                "Ves unas llaves que no deberían estar aquí"
            ]),
            Ubicacion("Baño", [
                "Hay manchas rojas en el espejo del baño",
                "Encuentras un reloj de pulsera olvidado",
                "Ves marcas recientes en la cerradura"
            ]),
            Ubicacion("Cocina", [
                "Encuentras comida teñida de color rojo",
                "El reloj de la cocina ha sido manipulado",
                "Hay un juego de llaves extra en un cajón"
            ]),
            Ubicacion("Sótano", [
                "Encuentras restos de maquillaje en una mesa",
                "Hay un reloj antiguo que todavía funciona",
                "Ves llaves oxidadas de lugares desconocidos"
            ])
        ]


class SaltoTemporal:
    def __init__(self):
        self._usado = False
        self._estado_guardado = None

    def guardar_estado(self, juego):
        if not self._usado:
            self._estado_guardado = {
                "dia_actual": juego.dia_actual,
                "pistas": list(juego.pistas_encontradas),
                "ubicaciones": [(u.nombre, list(u.pistas_restantes)) for u in juego.ubicaciones]
            }

    def regresar_en_el_tiempo(self, juego):
        if self._usado or not self._estado_guardado:
            return False
        estado = self._estado_guardado
        juego.dia_actual = estado["dia_actual"]
        juego.pistas_encontradas = estado["pistas"]
        for u in juego.ubicaciones:
            for nombre, pistas_restantes in estado["ubicaciones"]:
                if u.nombre == nombre:
                    u.pistas_restantes = pistas_restantes
        self._usado = True
        return True


# === Interfaz gráfica ===

class JuegoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🧠 Juego del Impostor - Psiquiátrico 🕵‍♂")
        self.juego = JuegoDetective()
        self.juego.inicializar_juego()
        self.salto_temporal = SaltoTemporal()
        self.crear_interfaz()
        self.investigado_hoy = False
        self.interrogado_hoy = False

    def crear_interfaz(self):
        self.texto = tk.Text(self.root, width=80, height=25, wrap="word", bg="#f9f9f9")
        self.texto.pack(pady=10)

        self.boton_investigar = tk.Button(self.root, text="🔍 Investigar", command=self.investigar)
        self.boton_investigar.pack(side="left", padx=10)

        self.boton_interrogar = tk.Button(self.root, text="❓ Interrogar", command=self.interrogar, state="disabled")
        self.boton_interrogar.pack(side="left", padx=10)

        self.boton_siguiente = tk.Button(self.root, text="⏭ Siguiente Día", command=self.siguiente_dia,
                                         state="disabled")
        self.boton_siguiente.pack(side="left", padx=10)

        self.mostrar_intro()
        self.boton_tiempo = tk.Button(self.root, text="⏳ Regresar en el tiempo", command=self.regresar_tiempo)
        self.boton_tiempo.pack(side="left", padx=10)

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
                "¿A quién deseas interrogar?\n" + "\n".join(
                    [f"{i + 1}. {n}" for i, n in enumerate(nombres)]
                ) + "\n4. No interrogar a nadie"
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

# === Ejecución ===
if __name__ == "__main__":
    root = tk.Tk()
    gui = JuegoGUI(root)
    root.mainloop() 
