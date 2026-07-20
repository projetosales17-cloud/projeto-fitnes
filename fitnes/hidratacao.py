"""Estimativa de hidratação diária recomendada.

Usa a referência geral de 35 ml de água por kg de peso corporal por
dia, somada a uma quantidade extra conforme o nível de atividade
física, para compensar a perda de líquidos pelo suor.
"""

ML_POR_KG = 35

EXTRA_ML_POR_ATIVIDADE = {
    "sedentario": 0,
    "leve": 350,
    "moderado": 550,
    "intenso": 750,
    "muito_intenso": 1000,
}


def calcular_hidratacao_diaria(peso_kg, nivel_atividade):
    """Retorna a hidratação diária recomendada, em mililitros."""
    if peso_kg <= 0:
        raise ValueError("Peso deve ser um valor positivo")
    if nivel_atividade not in EXTRA_ML_POR_ATIVIDADE:
        opcoes = ", ".join(EXTRA_ML_POR_ATIVIDADE)
        raise ValueError(f"Nível de atividade deve ser um de: {opcoes}")

    base_ml = peso_kg * ML_POR_KG
    extra_ml = EXTRA_ML_POR_ATIVIDADE[nivel_atividade]
    return round(base_ml + extra_ml, 2)
