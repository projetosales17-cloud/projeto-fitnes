"""Triagem de risco pré-atividade física.

Este módulo NÃO faz diagnóstico médico. Ele aplica critérios de
referência amplamente reconhecidos (classificação de pressão arterial
da American Heart Association e o questionário PAR-Q) para sinalizar
quando uma pessoa deve procurar avaliação médica antes de iniciar ou
retomar um programa de exercícios.
"""

RECOMENDACAO_MEDICA = (
    "Recomendamos procurar um médico e realizar exames antes de "
    "iniciar ou continuar um programa de atividade física."
)

RECOMENDACAO_URGENTE = (
    "Valores compatíveis com crise hipertensiva. Procure atendimento "
    "médico imediatamente antes de praticar qualquer atividade física."
)

CATEGORIAS_PRESSAO_COM_RISCO = {
    "Hipotensão",
    "Hipertensão estágio 1",
    "Hipertensão estágio 2",
    "Crise hipertensiva",
}


def classificar_pressao_arterial(sistolica, diastolica):
    """Classifica a pressão arterial segundo critérios da American Heart
    Association (valores em mmHg)."""
    if sistolica <= 0 or diastolica <= 0:
        raise ValueError("Sistólica e diastólica devem ser valores positivos")

    if sistolica >= 180 or diastolica >= 120:
        return "Crise hipertensiva"
    if sistolica >= 140 or diastolica >= 90:
        return "Hipertensão estágio 2"
    if sistolica >= 130 or diastolica >= 80:
        return "Hipertensão estágio 1"
    if sistolica < 90 or diastolica < 60:
        return "Hipotensão"
    if sistolica >= 120:
        return "Pressão elevada"
    return "Normal"


def verificar_alerta_pressao_arterial(categoria):
    """Retorna uma recomendação para a categoria de pressão informada,
    ou None quando a categoria não indica risco."""
    if categoria == "Crise hipertensiva":
        return RECOMENDACAO_URGENTE
    if categoria in CATEGORIAS_PRESSAO_COM_RISCO:
        return RECOMENDACAO_MEDICA
    return None


PERGUNTAS_PAR_Q = {
    "problema_cardiaco": (
        "Um médico já disse que você possui um problema cardíaco e "
        "recomendou realizar atividade física apenas sob supervisão?"
    ),
    "dor_peito_atividade": "Você sente dor no peito ao praticar atividade física?",
    "dor_peito_repouso": (
        "No último mês, você sentiu dor no peito quando não estava "
        "praticando atividade física?"
    ),
    "tontura_desequilibrio": (
        "Você perde o equilíbrio por tontura ou já perdeu a consciência?"
    ),
    "problema_osseo_articular": (
        "Você tem algum problema ósseo ou articular que poderia piorar "
        "com uma mudança na sua atividade física?"
    ),
    "medicamento_pressao_coracao": (
        "Um médico prescreveu atualmente medicamentos para pressão "
        "arterial ou para o coração?"
    ),
    "outro_motivo": (
        "Você conhece qualquer outro motivo pelo qual não deveria "
        "praticar atividade física?"
    ),
}


def triagem_par_q(respostas):
    """Aplica o questionário PAR-Q.

    `respostas` é um dict com um subconjunto das chaves de
    PERGUNTAS_PAR_Q mapeadas para True (sim) ou False (não). Perguntas
    não informadas são tratadas como "não".

    Retorna a lista de perguntas respondidas como "sim" — qualquer
    resposta positiva no PAR-Q indica que a pessoa deve consultar um
    médico antes de aumentar o nível de atividade física.
    """
    return [
        pergunta
        for chave, pergunta in PERGUNTAS_PAR_Q.items()
        if respostas.get(chave)
    ]


def avaliar_liberacao_atividade_fisica(respostas):
    """Combina o PAR-Q em um resultado de triagem simples.

    Retorna um dict com:
    - liberado: False se houve qualquer resposta positiva no PAR-Q
    - alertas: lista das perguntas respondidas como "sim"
    - recomendacao: texto de orientação
    """
    alertas = triagem_par_q(respostas)
    if alertas:
        return {
            "liberado": False,
            "alertas": alertas,
            "recomendacao": RECOMENDACAO_MEDICA,
        }
    return {
        "liberado": True,
        "alertas": [],
        "recomendacao": (
            "Nenhum fator de risco identificado no PAR-Q. Ainda assim, "
            "recomenda-se avaliação médica periódica antes de iniciar "
            "um programa de exercícios."
        ),
    }
