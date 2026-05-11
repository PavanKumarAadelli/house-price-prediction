import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load('house_price_model.pkl')

st.title("🏠 Bengaluru House Price Predictor")
st.write("This app predicts the price of a house in Bengaluru based on its features.")

st.sidebar.header("Input Features")

location = st.sidebar.text_input("Location", "Whitefield")

# Area Type
area_type = st.sidebar.selectbox("Area Type", ("Super built-up  Area", "Plot  Area", "Built-up  Area", "Carpet  Area"))

# Numerical Features
total_sqft = st.sidebar.number_input("Total Sqft", min_value=300, max_value=10000, value=1200)
bath = st.sidebar.number_input("Bathrooms", min_value=1, max_value=20, value=2)
balcony = st.sidebar.number_input("Balconies", min_value=0, max_value=5, value=1)
bhk = st.sidebar.number_input("BHK (Bedrooms)", min_value=1, max_value=20, value=2)

# 4. Prepare Data for Prediction

def get_location_hash(loc):
    return hash(loc) % 1000

input_data = {
    'total_sqft_log': np.log1p(total_sqft), # Apply Log Transformation
    'bath': bath,
    'bhk': bhk,
    'location_encoded': get_location_hash(location)
}

area_types = ["Plot  Area", "Built-up  Area", "Carpet  Area"] # Assuming Super built-up is dropped (drop_first=True)
for at in area_types:
    input_data[f'area_type_{at}'] = 0

if area_type in area_types:
    input_data[f'area_type_{area_type}'] = 1

input_df = pd.DataFrame([input_data])


# 5. Prediction
if st.button("Predict Price"):
    prediction_log = model.predict(input_df)

    prediction_price = np.expm1(prediction_log)[0]

    st.success(f"Predicted Price: {prediction_price:.2f} Lakhs")
    st.info(f"Approx. ₹ {prediction_price * 100000:.0f}")

