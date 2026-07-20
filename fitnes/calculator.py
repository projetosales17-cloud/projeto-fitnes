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
