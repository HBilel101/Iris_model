import pickle
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 1. Charger le dataset Iris
iris = load_iris()
X, y = iris.data, iris.target

# 2. Diviser le dataset en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 3. Entraîner un modèle (Random Forest dans cet exemple)
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# 4. Évaluer la précision du modèle
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# 5. Sauvegarder le modèle entraîné
with open('iris_model.pkl', 'wb') as f:
    pickle.dump(model, f)