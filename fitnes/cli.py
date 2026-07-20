"""Interface de linha de comando do Projeto Fitnes.

`ler` e `escrever` são injetados (por padrão `input`/`print`) para
permitir testar os fluxos sem interação real com o terminal.
"""

from fitnes.calculator import (
    FATORES_ATIVIDADE,
    calcular_gasto_calorico_diario,
    calcular_imc,
    calcular_tmb,
    classificar_imc,
    verificar_alerta_saude,
)
from fitnes.composicao_corporal import calcular_percentual_gordura
from fitnes.frequencia_cardiaca import calcular_fc_maxima, calcular_zonas_treino
from fitnes.hidratacao import calcular_hidratacao_diaria
from fitnes.triagem import (
    PERGUNTAS_PAR_Q,
    avaliar_liberacao_atividade_fisica,
    classificar_pressao_arterial,
    verificar_alerta_pressao_arterial,
)

MENU = """
=== Projeto Fitnes ===
1 - Calcular IMC
2 - Calcular TMB e gasto calórico diário
3 - Classificar pressão arterial
4 - Triagem PAR-Q (fatores de risco antes de treinar)
5 - Zonas de frequência cardíaca
6 - Hidratação diária recomendada
7 - Percentual de gordura corporal
0 - Sair
"""


def _pedir_float(ler, escrever, mensagem):
    while True:
        valor = ler(mensagem)
        try:
            return float(valor)
        except ValueError:
            escrever("Valor inválido, digite um número.")


def _pedir_inteiro(ler, escrever, mensagem):
    while True:
        valor = ler(mensagem)
        try:
            return int(valor)
        except ValueError:
            escrever("Valor inválido, digite um número inteiro.")


def _pedir_sexo(ler, escrever):
    while True:
        valor = ler("Sexo (M/F): ").strip().upper()
        if valor in ("M", "F"):
            return valor
        escrever("Digite M ou F.")


def _pedir_nivel_atividade(ler, escrever):
    opcoes = ", ".join(FATORES_ATIVIDADE)
    while True:
        valor = ler(f"Nível de atividade ({opcoes}): ").strip().lower()
        if valor in FATORES_ATIVIDADE:
            return valor
        escrever(f"Nível inválido. Opções: {opcoes}")


def _fluxo_imc(ler, escrever):
    peso = _pedir_float(ler, escrever, "Peso (kg): ")
    altura = _pedir_float(ler, escrever, "Altura (m): ")
    try:
        imc = calcular_imc(peso, altura)
    except ValueError as erro:
        escrever(f"Erro: {erro}")
        return
    escrever(f"IMC: {imc} ({classificar_imc(imc)})")
    alerta = verificar_alerta_saude(imc)
    if alerta:
        escrever(f"ATENÇÃO: {alerta}")


def _fluxo_tmb(ler, escrever):
    peso = _pedir_float(ler, escrever, "Peso (kg): ")
    altura_cm = _pedir_float(ler, escrever, "Altura (cm): ")
    idade = _pedir_inteiro(ler, escrever, "Idade (anos): ")
    sexo = _pedir_sexo(ler, escrever)
    try:
        tmb = calcular_tmb(peso, altura_cm, idade, sexo)
    except ValueError as erro:
        escrever(f"Erro: {erro}")
        return
    escrever(f"TMB: {tmb} kcal/dia")
    nivel = _pedir_nivel_atividade(ler, escrever)
    gasto = calcular_gasto_calorico_diario(tmb, nivel)
    escrever(f"Gasto calórico diário estimado: {gasto} kcal")


def _fluxo_pressao(ler, escrever):
    sistolica = _pedir_float(ler, escrever, "Pressão sistólica (mmHg): ")
    diastolica = _pedir_float(ler, escrever, "Pressão diastólica (mmHg): ")
    try:
        categoria = classificar_pressao_arterial(sistolica, diastolica)
    except ValueError as erro:
        escrever(f"Erro: {erro}")
        return
    escrever(f"Classificação: {categoria}")
    alerta = verificar_alerta_pressao_arterial(categoria)
    if alerta:
        escrever(f"ATENÇÃO: {alerta}")


def _fluxo_parq(ler, escrever):
    respostas = {}
    for chave, pergunta in PERGUNTAS_PAR_Q.items():
        resposta = ler(f"{pergunta} (s/n): ").strip().lower()
        respostas[chave] = resposta in ("s", "sim")

    resultado = avaliar_liberacao_atividade_fisica(respostas)
    if resultado["liberado"]:
        escrever("Nenhum fator de risco identificado no PAR-Q.")
    else:
        escrever("ATENÇÃO: fatores de risco identificados:")
        for item in resultado["alertas"]:
            escrever(f"- {item}")
    escrever(resultado["recomendacao"])


def _fluxo_frequencia_cardiaca(ler, escrever):
    idade = _pedir_inteiro(ler, escrever, "Idade (anos): ")
    try:
        fc_maxima = calcular_fc_maxima(idade)
    except ValueError as erro:
        escrever(f"Erro: {erro}")
        return
    escrever(f"FC máxima estimada: {fc_maxima} bpm")
    for nome, (minimo, maximo) in calcular_zonas_treino(fc_maxima).items():
        escrever(f"{nome}: {minimo}-{maximo} bpm")


def _fluxo_hidratacao(ler, escrever):
    peso = _pedir_float(ler, escrever, "Peso (kg): ")
    nivel = _pedir_nivel_atividade(ler, escrever)
    try:
        hidratacao = calcular_hidratacao_diaria(peso, nivel)
    except ValueError as erro:
        escrever(f"Erro: {erro}")
        return
    escrever(f"Hidratação diária recomendada: {hidratacao} ml")


def _fluxo_composicao_corporal(ler, escrever):
    sexo = _pedir_sexo(ler, escrever)
    altura_cm = _pedir_float(ler, escrever, "Altura (cm): ")
    pescoco_cm = _pedir_float(ler, escrever, "Pescoço (cm): ")
    cintura_cm = _pedir_float(ler, escrever, "Cintura (cm): ")
    quadril_cm = None
    if sexo == "F":
        quadril_cm = _pedir_float(ler, escrever, "Quadril (cm): ")
    try:
        percentual = calcular_percentual_gordura(
            sexo, altura_cm, pescoco_cm, cintura_cm, quadril_cm
        )
    except ValueError as erro:
        escrever(f"Erro: {erro}")
        return
    escrever(f"Percentual de gordura corporal estimado: {percentual}%")


OPCOES = {
    "1": _fluxo_imc,
    "2": _fluxo_tmb,
    "3": _fluxo_pressao,
    "4": _fluxo_parq,
    "5": _fluxo_frequencia_cardiaca,
    "6": _fluxo_hidratacao,
    "7": _fluxo_composicao_corporal,
}


def main(ler=input, escrever=print):
    while True:
        escrever(MENU)
        opcao = ler("Escolha uma opção: ").strip()
        if opcao == "0":
            escrever("Até logo!")
            return
        fluxo = OPCOES.get(opcao)
        if fluxo is None:
            escrever("Opção inválida.")
            continue
        fluxo(ler, escrever)


if __name__ == "__main__":
    main()
