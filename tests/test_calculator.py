import pytest

from fitnes.calculator import (
    calcular_gasto_calorico_diario,
    calcular_imc,
    calcular_tmb,
    classificar_imc,
    verificar_alerta_saude,
)


def test_calcular_imc():
    assert calcular_imc(70, 1.75) == 22.86


def test_calcular_imc_peso_invalido():
    with pytest.raises(ValueError):
        calcular_imc(0, 1.75)


def test_calcular_imc_altura_invalida():
    with pytest.raises(ValueError):
        calcular_imc(70, -1.75)


def test_classificar_imc_abaixo_do_peso():
    assert classificar_imc(17) == "Abaixo do peso"


def test_classificar_imc_peso_normal():
    assert classificar_imc(22) == "Peso normal"


def test_classificar_imc_sobrepeso():
    assert classificar_imc(27) == "Sobrepeso"


def test_classificar_imc_obesidade():
    assert classificar_imc(32) == "Obesidade"


def test_calcular_tmb_masculino():
    assert calcular_tmb(70, 175, 30, "M") == 1648.75


def test_calcular_tmb_feminino():
    assert calcular_tmb(60, 165, 25, "F") == 1345.25


def test_calcular_tmb_sexo_invalido():
    with pytest.raises(ValueError):
        calcular_tmb(70, 175, 30, "X")


def test_calcular_tmb_valores_invalidos():
    with pytest.raises(ValueError):
        calcular_tmb(0, 175, 30, "M")


def test_calcular_gasto_calorico_diario():
    assert calcular_gasto_calorico_diario(1648.75, "moderado") == 2555.56


def test_calcular_gasto_calorico_diario_nivel_invalido():
    with pytest.raises(ValueError):
        calcular_gasto_calorico_diario(1648.75, "voador")


def test_verificar_alerta_saude_magreza_grave():
    assert verificar_alerta_saude(15) is not None


def test_verificar_alerta_saude_obesidade_grave():
    assert verificar_alerta_saude(41) is not None


def test_verificar_alerta_saude_peso_normal():
    assert verificar_alerta_saude(22) is None


def test_verificar_alerta_saude_limite_obesidade_grave():
    assert verificar_alerta_saude(40) is not None
