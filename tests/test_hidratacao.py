import pytest

from fitnes.hidratacao import calcular_hidratacao_diaria


def test_calcular_hidratacao_diaria_sedentario():
    assert calcular_hidratacao_diaria(70, "sedentario") == 2450


def test_calcular_hidratacao_diaria_moderado():
    assert calcular_hidratacao_diaria(70, "moderado") == 3000


def test_calcular_hidratacao_diaria_intenso():
    assert calcular_hidratacao_diaria(80, "intenso") == 3550


def test_calcular_hidratacao_diaria_peso_invalido():
    with pytest.raises(ValueError):
        calcular_hidratacao_diaria(0, "sedentario")


def test_calcular_hidratacao_diaria_nivel_invalido():
    with pytest.raises(ValueError):
        calcular_hidratacao_diaria(70, "voador")
