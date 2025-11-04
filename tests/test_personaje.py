import pytest
from juego.personaje import Personaje


def test_creacion_personaje():
    p = Personaje("Ana")
    assert p.get_nombre() == "Ana"
    assert not p.es_impostor()


def test_comportamiento():
    p = Personaje("Carlos")
    p.agregar_comportamiento("Leyó un libro")
    assert p.get_ultimo_comportamiento() == "Leyó un libro"


def test_impostor_flag():
    p = Personaje("Laura")
    p.set_impostor(True)
    assert p.es_impostor()
