# -*- coding: utf-8 -*-
"""
Created on Sun Oct  5 15:56:21 2025

@author: NEHAL
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Loading the saved models

diabetes_model = pickle.load(open('trained_model_diabetic.sav','rb'))

heart_model = pickle.load(open('trained_model_heart.sav','rb'))

breast_model = pickle.load(open('trained_model_breast.sav','rb'))


# creating the side bar

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction','Heart Disease Prediction','Breast Cancer Prediction'],
                           icons = ['activity','heart','person'],
                           default_index=0)
    

# diabetes prediction page

if(selected == 'Diabetes Prediction'):
    
    st.title('Diabetes Prediction System')
    
    
    # getting input data from user
    # creating coulumns
    col1,col2,col3 = st.columns(3)
    
    with col1:
        Pregnancies   = st.text_input('Number of pregnancies')
    
    with col2:
        Glucose = st.text_input('Glucose level')  
        
    with col3:
        BMI           = st.text_input('BMI value')
        
    with col1:
        SkinThickness = st.text_input('Skin thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin level')
    
    with col3:
        BloodPressure = st.text_input('Blood pressure level')
    
    with col1:
        DiabetesPedigreeFunction  = st.text_input('Diabetes Pedigree Function')
    
    with col2:
        Age     = st.text_input('Age of the person')
        
        
        
        
    # code for prediction
    
    diab_diagnosis = ''
    
    # creating button for prediction system
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        
        if diab_prediction[0] == 1:
                diab_diagnosis = 'The person is likely to have diabetes.'
        else:
                diab_diagnosis = 'The person is not likely to have diabetes.'
    
    st.success(diab_diagnosis)

# heart prediction page

if selected == 'Heart Disease Prediction':
    
    st.title('Heart Disease Prediction System')
    
    # Creating columns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age      = st.text_input('Age')
    
    with col2:
        sex      = st.text_input('Sex (1 = male, 0 = female)')
    
    with col3:
        cp       = st.text_input('Chest Pain Type (0–3)')
    
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    
    with col2:
        chol     = st.text_input('Serum Cholesterol (mg/dl)')
    
    with col3:
        fbs      = st.text_input('Fasting Blood Sugar > 120 mg/dl (1 = true, 0 = false)')
    
    with col1:
        restecg  = st.text_input('Resting ECG results (0–2)')
    
    with col2:
        thalach  = st.text_input('Maximum Heart Rate Achieved')
    
    with col3:
        exang    = st.text_input('Exercise Induced Angina (1 = yes, 0 = no)')
    
    with col1:
        oldpeak  = st.text_input('Oldpeak (ST depression induced by exercise)')
    
    with col2:
        slope    = st.text_input('Slope of peak exercise ST segment (0–2)')
    
    with col3:
        ca       = st.text_input('Number of major vessels (0–3) colored by fluoroscopy')
    
    with col1:
        thal     = st.text_input('Thalassemia (1 = normal; 2 = fixed defect; 3 = reversible defect)')
        
    heart_diagnosis = ''
    
    # creating button for prediction system
    if st.button('Heart Test Result'):
        heart_prediction = diabetes_model.predict([[sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        
        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is likely to have diabetes.'
        else:
            heart_diagnosis = 'The person is not likely to have diabetes.'
    
    st.success(heart_diagnosis)
    
    
# breast cancer prediction page

if selected == 'Breast Cancer Prediction':
    
    st.title('Breast Cancer Prediction System')
    
    # Create a layout with 3 columns for better organization
    col1, col2, col3 = st.columns(3)

    # Use a dictionary to store the input fields for easier management
    # and to ensure correct order
    features = {}

    # Column 1
    with col1:
        features['mean radius'] = st.text_input('Mean Radius')
        features['mean concavity'] = st.text_input('Mean Concavity')
        features['mean symmetry'] = st.text_input('Mean Symmetry')
        features['radius error'] = st.text_input('Radius Error')
        features['perimeter error'] = st.text_input('Perimeter Error')
        features['concavity error'] = st.text_input('Concavity Error')
        features['symmetry error'] = st.text_input('Symmetry Error')
        features['worst radius'] = st.text_input('Worst Radius')
        features['worst perimeter'] = st.text_input('Worst Perimeter')
        features['worst concavity'] = st.text_input('Worst Concavity')

    # Column 2
    with col2:
        features['mean texture'] = st.text_input('Mean Texture')
        features['mean concave points'] = st.text_input('Mean Concave Points')
        features['mean fractal dimension'] = st.text_input('Mean Fractal Dimension')
        features['texture error'] = st.text_input('Texture Error')
        features['area error'] = st.text_input('Area Error')
        features['concave points error'] = st.text_input('Concave Points Error')
        features['fractal dimension error'] = st.text_input('Fractal Dimension Error')
        features['worst texture'] = st.text_input('Worst Texture')
        features['worst area'] = st.text_input('Worst Area')
        features['worst concave points'] = st.text_input('Worst Concave Points')

    # Column 3
    with col3:
        features['mean perimeter'] = st.text_input('Mean Perimeter')
        features['mean area'] = st.text_input('Mean Area')
        features['mean smoothness'] = st.text_input('Mean Smoothness')
        features['mean compactness'] = st.text_input('Mean Compactness')
        features['smoothness error'] = st.text_input('Smoothness Error')
        features['compactness error'] = st.text_input('Compactness Error')
        features['worst smoothness'] = st.text_input('Worst Smoothness')
        features['worst compactness'] = st.text_input('Worst Compactness')
        features['worst symmetry'] = st.text_input('Worst Symmetry')
        features['worst fractal dimension'] = st.text_input('Worst Fractal Dimension')
    
    cancer_diagnosis = ''
    
    # creating button for prediction
    if st.button('Cancer Test Result'):
        # Convert the dictionary values to a list in the correct order for the model
        input_data = [float(features[key]) for key in features]
        
        cancer_prediction = cancer_model.predict([input_data])
        
        if cancer_prediction[0] == 1:
            cancer_diagnosis = 'The tumor is likely malignant.'
        else:
            cancer_diagnosis = 'The tumor is likely benign.'
    
    st.success(cancer_diagnosis)
    
    
    
    