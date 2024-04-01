import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the diabetes dataset
diabetes_data = pd.read_csv('diabetes.csv')

# Split the data into features and target
X = diabetes_data.drop('Outcome', axis=1)
y = diabetes_data['Outcome']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest classifier
rf_classifier = RandomForestClassifier()
rf_classifier.fit(X_train, y_train)

# Make predictions
def predict_diabetes(input_data):
    prediction = rf_classifier.predict(input_data)
    return prediction

# Create a Streamlit web app
st.title('Diabetic Prediction System')

st.write('Enter the following details to predict if you have diabetes or not:')

# Input fields for user to enter data
pregnancies = st.number_input('Pregnancies', min_value=0, max_value=17, value=1)
glucose = st.number_input('Glucose', min_value=0, max_value=200, value=100)
blood_pressure = st.number_input('Blood Pressure', min_value=0, max_value=122, value=70)
skin_thickness = st.number_input('Skin Thickness', min_value=0, max_value=99, value=20)
insulin = st.number_input('Insulin', min_value=0, max_value=846, value=79)
bmi = st.number_input('BMI', min_value=0.0, max_value=67.1, value=25.0)
dpf = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=2.42, value=0.5)
age = st.number_input('Age', min_value=21, max_value=81, value=30)

# User input data
input_data = [[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]]

# Predict button
if st.button('Predict'):
    prediction = predict_diabetes(input_data)
    if prediction[0] == 0:
        st.write('You are not diabetic.')
    else:
        st.write('You are diabetic.')
