# Shap_and_compas

This GitHub repository contains a project dedicated to the study of the SHAP tool in the context of an educational project on COMPAS data. This application has been developed with the aim of presenting visualizations of different COMPAS project databases and making predictions.

## Context

The project is based on COMPAS data, a dataset used to assess the likelihood of recidivism in criminal defendants. The goal of this project is to analyze the data, preprocess it, build a machine learning model for making recidivism predictions, and create an interactive application using Streamlit to visualize the results.

## Repository Structure

The repository is organized as follows:

- **Notebooks**: This directory contains two notebook files:

  1. **Analysis.ipynb**: This notebook is dedicated to exploratory analysis of COMPAS data. It includes steps such as data import, feature exploration, trend and correlation identification, and generation of visualizations to better understand the data.
  
  2. **Preprocessing_ML.ipynb**: This notebook focuses on data preprocessing, data engineering, building a machine learning model, and evaluating performance. It includes steps such as data manipulation, cleaning, feature selection, train-test split, model training, and result evaluation.

- **Streamlit**: This directory contains the necessary files for the Streamlit application:

  1. **main.py**: This is the main file of the Streamlit application. It contains the code to create the user interface, load the trained model, collect user inputs, perform recidivism predictions, and display the results.
  
  2. **prediction.py**: This file contains the necessary functions to perform recidivism predictions using the trained model. It takes user-provided features and returns an estimation of the recidivism probability.
  
  3. **datavisualization.py**: This file contains functions to generate interactive visualizations from COMPAS data. It uses preprocessed data and provides charts and diagrams to better understand the characteristics of criminal defendants.
  
  4. **model.sav**: This file contains the trained and saved machine learning model. It is loaded by the Streamlit application to perform recidivism predictions.

## Author

This project was developed by AMOS Constant Junior and is available on GitHub.

**Thank you for your interest in our project!**
