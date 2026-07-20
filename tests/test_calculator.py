from fitnes.calculator import calcular_imc, classificar_imc


def test_calcular_imc():
    assert calcular_imc(70, 1.75) == 22.86


def test_classificar_imc_abaixo_do_peso():
    assert classificar_imc(17) == "Abaixo do peso"


def test_classificar_imc_peso_normal():
    assert classificar_imc(22) == "Peso normal"


def test_classificar_imc_sobrepeso():
    assert classificar_imc(27) == "Sobrepeso"


def test_classificar_imc_obesidade():
    assert classificar_imc(32) == "Obesidade"
