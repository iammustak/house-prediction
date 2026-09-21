
import streamlit as st
import pickle
import json
import numpy as np

# Load model
with open("bangalore_home_prices_model.pickle", "rb") as f:
    model = pickle.load(f)

with open("columns.json", "r") as f:
    columns = json.load(f)


# Page
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠"
)

st.title("🏠 Bangalore House Price Prediction")
st.write("Enter property details to predict the price.")

# Inputs
bhk = st.number_input("BHK", 1, 10, 2)

sqft = st.number_input(
    "Total Square Feet",
    300.0,
    10000.0,
    1000.0
)

balcony = st.number_input(
    "Balcony",
    0,
    5,
    1
)

locations = [
    col.replace("location_", "")
    for col in columns
    if col.startswith("location_")
]

location = st.selectbox(
    "Location",
    locations
)


# Prediction
if st.button("Predict Price"):

    x = np.zeros(len(columns))

    x[columns.index("bhk")] = bhk
    x[columns.index("total_sqft")] = sqft
    x[columns.index("balcony")] = balcony

    location_column = "location_" + location

    if location_column in columns:
        x[columns.index(location_column)] = 1

    price = model.predict([x])[0]

    st.success(
        f"🏠 Estimated Price: ₹ {price:.2f} Lakhs"
    )
