import streamlit as st
import numpy as np
from prediction import make_prediction

# 1. Titre de l'application et description
st.title("Prédiction de l'espèce de la fleur Iris")
st.write("""
Cette application permet de prédire l'espèce d'une fleur Iris en fonction des caractéristiques saisies. 
Veuillez entrer les longueurs et largeurs des sépales et des pétales, puis cliquez sur le bouton pour obtenir une prédiction.
""")

# 2. Interface utilisateur avec sliders et deux colonnes
st.sidebar.header("Entrées des caractéristiques")

# Diviser l'interface en deux colonnes
col1, col2 = st.columns(2)

with col1:
    # Sliders pour les caractéristiques des sépales
    sepal_length = st.slider('Longueur des sépales (cm)', 4.0, 8.0, 5.1)
    sepal_width = st.slider('Largeur des sépales (cm)', 2.0, 4.5, 3.5)

with col2:
    # Sliders pour les caractéristiques des pétales
    petal_length = st.slider('Longueur des pétales (cm)', 1.0, 7.0, 1.4)
    petal_width = st.slider('Largeur des pétales (cm)', 0.1, 2.5, 0.2)

# 3. Bouton pour lancer la prédiction
if st.button("Prédire l'espèce"):
    # Regrouper les entrées utilisateur
    input_data = [sepal_length, sepal_width, petal_length, petal_width]
    
    # Lancer la prédiction en utilisant la fonction `make_prediction` de prediction.py
    prediction = make_prediction(input_data)
    
    # Afficher la classe prédite
    species = ['Setosa', 'Versicolor', 'Virginica']
    st.success(f"L'espèce prédite est : {species[prediction[0]]}")