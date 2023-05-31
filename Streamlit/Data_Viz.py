import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

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
def data_visualization():
        st.title("Data visualization des données ")
        
    # Boîte de sélection pour choisir une dataset
        selected_dataset = st.sidebar.selectbox('Sélectionnez une dataset', list(datasets.keys()))
    # Affichage de l'option sélectionnée
        st.write('Vous avez sélectionné la dataset :', selected_dataset)

    # Affichage des données de la dataset sélectionnée
        selected_data = datasets[selected_dataset]
        st.write(selected_data)


        st.markdown("## Tracé de l'histogramme de chaque colonne numérique ")
        numeric_cols = selected_data.select_dtypes(include=["float64", "int64"]).columns.tolist()
        # Calcul du nombre de lignes et de colonnes nécessaires pour afficher les histogrammes
        num_cols = len(numeric_cols)
        num_rows = (num_cols - 1) // 3 + 1

        fig, axes = plt.subplots(nrows=num_rows, ncols=3, figsize=(12, 3*num_rows))

        for i, col in enumerate(numeric_cols):
            row_idx = i // 3
            col_idx = i % 3
            ax = axes[row_idx, col_idx]
            ax.hist(selected_data[col].dropna(), bins=10)
            ax.set_title(col)

    # Suppression des axes inutiles
        for i in range(num_cols, num_rows*3):
            row_idx = i // 3
            col_idx = i % 3
            fig.delaxes(axes[row_idx, col_idx])

        # Ajustement des espacements entre les graphiques
        fig.tight_layout()

        # Afficher la figure
        st.pyplot(fig) 
        if selected_dataset != 'Propublica Data':
            if   selected_dataset == "Compas Scores" :
                X = selected_data[['Agency_Text','Sex_Code_Text', 'Ethnic_Code_Text','ScaleSet',
            'Language', 'LegalStatus', 'CustodyStatus', 'MaritalStatus','RecSupervisionLevel', 
                'RecSupervisionLevelText','DisplayText', 'RawScore', 'DecileScore', 'ScoreText',
            'AssessmentType']]
                colonnes = X.select_dtypes(include=["object"]).columns.tolist()




            elif selected_dataset == "Violent Parsed" :
                X =selected_data[["sex","age_cat","race","type_of_assessment","v_type_of_assessment","v_score_text"]]
                colonnes = X.select_dtypes(include=["object"]).columns.tolist()
            
            st.markdown("## Tracé de l'histogramme de chaque colonne catégorielles ")
        # Sélection des colonnes catégorielles
    

        # Calcul du nombre de lignes et de colonnes nécessaires pour afficher les diagrammes en bande
            num_cols = len(colonnes)
            num_rows = (num_cols - 1) // 3 + 1

            # Spécification des couleurs pour chaque catégorie
            colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

            # Tracé du diagramme en bande pour chaque colonne catégorielle
            fig2, axes = plt.subplots(nrows=num_rows, ncols=3, figsize=(15, 6*num_rows))

            for i, col in enumerate(colonnes):
                row_idx = i // 3
                col_idx = i % 3
                ax = axes[row_idx, col_idx]
                counts = X[col].value_counts()
                bars = ax.bar(counts.index, counts, color=colors[:len(counts)])
                ax.set_title(col)
                ax.tick_params(axis='x', rotation=45)
                # Ajout d'une légende pour les couleurs
                if len(counts) > len(colors):
                    ax.legend(bars, counts.index, bbox_to_anchor=(0.2, 1), loc='upper left')

            # Suppression des axes inutiles
            for i in range(num_cols, num_rows*3):
                row_idx = i // 3
                col_idx = i % 3
                fig2.delaxes(axes[row_idx, col_idx])

            # Ajustement des espacements entre les graphiques
            fig2.tight_layout()
            st.pyplot(fig2)


            if selected_dataset=="Compas Scores":
                counts_sex = X['Sex_Code_Text'].value_counts()
                race_ = X['Ethnic_Code_Text']
                Ethnic_Sex_data = ['Ethnic_Code_Text', 'Sex_Code_Text']
                Ethnic_SupervisionLevel =['Ethnic_Code_Text', "ScoreText"]

                Sex_SupervisionLevel =['Sex_Code_Text', "ScoreText"]
                Decil_parEthnies =['Ethnic_Code_Text', "DecileScore"]
                Decil_parSex =['Sex_Code_Text', "DecileScore"]

            elif selected_dataset == "Violent Parsed":
                counts_sex = X['sex'].value_counts()
                race_ = X['race']
                Ethnic_Sex_data = ['race', 'sex']
                Ethnic_SupervisionLevel =['race', "v_score_text"]
                Sex_SupervisionLevel =['sex', "v_score_text"]
                Decil_parEthnies =['race', "decile_score"]
                Decil_parSex =['sex', "decile_score"]


            col1, col2 = st.columns(2)
            categories = counts_sex.index.tolist()
            count_values = counts_sex.values.tolist()
            plt.figure(figsize=(25, 10))
            with col1:
                st.header('Les origines')
                figRace, ax = plt.subplots(figsize=(22, 20))
                # Créer l'histogramme avec Seaborn et spécifier la couleur des barres
                sns.histplot(race_, ax=ax, kde=False, color='steelblue')
                # Afficher l'histogramme
                st.pyplot(figRace)

            

            # Affichage du pie chart dans la deuxième colonne
            with col2:
                st.header('Les sexes')
                figSex, ax = plt.subplots()
                ax.pie(count_values, labels=categories, autopct='%1.1f%%')
                st.pyplot(figSex)
            
            st.markdown("## Les origines par rapport aux sexes")
            Ethnic_Sex, ax = plt.subplots(figsize=(12, 5))
            sns.countplot(data=selected_data, x=Ethnic_Sex_data[0], hue=Ethnic_Sex_data[1])
        
            st.pyplot(Ethnic_Sex)

            col3, col4 = st.columns(2)


            with col3:
                st.markdown('### Les origines par rapport aux niveau de Score')
                figRace, ax = plt.subplots(figsize=(22, 20))
                # Créer l'histogramme avec Seaborn et spécifier la couleur des barres
                sns.countplot(data=selected_data, x=Ethnic_SupervisionLevel[0], hue=Ethnic_SupervisionLevel[1])
                # Afficher l'histogramme
                st.pyplot(figRace)


            # Affichage du pie chart dans la deuxième colonne
            with col4:
                st.markdown('### Les sexes par rapport aux niveau de Score')
                figSex, ax = plt.subplots(figsize=(22, 20))
                sns.countplot(data=selected_data, x=Sex_SupervisionLevel[0], hue=Sex_SupervisionLevel[1])
                st.pyplot(figSex)


            col5, col6 = st.columns(2)


            with col5:
                st.markdown('#### Box plot des decile score par ethnies')
                fig_Decile, ax = plt.subplots(figsize=(20, 15))
                ax.boxplot(
                    [selected_data[selected_data[Decil_parEthnies[0]] == z][Decil_parEthnies[1]] for z in selected_data[Decil_parEthnies[0]].unique()],
                    labels=selected_data[Decil_parEthnies[0]].unique()
                )

                ax.set_xlabel('Ethnie')
                ax.set_ylabel('Decile Score')            
                st.pyplot(fig_Decile)


            # Affichage du pie chart dans la deuxième colonne
            with col6:
                st.markdown('#### Box plot des decile score par sexes (Femme ou homme)')

                fig_Decile, ax = plt.subplots(figsize=(20, 15))
                ax.boxplot([selected_data[selected_data[Decil_parSex[0]] == z][Decil_parSex[1]] for z in selected_data[Decil_parSex[0]].unique()],labels=selected_data[Decil_parSex[0]].unique())

                ax.set_xlabel('Sex')
                ax.set_ylabel('Decile Score')
                    
                st.pyplot(fig_Decile)

            if selected_dataset=="Compas Scores":
                col7, col8 = st.columns(2)
                with col7:
                    st.markdown('### Les origines par rapport aux niveau de Score')
                    figRace, ax = plt.subplots(figsize=(22, 20))
                    # Créer l'histogramme avec Seaborn et spécifier la couleur des barres
                    sns.countplot(data=selected_data, y='Ethnic_Code_Text', hue='LegalStatus')
                    # Afficher l'histogramme
                    st.pyplot(figRace)


                # Affichage du pie chart dans la deuxième colonne
                with col8:
                    st.markdown('### Les origines par rapport aux niveau de Score')
                    figRace, ax = plt.subplots(figsize=(22, 20))
                    # Créer l'histogramme avec Seaborn et spécifier la couleur des barres
                    sns.countplot(data=selected_data, y='Sex_Code_Text', hue='LegalStatus')
                    # Afficher l'histogramme
                    st.pyplot(figRace)

                col9, col10 = st.columns(2)
                with col9:
                    st.markdown('### Les origines par rapport aux Status Légaux')
                    figRace, ax = plt.subplots(figsize=(22, 20))
                    # Créer l'histogramme avec Seaborn et spécifier la couleur des barres
                    sns.countplot(data=selected_data, y='Ethnic_Code_Text', hue='MaritalStatus')
                    # Afficher l'histogramme
                    st.pyplot(figRace)


                # Affichage du pie chart dans la deuxième colonne
                with col10:
                    st.markdown('### Les origines par rapport aux Status Légaux')
                    figRace, ax = plt.subplots(figsize=(22, 20))
                    # Créer l'histogramme avec Seaborn et spécifier la couleur des barres
                    sns.countplot(data=selected_data, y='Sex_Code_Text', hue='MaritalStatus')
                    # Afficher l'histogramme
                    st.pyplot(figRace)
        
             
if __name__ == "__main__":
    data_Viz()
