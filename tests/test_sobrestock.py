import pytest
from src.inventario import detectar_sobrestock


def test_supera_maximo():
    assert detectar_sobrestock(31, 30)


def test_limite_no_es_sobrestock():
    assert not detectar_sobrestock(30, 30)


def test_stock_normal():
    assert not detectar_sobrestock(10, 30)


@pytest.mark.parametrize("actual,maximo", [(-1, 30), (5, 0), (5, -1)])
def test_datos_invalidos(actual, maximo):
    with pytest.raises(ValueError):
        detectar_sobrestock(actual, maximo)
