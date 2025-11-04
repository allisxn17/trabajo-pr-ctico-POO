import random
from juego.personaje import Personaje
from juego.ubicacion import Ubicacion

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
        self.personajes = [Personaje(nombre) for nombre in nombres[:3]]
        self.impostor_real = random.choice(self.personajes)
        self.impostor_real.set_impostor(True)
        self.ubicaciones = [
            Ubicacion("Dormitorio", [
                "Encontraste un labial rojo escondido entre sábanas",
                "Hay un reloj con la hora detenida en las 3:15",
                "Ves unas llaves que no deberían estar aquí"
            ]),
            Ubicacion("Baño", [
                "Hay manchas rojas en el espejo",
                "Encuentras un reloj de pulsera olvidado",
                "Ves marcas recientes en la cerradura"
            ]),
            Ubicacion("Cocina", [
                "Encuentras comida teñida de color rojo",
                "El reloj ha sido manipulado",
                "Hay un juego de llaves extra en un cajón"
            ]),
            Ubicacion("Sótano", [
                "Encuentras restos de maquillaje en una mesa",
                "Hay un reloj antiguo que todavía funciona",
                "Ves llaves oxidadas de lugares desconocidos"
            ])
        ]
