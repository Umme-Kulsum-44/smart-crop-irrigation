import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model and label encoder
model = joblib.load('C:/Users/dell/OneDrive/Desktop/smart-crop-irrigation/data/processed/rf_model.joblib')
le = joblib.load('C:/Users/dell/OneDrive/Desktop/smart-crop-irrigation/data/processed/label_encoder.joblib')

st.title("🌱 Smart Crop Recommendation")

st.write("Enter soil and weather conditions below:")

# Input sliders
N = st.slider("Nitrogen (N)", 0, 140, 50)
P = st.slider("Phosphorus (P)", 5, 145, 50)
K = st.slider("Potassium (K)", 5, 205, 50)
temperature = st.slider("Temperature (°C)", 8, 45, 25)
humidity = st.slider("Humidity (%)", 10, 100, 50)
ph = st.slider("pH value", 3.0, 9.0, 6.5)
rainfall = st.slider("Rainfall (mm)", 20, 300, 100)

# Prediction
if st.button("Recommend Crop"):
    input_data = pd.DataFrame([[N, P, K, temperature, humidity, ph, rainfall]],
                              columns=['N','P','K','temperature','humidity','ph','rainfall'])
    pred = model.predict(input_data)
    crop = le.inverse_transform(pred)[0]
    st.success(f"Recommended Crop: {crop}")
