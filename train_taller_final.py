import os
import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Cargar datos
data = pd.read_csv(r"C:\DMC\Machine Learning Eng\clase12_taller_Final\Data_Taller_MLE.csv")
X = data.drop("loan_status", axis=1)
y = data["loan_status"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Configurar MLflow
mlflow.set_tracking_uri("http://localhost:5000")  # Servidor MLflow local
mlflow.set_experiment("credito_experiment_taller")

# Entrenar modelo
with mlflow.start_run():
    model = LogisticRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    acc = accuracy_score(y_test, predictions)

    mlflow.log_metric("accuracy", acc)
    mlflow.sklearn.log_model(model, "model")
    print(f"Modelo guardado con precisión: {acc:.2f}")
