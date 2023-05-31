# formulaire_streamlit.py
import streamlit as st
import pandas as pd
import pickle


 # Chargement du modèle
with open('models/violent_parsed_model_2.sav', 'rb') as file:
    model = pickle.load(file)

def afficher_formulaire():

    Data2_age_cat = {"Greater than 45": 1, "25 - 45": 0, "Less than 25": 2}
    
    Data2_race = {'Other':5, 'Caucasian':2, 'African-American':0, 'Hispanic':3, 'Asian':1,
 'Native American':4,}
    Data2_score_text = {'Low':1, 'Medium':2, 'High':0,}
    Data2_sex = {"Male": 1, "Female": 0}
    
    
    age,cat_age= st.columns(2)
    with cat_age:
        cat_age_cible = st.selectbox("Categorie d'âge", list(Data2_age_cat.keys()), format_func=lambda  x: x)

    with age:
        age_cible = st.number_input("Âge", value=0, step=1)
    sex_, race = st.columns(2)
    with race:
        race_ = st.selectbox("Éthnies", list(Data2_race.keys()), format_func=lambda  x: x)
    with sex_:
        sex_2=st.selectbox("Sexe",list(Data2_sex.keys()), format_func=lambda  x: x)
    score_, priors_= st.columns(2)
    with priors_:
        priors = st.number_input("Priorité", value=0, step=1)
    with score_:
        score_text = st.selectbox("Niveau de score ", list(Data2_score_text.keys()), format_func=lambda  x: x)
           

    
   
    # Bouton de soumission
    submitted = st.button("Soumettre")

    # Traitement des données soumises
    if submitted:
       
        
        data = pd.DataFrame({'age': age_cible, 
                             'age_cat': [Data2_age_cat[cat_age_cible]],
                             'priors_count': priors,
                               'race': [Data2_race[race_]],
                               'score_text': [Data2_score_text[score_text]],
                                 'sex': [Data2_sex[sex_2]],
                                   'v_score_text': [Data2_score_text[score_text]]})
       
				
    # Prédiction avec votre modèle
        prediction = model.predict(data)
        if prediction[0] == 0:

            st.write("Cette personne n'est pas susceptible de récidiver.")
        elif prediction[0] == 1:
            st.write("Cette personne est susceptible de récidiver.")



if __name__ == "__main__":
    afficher_formulaire()
