import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import joblib

class CreditPipeline:
    """Simula um processo de ETL e Engenharia de Dados"""
    def __init__(self):
        self.scaler = StandardScaler()

    def extract_data(self):
        # Simulando carga de dados (Poderia ser um pd.read_sql ou read_csv)
        np.random.seed(42)
        n = 1000
        data = {
            'renda': np.random.normal(5000, 1500, n),
            'idade': np.random.randint(18, 65, n),
            'atrasos_12m': np.random.poisson(0.6, n),
            'historico_credito': np.random.choice([0, 1], n, p=[0.3, 0.7])
        }
        df = pd.DataFrame(data)
        # Target: Inadimplência baseada em lógica probabilística
        logit = 2 - 0.001*df['renda'] + 1.5*df['atrasos_12m'] - 0.8*df['historico_credito']
        df['target'] = (1 / (1 + np.exp(-logit)) > 0.5).astype(int)
        return df

    def transform(self, X, is_train=True):
        if is_train:
            return self.scaler.fit_transform(X)
        return self.scaler.transform(X)

class CreditModel:
    def __init__(self):
        self.pipeline = CreditPipeline()
        self.model = LogisticRegression(solver='lbfgs')

    def run_training(self):
        print("Iniciando extração e treino...")
        df = self.pipeline.extract_data()
        
        X = df.drop('target', axis=1)
        y = df['target']
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        
        X_train_scaled = self.pipeline.transform(X_train)
        self.model.fit(X_train_scaled, y_train)
        
        print(f"Modelo treinado. Acurácia: {self.model.score(self.pipeline.transform(X_test, False), y_test):.2%}")

    def predict_score(self, input_data):
        df_input = pd.DataFrame([input_data])
        scaled_data = self.pipeline.transform(df_input, is_train=False)
        
        prob_default = self.model.predict_proba(scaled_data)[0][1]
        score = int((1 - prob_default) * 1000)
        
        status = "Aprovado" if score > 700 else "Análise" if score > 400 else "Reprovado"
        return {"score": score, "prob_default": f"{prob_default:.2%}", "status": status}

if __name__ == "__main__":
    app = CreditModel()
    app.run_training()
    
    # Teste prático
    teste = {'renda': 7500, 'idade': 40, 'atrasos_12m': 0, 'historico_credito': 1}
    print(f"\nResultado para o cliente: {app.predict_score(teste)}")
