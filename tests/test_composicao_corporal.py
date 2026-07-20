import pytest

from fitnes.composicao_corporal import calcular_percentual_gordura


def test_calcular_percentual_gordura_masculino():
    resultado = calcular_percentual_gordura(
        sexo="M", altura_cm=180, pescoco_cm=38, cintura_cm=85
    )
    assert resultado == 16.11


def test_calcular_percentual_gordura_feminino():
    resultado = calcular_percentual_gordura(
        sexo="F", altura_cm=165, pescoco_cm=32, cintura_cm=70, quadril_cm=95
    )
    assert resultado == 24.86


def test_calcular_percentual_gordura_sexo_invalido():
    with pytest.raises(ValueError):
        calcular_percentual_gordura(sexo="X", altura_cm=180, pescoco_cm=38, cintura_cm=85)


def test_calcular_percentual_gordura_medidas_invalidas():
    with pytest.raises(ValueError):
        calcular_percentual_gordura(sexo="M", altura_cm=0, pescoco_cm=38, cintura_cm=85)


def test_calcular_percentual_gordura_cintura_menor_que_pescoco():
    with pytest.raises(ValueError):
        calcular_percentual_gordura(sexo="M", altura_cm=180, pescoco_cm=40, cintura_cm=35)


def test_calcular_percentual_gordura_feminino_sem_quadril():
    with pytest.raises(ValueError):
        calcular_percentual_gordura(sexo="F", altura_cm=165, pescoco_cm=32, cintura_cm=70)
