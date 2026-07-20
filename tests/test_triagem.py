import pytest

from fitnes.triagem import (
    avaliar_liberacao_atividade_fisica,
    classificar_pressao_arterial,
    triagem_par_q,
    verificar_alerta_pressao_arterial,
)


def test_classificar_pressao_normal():
    assert classificar_pressao_arterial(110, 70) == "Normal"


def test_classificar_pressao_elevada():
    assert classificar_pressao_arterial(125, 70) == "Pressão elevada"


def test_classificar_pressao_hipertensao_estagio_1():
    assert classificar_pressao_arterial(132, 82) == "Hipertensão estágio 1"


def test_classificar_pressao_hipertensao_estagio_2():
    assert classificar_pressao_arterial(150, 95) == "Hipertensão estágio 2"


def test_classificar_pressao_crise_hipertensiva():
    assert classificar_pressao_arterial(185, 125) == "Crise hipertensiva"


def test_classificar_pressao_hipotensao():
    assert classificar_pressao_arterial(85, 55) == "Hipotensão"


def test_classificar_pressao_valores_invalidos():
    with pytest.raises(ValueError):
        classificar_pressao_arterial(0, 70)


def test_verificar_alerta_pressao_arterial_normal():
    assert verificar_alerta_pressao_arterial("Normal") is None


def test_verificar_alerta_pressao_arterial_hipotensao():
    assert verificar_alerta_pressao_arterial("Hipotensão") is not None


def test_verificar_alerta_pressao_arterial_crise():
    alerta = verificar_alerta_pressao_arterial("Crise hipertensiva")
    assert alerta is not None
    assert "imediatamente" in alerta


def test_triagem_par_q_sem_fatores_de_risco():
    assert triagem_par_q({}) == []


def test_triagem_par_q_com_fator_de_risco():
    resultado = triagem_par_q({"dor_peito_atividade": True})
    assert len(resultado) == 1


def test_triagem_par_q_multiplos_fatores():
    resultado = triagem_par_q(
        {"problema_cardiaco": True, "tontura_desequilibrio": True, "outro_motivo": False}
    )
    assert len(resultado) == 2


def test_avaliar_liberacao_atividade_fisica_liberado():
    resultado = avaliar_liberacao_atividade_fisica({})
    assert resultado["liberado"] is True
    assert resultado["alertas"] == []


def test_avaliar_liberacao_atividade_fisica_nao_liberado():
    resultado = avaliar_liberacao_atividade_fisica({"medicamento_pressao_coracao": True})
    assert resultado["liberado"] is False
    assert len(resultado["alertas"]) == 1
