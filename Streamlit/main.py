import streamlit as st
import numpy as np
import pandas as pd
from formulaire_predict import afficher_formulaire
from Data_Viz import data_visualization


def main():

    compas_scores = pd.read_csv('../data/compas-scores-raw.csv')
    violent_parsed = pd.read_csv('../data/cox-violent-parsed.csv')
    propublica_data = pd.read_csv('../data/propublica_data_for_fairml.csv')
    compas_scores['Ethnic_Code_Text'] = compas_scores['Ethnic_Code_Text'].replace('African-Am', "African-American")
    # Liste des datasets
    datasets = {
        'Compas Scores': compas_scores,
        'Violent Parsed': violent_parsed,
        'Propublica Data': propublica_data
    }


    def home():
        st.title('COMPAS Recidivism Risk Analysis')
        image_2 = 'https://www.coe.int/documents/16695/10936098/0/a2950883-a918-1946-16a5-5c95f69ecbc8'
        st.image(image_2, caption="Comparateur de meilleurs models", use_column_width=True)
        st.write("Bienvenue dans notre application Streamlit dédiée à l'étude de l'outil SHAP dans le contexte d'un projet pédagogique sur les données COMPAS. Cette application a été développée dans le but de présenter les visualisations des différentes bases de données du projet COMPAS, ainsi que de réaliser des prédictions.")
        st.markdown("L'algorithme commercial populaire appelé COMPAS (Correctional Offender Management Profiling for Alternative Sanctions) est utilisé par les juges et les agents de libération conditionnelle pour évaluer la probabilité de récidive des défendeurs criminels. Une étude de suivi sur deux ans a démontré que cet algorithme présente un biais en faveur des accusés blancs et au détriment des détenus noirs. Cette étude a mesuré le schéma des erreurs en termes de précision/sensibilité, révélant des résultats remarquables. En d'autres termes, l'étude a examiné ceux qui ont réellement commis des crimes ou des crimes violents deux ans après leur évaluation par l'algorithme.")
        st.markdown(''' 
        
        ''')
        st.markdown(''' 
Le projet pédagogique comprend trois jeux de données distincts qui seront explorés à travers notre application. Chacun de ces ensembles de données fournit des informations précieuses pour comprendre et analyser les évaluations de récidive effectuées par le système COMPAS.

Grâce à notre application, vous pourrez visualiser ces jeux de données de manière interactive, en explorant les différents aspects et caractéristiques. Nous avons utilisé des graphiques et des tableaux pour représenter les informations de manière claire et compréhensible. Vous pourrez ainsi examiner les tendances, les corrélations et les distributions présentes dans les données COMPAS.

En plus de l'aspect visuel, notre application vous permet également de réaliser des prédictions. En utilisant des modèles préalablement entraînés sur les données COMPAS, vous pourrez fournir des entrées spécifiques et obtenir une prédiction sur la probabilité de récidive d'un individu. Cela vous permettra de mieux comprendre le fonctionnement de l'outil SHAP et son impact sur les résultats des évaluations de récidive.

Nous avons conçu cette application dans un but éducatif, en mettant l'accent sur la compréhension et l'interprétation des données COMPAS. Nous espérons qu'elle vous aidera à approfondir vos connaissances sur les questions de justice pénale et de biais algorithmique.

Nous vous invitons donc à explorer notre application Streamlit dédiée à l'étude de l'outil SHAP dans le cadre du projet pédagogique sur les données COMPAS. N'hésitez pas à interagir avec les visualisations, à réaliser des prédictions et à tirer vos propres conclusions. Bonne exploration !''')

    # Page 1
    def page1():
        data_visualization()
            

  



    # Page 2
    def page2():
        st.title("Models IA et Prédiction")
        image = 'Img/model_2_.png'
        st.image(image, caption="Comparateur de meilleurs models", use_column_width=True)
        

                
        st.markdown("## Prédictions")
        afficher_formulaire()

    


    # Définir les onglets
    tabs = {
        "Accueil": home,
        "Data Viz": page1,
        "Prédiction": page2
    }

    
    selected_tab = st.sidebar.selectbox("Navigation", list(tabs.keys()))
    page = tabs[selected_tab]
    page()


if __name__ == "__main__":
    main()