# Projeto Fitnes

[![Tests](https://github.com/projetosales17-cloud/projeto-fitnes/actions/workflows/tests.yml/badge.svg)](https://github.com/projetosales17-cloud/projeto-fitnes/actions/workflows/tests.yml)

Ferramentas simples em Python para acompanhamento de saúde e treino.

## Funcionalidades

- Cálculo de IMC (Índice de Massa Corporal)
- Classificação do IMC em categorias (abaixo do peso, normal, sobrepeso, obesidade)
- Cálculo de Taxa Metabólica Basal (TMB) pela fórmula de Mifflin-St Jeor
- Cálculo de gasto calórico diário a partir da TMB e do nível de atividade
- Alerta recomendando avaliação médica quando o IMC indica magreza grave ou obesidade grave
- Classificação de pressão arterial (hipotensão, normal, elevada, hipertensão estágio 1/2, crise hipertensiva)
- Triagem PAR-Q para identificar outros fatores de risco antes de iniciar atividade física
- Cálculo de frequência cardíaca máxima e zonas de intensidade de treino

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

### Triagem de risco pré-atividade física

```python
from fitnes.triagem import (
    classificar_pressao_arterial,
    verificar_alerta_pressao_arterial,
    avaliar_liberacao_atividade_fisica,
)

categoria = classificar_pressao_arterial(sistolica=150, diastolica=95)
print(categoria)  # "Hipertensão estágio 2"
print(verificar_alerta_pressao_arterial(categoria))  # recomenda avaliação médica

resultado = avaliar_liberacao_atividade_fisica({
    "problema_cardiaco": False,
    "dor_peito_atividade": True,
})
print(resultado["liberado"])      # False
print(resultado["alertas"])       # lista das perguntas do PAR-Q respondidas "sim"
print(resultado["recomendacao"])  # recomenda avaliação médica
```

> **Aviso:** `fitnes/triagem.py` não faz diagnóstico médico. Aplica a
> classificação de pressão arterial da American Heart Association e o
> questionário padrão PAR-Q (Physical Activity Readiness Questionnaire)
> apenas para sinalizar quando uma avaliação médica é recomendada antes
> de iniciar ou retomar atividade física.

### Frequência cardíaca e zonas de treino

```python
from fitnes.frequencia_cardiaca import calcular_fc_maxima, calcular_zonas_treino

fc_maxima = calcular_fc_maxima(idade=30)
print(fc_maxima)  # 190

zonas = calcular_zonas_treino(fc_maxima)
print(zonas["Zona 3 - Moderada (70-80%)"])  # (133, 152)
```

## Rodando os testes

```bash
pip install pytest
pytest
```
