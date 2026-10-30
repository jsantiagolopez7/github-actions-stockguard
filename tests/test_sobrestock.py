import pytest
from src.sobrestock import detectar_sobrestock, porcentaje_inventario


def test_hay_sobrestock():
    assert detectar_sobrestock(120, 100) is True


def test_limite_no_es_sobrestock():
    assert detectar_sobrestock(100, 100) is False


def test_sobrestock_invalido():
    with pytest.raises(ValueError):
        detectar_sobrestock(50, 0)


def test_porcentaje_inventario():
    assert porcentaje_inventario(45, 60) == 75.0
