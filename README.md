# Projeto Fitnes

Ferramentas simples em Python para acompanhamento de saúde e treino.

## Funcionalidades

- Cálculo de IMC (Índice de Massa Corporal)
- Classificação do IMC em categorias (abaixo do peso, normal, sobrepeso, obesidade)

## Como usar

```python
from fitnes.calculator import calcular_imc, classificar_imc

imc = calcular_imc(peso_kg=70, altura_m=1.75)
print(imc)  # 22.86
print(classificar_imc(imc))  # "Peso normal"
```

## Rodando os testes

```bash
pip install pytest
pytest
```
