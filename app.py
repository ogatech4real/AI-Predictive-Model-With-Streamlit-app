import streamlit as st
import pandas as pd
from joblib import load

model = load('energy_predictor.joblib')

st.title("Energy Consumption Predictor")

proc_temp = st.number_input("Enter Process Temperature (°C):", 0.0, 200.0)
env_temp = st.number_input("Enter Environmental Temperature (°C):", -20.0, 60.0)

if st.button("Predict Energy Consumption"):
    input_df = pd.DataFrame([[proc_temp, env_temp]], columns=['ProcTemp', 'EnvTemp'])
    prediction = model.predict(input_df)[0]
    st.success(f"Estimated Energy Consumption: {prediction:.4f} units")
