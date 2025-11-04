import pytest
from juego.juego import JuegoDetective
from juego.ubicacion import Ubicacion


def test_inicializacion_juego():
    j = JuegoDetective()
    j.inicializar_juego()

    assert len(j.personajes) == 3
    assert j.impostor_real is not None
    assert len(j.ubicaciones) == 4


def test_pistas_en_ubicacion():
    ubicacion = Ubicacion("Baño", ["Pista 1", "Pista 2"])
    assert ubicacion.tiene_pistas()
    pista = ubicacion.obtener_pista()
    assert pista == "Pista 1"
    assert len(ubicacion.pistas_restantes) == 1
