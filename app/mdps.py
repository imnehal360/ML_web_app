# -*- coding: utf-8 -*-
"""
Created on Sun Oct  5 15:56:21 2025

@author: NEHAL
"""
import sys
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from chatbot import get_gemini_response

# --- Loading Models ---
try:
    diabetes_model = pickle.load(open('C:/Users/NEHAL/Desktop/MDPS/ML_web_app/app/trained_model_diabetic.sav', 'rb'))
    heart_model = pickle.load(open('C:/Users/NEHAL/Desktop/MDPS/ML_web_app/app/trained_model_heart.sav', 'rb'))
    breast_model = pickle.load(open('C:/Users/NEHAL/Desktop/MDPS/ML_web_app/app/trained_model_breast.sav', 'rb'))
except FileNotFoundError as e:
    st.error(f"Model file not found. Please ensure the model files are in the 'app' directory. Error: {e}")
    st.stop()

# --- Main App Logic ---
with st.sidebar:
    selected = option_menu(
        'Multiple Disease Prediction',
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Breast Cancer Prediction', 'AI Medical Assistant'],
        icons=['activity', 'heart', 'person', 'robot'], default_index=0
    )

# --- Render Prediction Pages ---
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction System')
    col1,col2,col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of pregnancies')
    with col2:
        Glucose = st.text_input('Glucose level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        SkinThickness = st.text_input('Skin thickness value')
    with col2:
        Insulin = st.text_input('Insulin level')
    with col3:
        BloodPressure = st.text_input('Blood pressure level')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function')
    with col2:
        Age = st.text_input('Age of the person')

    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        # Correctly format input data as a list of numbers
        input_data = [float(Pregnancies), float(Glucose), float(BloodPressure), float(SkinThickness), float(Insulin), float(BMI), float(DiabetesPedigreeFunction), float(Age)]
        diab_prediction = diabetes_model.predict([input_data])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is likely to have diabetes.'
        else:
            diab_diagnosis = 'The person is not likely to have diabetes.'

    st.success(diab_diagnosis)

if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction System')
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex (1 = male, 0 = female)')
    with col3:
        cp = st.text_input('Chest Pain Type (0–3)')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholesterol (mg/dl)')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl (1 = true, 0 = false)')
    with col1:
        restecg = st.text_input('Resting ECG results (0–2)')
    with col2:
        thalach = st.text_input('Maximum Heart Rate Achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina (1 = yes, 0 = no)')
    with col1:
        oldpeak = st.text_input('Oldpeak (ST depression induced by exercise)')
    with col2:
        slope = st.text_input('Slope of peak exercise ST segment (0–2)')
    with col3:
        ca = st.text_input('Number of major vessels (0–3) colored by fluoroscopy')
    with col1:
        thal = st.text_input('Thalassemia (1 = normal; 2 = fixed defect; 3 = reversible defect)')

    heart_diagnosis = ''
    if st.button('Heart Test Result'):
        # Using the correct model (heart_model) and corrected input list
        input_data = [float(age), float(sex), float(cp), float(trestbps), float(chol), float(fbs), float(restecg), float(thalach), float(exang), float(oldpeak), float(slope), float(ca), float(thal)]
        heart_prediction = heart_model.predict([input_data])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is likely to have heart disease.'
        else:
            heart_diagnosis = 'The person is not likely to have heart disease.'

    st.success(heart_diagnosis)

if selected == 'Breast Cancer Prediction':
    st.title('Breast Cancer Prediction System')
    col1, col2, col3 = st.columns(3)
    features = {}

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
    if st.button('Cancer Test Result'):
        input_data = [float(features[key]) for key in features]
        cancer_prediction = breast_model.predict([input_data])

        if cancer_prediction[0] == 1:
            cancer_diagnosis = 'The tumor is likely malignant.'
        else:
            cancer_diagnosis = 'The tumor is likely benign.'

    st.success(cancer_diagnosis)

if selected == 'AI Medical Assistant':
    st.title("CareBot")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("What is up?"):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        response = get_gemini_response(prompt)
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})