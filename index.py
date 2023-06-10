from tensorflow.keras.models import load_model
import pandas as pd
import streamlit as st

st.title("Flood Level Prediction")

intensity = st.selectbox( 'RAIN INTENSITY (0 for None, 1 for Light, 2 for Moderate, 3 for Heavy)', ('0', '1', '2','3'))

user_input = pd.DataFrame([[intensity]], columns=["intensity"])

model = load_model('model.h5')
model.built = True

if st.button("Predict"):
	st.write("Flood Probability: ", pred_int,'%')

pd.show_versions()