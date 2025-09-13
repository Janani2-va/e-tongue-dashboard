



import streamlit as st
import joblib


# Load trained model
model = joblib.load("e_tongue_model.pkl")



st.title("🌿 E-Tongue Dravya Identification Dashboard")

st.write("Enter sensor readings below:")

# Input fields
pH = st.number_input("pH", min_value=0.0, max_value=14.0, step=0.1)
orp = st.number_input("ORP (mV)", min_value=-500, max_value=1000, step=1)
cond = st.number_input("Conductivity (µS/cm)", min_value=0, max_value=10000, step=10)
metal = st.number_input("Metal Electrode (V)", min_value=0.0, max_value=5.0, step=0.01)

if st.button("🔮 Predict Dravya"):
    new_sample = [[pH, orp, cond, metal]]
    prediction = model.predict(new_sample)

    st.success(f"✅ Predicted Dravya: *{prediction[0]}*")

