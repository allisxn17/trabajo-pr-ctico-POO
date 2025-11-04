import random
from .personaje import Personaje
from .ubicacion import Ubicacion
from .salto_temporal import SaltoTemporal

class Juego:
    def __init__(self, nombres_personajes, ubicaciones_pistas):
        self.personajes = [Personaje(nombre) for nombre in nombres_personajes]
        self.ubicaciones = [Ubicacion(nombre, pistas) for nombre, pistas in ubicaciones_pistas.items()]
        self.impostor = random.choice(self.personajes)
        self.impostor.asignar_impostor()
        self.pistas_encontradas = []
        self.salto_temporal = SaltoTemporal(self)

    def mostrar_personajes(self):
        print("\nPersonajes en el juego:")
        for personaje in self.personajes:
            print(f"- {personaje.nombre}")

    def mostrar_ubicaciones(self):
        print("\nUbicaciones disponibles:")
        for ubicacion in self.ubicaciones:
            print(f"- {ubicacion}")

    def investigar_ubicacion(self, nombre_ubicacion):
        ubicacion = next((u for u in self.ubicaciones if u.nombre == nombre_ubicacion), None)
        if ubicacion:
            pista = ubicacion.obtener_pista()
            if pista:
                print(f"\nHas encontrado una pista en {nombre_ubicacion}: {pista}")
                self.pistas_encontradas.append(pista)
            else:
                print(f"\nYa no quedan pistas en {nombre_ubicacion}.")
        else:
            print(f"\nNo existe la ubicación '{nombre_ubicacion}'.")

    def interrogar_personaje(self, nombre_personaje):
        personaje = next((p for p in self.personajes if p.nombre == nombre_personaje), None)
        if personaje:
            personaje.hablar(self.pistas_encontradas)
        else:
            print(f"\nNo existe el personaje '{nombre_personaje}'.")

    def realizar_salto_temporal(self):
        self.salto_temporal.ejecutar()

    def verificar_estado(self):
        print("\n--- Estado del juego ---")
        print(f"Pistas encontradas: {len(self.pistas_encontradas)}")
        for ubicacion in self.ubicaciones:
            print(ubicacion)

