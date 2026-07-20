def calcular_imc(peso_kg, altura_m):
    if peso_kg <= 0 or altura_m <= 0:
        raise ValueError("Peso e altura devem ser valores positivos")
    return round(peso_kg / (altura_m ** 2), 2)


def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    if imc < 25:
        return "Peso normal"
    if imc < 30:
        return "Sobrepeso"
    return "Obesidade"


FATORES_ATIVIDADE = {
    "sedentario": 1.2,
    "leve": 1.375,
    "moderado": 1.55,
    "intenso": 1.725,
    "muito_intenso": 1.9,
}


def calcular_tmb(peso_kg, altura_cm, idade, sexo):
    """Taxa Metabólica Basal pela fórmula de Mifflin-St Jeor."""
    if peso_kg <= 0 or altura_cm <= 0 or idade <= 0:
        raise ValueError("Peso, altura e idade devem ser valores positivos")
    if sexo not in ("M", "F"):
        raise ValueError("Sexo deve ser 'M' ou 'F'")

    tmb = 10 * peso_kg + 6.25 * altura_cm - 5 * idade
    tmb += 5 if sexo == "M" else -161
    return round(tmb, 2)


def calcular_gasto_calorico_diario(tmb, nivel_atividade):
    if nivel_atividade not in FATORES_ATIVIDADE:
        opcoes = ", ".join(FATORES_ATIVIDADE)
        raise ValueError(f"Nível de atividade deve ser um de: {opcoes}")
    return round(tmb * FATORES_ATIVIDADE[nivel_atividade], 2)
