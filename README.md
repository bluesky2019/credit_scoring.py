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



## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://medium.com/@gilnei809/gilnei-azambuja-borges-analista-de-dados-e-administrador-de-banco-de-dados-8774175b0e46)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/gilnei-azambuja-borges-1a83432b)
[![Hugging Face](https://img.shields.io/badge/HuggingFace-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/bluesky2019)
[![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/gilneiborges)
[![PayPal](https://img.shields.io/badge/Donate-PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://www.paypal.com/donate/?hosted_button_id=FW4VNKJWXLTCJ)

---

[![PayPal](https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://www.paypal.com/donate/?hosted_button_id=FW4VNKJWXLTCJ)
