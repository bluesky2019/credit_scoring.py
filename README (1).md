<div align="center">

# 📊 Credit Scoring System
### Logistic Regression · Score 0–1000 · Python

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.x-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?style=flat-square&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-1.x-013243?style=flat-square&logo=numpy&logoColor=white)

</div>

---

## Sobre o Projeto

Implementação simplificada de um sistema de **Credit Scoring** para instituições financeiras. Diferente de sistemas baseados em regras fixas, este modelo utiliza **Regressão Logística** para calcular o risco de inadimplência de forma estatística, transformando variáveis financeiras em um score de **0 a 1000**.

---

## ⚙️ Como Funciona

```
Dados (renda, idade, histórico) → StandardScaler → Regressão Logística → Score
                                                                       ↓
                                          Score = (1 − P(inadimplência)) × 1000
```

| Etapa | Descrição |
|-------|-----------|
| 1. Entrada | Renda, idade, histórico de atrasos |
| 2. Normalização | `StandardScaler` padroniza a escala dos dados |
| 3. Predição | Regressão Logística calcula P(inadimplência) |
| 4. Score | Inverso da probabilidade × 1000 |

---

## 🛠️ Tecnologias

| Lib | Uso |
|-----|-----|
| **Pandas** | Manipulação e limpeza dos dados |
| **Scikit-Learn** | Treinamento do modelo e pré-processamento |
| **NumPy** | Operações matemáticas |

---

## 🚀 Instalação

```bash
pip install pandas scikit-learn numpy
```

---

## 🔗 Conecte-se

[![Portfolio](https://img.shields.io/badge/Portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://medium.com/@gilnei809/gilnei-azambuja-borges-analista-de-dados-e-administrador-de-banco-de-dados-8774175b0e46)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/gilnei-azambuja-borges-1a83432b)
[![Hugging Face](https://img.shields.io/badge/HuggingFace-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/bluesky2019)
[![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/gilneiborges)
[![PayPal](https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://www.paypal.com/donate/?hosted_button_id=FW4VNKJWXLTCJ)
