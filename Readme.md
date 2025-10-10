
Multiple Disease Prediction System
This project is a web-based application built with Streamlit that serves as a Multiple Disease Prediction System. It uses machine learning models to predict the likelihood of three common diseases: Diabetes, Heart Disease, and Breast Cancer. The application provides a simple and intuitive user interface to input various health parameters and receive an instant prediction.

Features
Diabetes Prediction: Predicts the likelihood of diabetes based on key health metrics. The model uses the following parameters:

Pregnancies

Glucose

Blood Pressure

Skin Thickness

Insulin

BMI

Diabetes Pedigree Function

Age

Heart Disease Prediction: Predicts the risk of heart disease by analyzing a set of clinical parameters. The model uses the following parameters:

age

sex

cp (chest pain type)

trestbps (resting blood pressure)

chol (serum cholesterol)

fbs (fasting blood sugar)

restecg (resting electrocardiographic results)

thalach (maximum heart rate achieved)

exang (exercise-induced angina)

oldpeak (ST depression induced by exercise)

slope (the slope of the peak exercise ST segment)

ca (number of major vessels colored by fluoroscopy)

thal (Thalassemia)

Breast Cancer Prediction: Predicts whether a tumor is malignant or benign based on various cellular features. The model uses 30 parameters, including:

mean radius

mean texture

mean perimeter

mean area

...and many more.

How it Works
The application loads pre-trained machine learning models saved as .sav files. When a user enters their health data and clicks the "Test Result" button, the application takes these inputs, feeds them into the respective model, and displays the predicted outcome.

Technology Stack
Python: The core programming language.

Streamlit: For building the interactive web application interface.

scikit-learn: The machine learning library used to create the prediction models.

Numpy: For numerical operations and handling array-like data.

pickle-mixin: Used to serialize and deserialize the trained models.

streamlit-option-menu: A custom component for creating the navigation sidebar.

Installation and Setup
Clone the Repository:

Bash

git clone <repository_url>
Navigate to the project directory:

Bash

cd <project_directory>
Install the required libraries:
The dependencies are listed in requirements.txt.

Bash

pip install -r requirements.txt
Usage
To run the application, execute the following command in your terminal:

Bash

streamlit run mdps.py
The application will open in your web browser, and you can start using the prediction system.

Disclaimer
This tool is intended for informational and educational purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of a qualified health provider with any questions you may have regarding a medical condition.