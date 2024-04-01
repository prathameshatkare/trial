import streamlit as st

# Title
st.title('Diabetic Prediction System')

# Sidebar
st.sidebar.header('User Input Features')

# Collecting user input features
def user_input_features():
    pregnancies = st.sidebar.slider('Pregnancies', 0, 17, 3)
    glucose = st.sidebar.slider('Glucose', 0, 199, 117)
    blood_pressure = st.sidebar.slider('Blood Pressure', 0, 122, 72)
    skin_thickness = st.sidebar.slider('Skin Thickness', 0, 99, 23)
    insulin = st.sidebar.slider('Insulin', 0, 846, 30)
    bmi = st.sidebar.slider('BMI', 0.0, 67.1, 32.0)
    dpf = st.sidebar.slider('Diabetes Pedigree Function', 0.078, 2.42, 0.372)
    age = st.sidebar.slider('Age', 21, 81, 29)

    features = {
        'Pregnancies': pregnancies,
        'Glucose': glucose,
        'Blood Pressure': blood_pressure,
        'Skin Thickness': skin_thickness,
        'Insulin': insulin,
        'BMI': bmi,
        'Diabetes Pedigree Function': dpf,
        'Age': age
    }
    return features

# Display user input features
user_input = user_input_features()
st.write('User Input Features:')
st.write(user_input)
