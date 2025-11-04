import unittest
from juego.personaje import Personaje

class TestPersonaje(unittest.TestCase):
    def test_creacion_personaje(self):
        p = Personaje("Carlos", "Paciente")
        self.assertEqual(p.nombre, "Carlos")
        self.assertEqual(p.rol, "Paciente")

    def test_interaccion(self):
        p = Personaje("Laura", "Impostor")
        respuesta = p.hablar()
        self.assertIsInstance(respuesta, str)

if __name__ == '__main__':
    unittest.main()
