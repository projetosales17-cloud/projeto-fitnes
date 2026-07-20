from fitnes.cli import main


def _executar(respostas):
    entradas = iter(respostas)
    saidas = []

    def ler(mensagem=""):
        return next(entradas)

    def escrever(mensagem=""):
        saidas.append(str(mensagem))

    main(ler=ler, escrever=escrever)
    return saidas


def test_cli_sai_imediatamente():
    saidas = _executar(["0"])
    assert any("Até logo" in linha for linha in saidas)


def test_cli_opcao_invalida():
    saidas = _executar(["99", "0"])
    assert any("Opção inválida" in linha for linha in saidas)


def test_cli_fluxo_imc():
    saidas = _executar(["1", "70", "1.75", "0"])
    assert any("IMC: 22.86" in linha for linha in saidas)
    assert any("Peso normal" in linha for linha in saidas)


def test_cli_fluxo_imc_valor_invalido_repete_pergunta():
    saidas = _executar(["1", "abc", "70", "1.75", "0"])
    assert any("Valor inválido" in linha for linha in saidas)
    assert any("IMC: 22.86" in linha for linha in saidas)


def test_cli_fluxo_imc_com_alerta_grave():
    saidas = _executar(["1", "40", "1.75", "0"])
    assert any("ATENÇÃO" in linha for linha in saidas)


def test_cli_fluxo_hidratacao():
    saidas = _executar(["6", "70", "moderado", "0"])
    assert any("3000" in linha for linha in saidas)


def test_cli_fluxo_pressao_com_alerta():
    saidas = _executar(["3", "150", "95", "0"])
    assert any("Hipertensão estágio 2" in linha for linha in saidas)
    assert any("ATENÇÃO" in linha for linha in saidas)


def test_cli_fluxo_par_q_sem_fatores_de_risco():
    respostas_par_q = ["n"] * 7
    saidas = _executar(["4", *respostas_par_q, "0"])
    assert any("Nenhum fator de risco identificado" in linha for linha in saidas)
