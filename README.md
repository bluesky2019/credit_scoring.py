# credit_scoring

# Simple Credit Scoring System (Logistic Regression)

Este repositório contém uma implementação simplificada de um sistema de **Credit Scoring** para instituições financeiras, utilizando **Regressão Logística** para prever a probabilidade de inadimplência.

## 🚀 Sobre o Projeto

O objetivo deste projeto é demonstrar como transformar dados financeiros (renda, idade, histórico de atrasos) em um Score de crédito que varia de 0 a 1000. Diferente de sistemas baseados em regras fixas, este modelo utiliza uma abordagem estatística para calcular o risco.

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **Pandas**: Manipulação de dados.
* **Scikit-Learn**: Treinamento do modelo de Machine Learning e pré-processamento.
* **Numpy**: Operações matemáticas.

## 📈 Como Funciona o Modelo

O sistema utiliza a **Regressão Logística** para mapear as variáveis de entrada em uma probabilidade entre 0 e 1. 

1.  **Normalização**: Os dados são padronizados usando `StandardScaler` para garantir que a diferença de escala (ex: renda vs idade) não viesse o modelo.
2.  **Cálculo do Score**: O score é derivado do inverso da probabilidade de inadimplência:
    $$Score = (1 - P(inadimplência)) \times 1000$$

## 📋 Pré-requisitos

Instale as dependências necessárias:

```bash
pip install pandas scikit-learn numpy
--


