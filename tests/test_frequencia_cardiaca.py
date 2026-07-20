import pytest

from fitnes.frequencia_cardiaca import calcular_fc_maxima, calcular_zonas_treino


def test_calcular_fc_maxima():
    assert calcular_fc_maxima(30) == 190


def test_calcular_fc_maxima_idade_invalida():
    with pytest.raises(ValueError):
        calcular_fc_maxima(0)


def test_calcular_zonas_treino():
    zonas = calcular_zonas_treino(190)
    assert zonas["Zona 1 - Recuperação (50-60%)"] == (95, 114)
    assert zonas["Zona 2 - Leve (60-70%)"] == (114, 133)
    assert zonas["Zona 3 - Moderada (70-80%)"] == (133, 152)
    assert zonas["Zona 4 - Intensa (80-90%)"] == (152, 171)
    assert zonas["Zona 5 - Máxima (90-100%)"] == (171, 190)


def test_calcular_zonas_treino_fc_maxima_invalida():
    with pytest.raises(ValueError):
        calcular_zonas_treino(0)
