
import pickle
import numpy as np

# Fonction pour charger le modèle depuis le fichier sauvegardé
def load_model(filepath='iris_model.pkl'):
    with open(filepath, 'rb') as f:
        model = pickle.load(f)
    return model

# Fonction pour faire des prédictions
def make_prediction(input_data):
    # Charger le modèle
    model = load_model()
    
    # Convertir les données d'entrée en format numpy array si nécessaire
    input_data = np.array(input_data).reshape(1, -1)
    
    # Faire des prédictions
    prediction = model.predict(input_data)
    
    return prediction