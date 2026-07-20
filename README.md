# Projeto Fitnes

Ferramentas simples em Python para acompanhamento de saúde e treino.

## Funcionalidades

- Cálculo de IMC (Índice de Massa Corporal)
- Classificação do IMC em categorias (abaixo do peso, normal, sobrepeso, obesidade)
- Cálculo de Taxa Metabólica Basal (TMB) pela fórmula de Mifflin-St Jeor
- Cálculo de gasto calórico diário a partir da TMB e do nível de atividade
- Alerta recomendando avaliação médica quando o IMC indica magreza grave ou obesidade grave

## Como usar

```python
from fitnes.calculator import (
    calcular_imc,
    classificar_imc,
    calcular_tmb,
    calcular_gasto_calorico_diario,
)

imc = calcular_imc(peso_kg=70, altura_m=1.75)
print(imc)  # 22.86
print(classificar_imc(imc))  # "Peso normal"

tmb = calcular_tmb(peso_kg=70, altura_cm=175, idade=30, sexo="M")
print(tmb)  # 1648.75

gasto = calcular_gasto_calorico_diario(tmb, nivel_atividade="moderado")
print(gasto)  # 2555.56

from fitnes.calculator import verificar_alerta_saude

alerta = verificar_alerta_saude(imc)
if alerta:
    print(alerta)  # recomenda procurar um médico e fazer exames
```

Níveis de atividade aceitos: `sedentario`, `leve`, `moderado`, `intenso`, `muito_intenso`.

> **Aviso:** `verificar_alerta_saude` não faz diagnóstico médico. É apenas um
> alerta para faixas de IMC associadas a maior risco (IMC < 16 ou IMC ≥ 40),
> recomendando buscar avaliação profissional antes de iniciar ou continuar
> um programa de treino.

## Rodando os testes

```bash
pip install pytest
pytest
```
