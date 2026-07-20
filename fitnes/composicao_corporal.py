"""Estimativa de percentual de gordura corporal.

Usa a fórmula da Marinha dos EUA (U.S. Navy), baseada em medidas de
circunferência corporal. Todas as medidas devem ser informadas em
centímetros.
"""

import math


def calcular_percentual_gordura(sexo, altura_cm, pescoco_cm, cintura_cm, quadril_cm=None):
    if sexo not in ("M", "F"):
        raise ValueError("Sexo deve ser 'M' ou 'F'")
    if altura_cm <= 0 or pescoco_cm <= 0 or cintura_cm <= 0:
        raise ValueError("Altura, pescoço e cintura devem ser valores positivos")

    if sexo == "M":
        if cintura_cm <= pescoco_cm:
            raise ValueError("Cintura deve ser maior que o pescoço")
        denominador = (
            1.0324
            - 0.19077 * math.log10(cintura_cm - pescoco_cm)
            + 0.15456 * math.log10(altura_cm)
        )
    else:
        if quadril_cm is None or quadril_cm <= 0:
            raise ValueError("Quadril é obrigatório e deve ser positivo para sexo 'F'")
        if (cintura_cm + quadril_cm) <= pescoco_cm:
            raise ValueError("Cintura + quadril deve ser maior que o pescoço")
        denominador = (
            1.29579
            - 0.35004 * math.log10(cintura_cm + quadril_cm - pescoco_cm)
            + 0.22100 * math.log10(altura_cm)
        )

    percentual = 495 / denominador - 450
    return round(percentual, 2)
