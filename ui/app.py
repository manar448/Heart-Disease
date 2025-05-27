import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt

# Load pipeline
pipeline = joblib.load("D:/AI & ML Sprints/models/final_pipeline.pkl")

st.title('Heart Disease Risk Prediction')

# Input fields
st.sidebar.header('Patient Input')
age = st.sidebar.number_input('Age', 20, 100)
trestbps = st.sidebar.number_input('Resting BP', 80, 200)
chol = st.sidebar.number_input('Cholesterol', 100, 600)
cp = st.sidebar.selectbox('Chest Pain Type', [0, 1, 2, 3])
thal = st.sidebar.selectbox('Thalassemia', [0, 1, 2, 3])

# Prediction
if st.sidebar.button('Predict'):
    input_data = pd.DataFrame([[age, trestbps, chol, cp, thal]],
                            columns=['age', 'trestbps', 'chol', 'cp', 'thal'])
    proba = pipeline.predict_proba(input_data)[0][1]
    
    # Display results
    st.subheader(f"Risk Probability: {proba:.1%}")
    st.progress(proba)
    
    # Visualization
    fig, ax = plt.subplots()
    ax.barh(['Low Risk', 'High Risk'], [1-proba, proba], color=['green', 'red'])
    st.pyplot(fig)

# Data Exploration Tab
st.header('Data Trends')
df = pd.read_csv("D:\AI & ML Sprints\data\cleaned_heart_disease.csv")
st.write(df.describe())

# Correlation Heatmap
if st.checkbox('Show Correlation Heatmap'):
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True)
    st.pyplot(plt)