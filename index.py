from tensorflow.keras.models import load_model
import pandas as pd
import streamlit as st
import requests

st.title("Flood Level Prediction")

intensity = st.selectbox( 'RAIN INTENSITY (0 for None, 1 for Light, 2 for Moderate, 3 for Heavy)', ('0', '1', '2','3'))

# user_input = pd.DataFrame([[intensity]], columns=["intensity"])
user_input = float(intensity)

model = load_model('model.h5')
model.built = True

def func_level():
    url = ('https://api.thingspeak.com/channels/2135773/feeds.json?api_key=5ISF03WS3CO2HYSD&results=2')
    print(url)
    response = requests.get(url)
    print(f"Request returned {response.status_code} : '{response.reason}'")
    msg=requests.get(url)
    msg=msg.json()['feeds'][-1]['field2']
    print("Last updated water level: \n\n"+str(msg))
    level = float(msg)
    return level

def func_predict():
    func_level()
    prediction =  [func_level(), user_input]
    pred = model.predict([prediction])
    pred_int = int(pred*100)
    return pred_int

if st.button("Predict"): 
    st.write("Current water level: ", func_level())  
    st.write("Flood Probability: ", func_predict(),'%')
    
pd.show_versions()

