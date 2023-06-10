import joblib
import pandas as pd
import streamlit as st

st.title("Flood Level Prediction")

intensity = st.selectbox( 'What is the intensity value?', ('0', '1', '2','3'))

user_input = pd.DataFrame([[intensity]], columns=["intensity"])

model = joblib.load('model.pkl')
model.built = True

if st.button("Predict"):
	st.write("Flood Probability: ", pred_int,'%')

pd.show_versions()