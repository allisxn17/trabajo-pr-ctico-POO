import unittest
from juego.juego import JuegoDetective

class TestJuego(unittest.TestCase):
    def test_inicializacion_juego(self):
        juego = JuegoDetective()
        self.assertGreaterEqual(juego.dias_totales, 1)

    def test_pista(self):
        juego = JuegoDetective()
        pista = juego.obtener_pista()
        self.assertIsInstance(pista, str)

    def test_interrogar(self):
        juego = JuegoDetective()
        resultado = juego.interrogar_personaje()
        self.assertIsInstance(resultado, str)

if __name__ == '__main__':
    unittest.main()
