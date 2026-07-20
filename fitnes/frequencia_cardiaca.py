"""Frequência cardíaca máxima e zonas de treino.

Usa a fórmula clássica (220 - idade) para estimar a frequência
cardíaca máxima e divide o resultado em cinco zonas de intensidade,
como referência geral para orientar o treino.
"""

ZONAS = [
    ("Zona 1 - Recuperação (50-60%)", 0.5, 0.6),
    ("Zona 2 - Leve (60-70%)", 0.6, 0.7),
    ("Zona 3 - Moderada (70-80%)", 0.7, 0.8),
    ("Zona 4 - Intensa (80-90%)", 0.8, 0.9),
    ("Zona 5 - Máxima (90-100%)", 0.9, 1.0),
]


def calcular_fc_maxima(idade):
    if idade <= 0:
        raise ValueError("Idade deve ser um valor positivo")
    return 220 - idade


def calcular_zonas_treino(fc_maxima):
    if fc_maxima <= 0:
        raise ValueError("FC máxima deve ser um valor positivo")
    return {
        nome: (round(fc_maxima * limite_inferior), round(fc_maxima * limite_superior))
        for nome, limite_inferior, limite_superior in ZONAS
    }
