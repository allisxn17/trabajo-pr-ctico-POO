from .personaje import Personaje
from .ubicacion import Ubicacion
from .salto_temporal import SaltoTemporal
import random


class Juego:
    def __init__(self, nombres_personajes, nombres_ubicaciones):
        self.personajes = [Personaje(nombre) for nombre in nombres_personajes]
        self.ubicaciones = [Ubicacion(nombre) for nombre in nombres_ubicaciones]
        self.pistas_encontradas = []
        self.impostor = random.choice(self.personajes)
        self.impostor.set_impostor(True)

    def iniciar_dia(self):
        for personaje in self.personajes:
            ubicacion = random.choice(self.ubicaciones)
            personaje.agregar_comportamiento(ubicacion.nombre)
            ubicacion.recibir_personaje(personaje)

    def investigar(self, nombre_ubicacion):
        ubicacion = next((u for u in self.ubicaciones if u.nombre == nombre_ubicacion), None)
        if not ubicacion:
            return f"La ubicación {nombre_ubicacion} no existe."
        pistas = ubicacion.generar_pistas()
        self.pistas_encontradas.extend(pistas)
        return pistas

    def interrogar_personaje(self, nombre_personaje):
        personaje = next((p for p in self.personajes if p.get_nombre() == nombre_personaje), None)
        if not personaje:
            return f"No existe ningún personaje llamado {nombre_personaje}."
        return personaje.interrogar(self.pistas_encontradas)

    def aplicar_salto_temporal(self):
        salto = SaltoTemporal(self)
        salto.ejecutar()
        return "El tiempo se ha distorsionado... todo ha cambiado."

    def mostrar_estado(self):
        estado = "\n=== ESTADO ACTUAL ===\n"
        estado += f"Pistas encontradas: {', '.join(self.pistas_encontradas) if self.pistas_encontradas else 'Ninguna'}\n"
        estado += "Personajes:\n"
        for p in self.personajes:
            tipo = "IMPOSTOR" if p.es_impostor() else "Normal"
            estado += f" - {p.get_nombre()} ({tipo}) | Último comportamiento: {p.get_ultimo_comportamiento()}\n"
        return estado
