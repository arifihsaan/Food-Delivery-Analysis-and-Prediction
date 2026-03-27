import streamlit as st
import joblib
import numpy as np
import pandas as pd

# load model
model = joblib.load('model_delivery_time_prediction.pkl')

st.title("Delivery Tme  Prediction")

st.write("Enter the delivery data")

# Input feature
Distance_km = st.number_input("Distance (in Km)", 0)
Weather = st.selectbox("Weather", ['Clear', 'Rainy', 'Foggy', 'Snowy', 'Windy'])
Traffic_Level = st.selectbox("Traffic Level", ['Low', 'Medium', 'High'])
Time_of_Day = st.selectbox("Time of Day", ['Morning', 'Afternoon', 'Evening', 'Night'])
Vehicle_Type = st.selectbox("Vehicle Type", ['Bike', 'Scooter', 'Car'])
Preparation_Time_min = st.number_input("Preparation Time (in minutes)", 0)
Courier_Experience_yrs = st.number_input("Courier Experience (in years)", 0)



input_data = pd.DataFrame({
    "Distance_km":[Distance_km],
    "Weather":[Weather],
    "Traffic_Level":[Traffic_Level],
    "Time_of_Day":[Time_of_Day],
    "Vehicle_Type":[Vehicle_Type],
    "Preparation_Time_min":[Preparation_Time_min],
    "Courier_Experience_yrs":[Courier_Experience_yrs],
})

# tombol prediksi
if st.button("Predict Delivery Time"):
    
    prediction = model.predict(input_data)

    st.success(f"Predicted Delivery Time: {prediction[0]:.2f} minutes")