import serial
import streamlit as st
import joblib

# Load trained model
model = joblib.load("e_tongue_model.pkl")

# Connect to Arduino (your Uno is on COM6)
ser = serial.Serial('COM6', 9600, timeout=1)

st.title("🌿 E-Tongue Dravya Identification Dashboard")

if st.button("📡 Get Live Sensor Data"):
    line = ser.readline().decode().strip()
    if line:
        try:
            # Expecting: pH,ORP,Cond,Metal
            pH, orp, cond, metal = map(float, line.split(","))
            st.write(f"📊 Sensor Data → pH: {pH}, ORP: {orp}, Cond: {cond}, Metal: {metal}")

            new_sample = [[pH, orp, cond, metal]]
            prediction = model.predict(new_sample)
            st.success(f"✅ Predicted Dravya: **{prediction[0]}**")
        except:
            st.error("⚠️ Invalid data format from Arduino")
