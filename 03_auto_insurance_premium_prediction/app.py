import streamlit as st

def predict_auto_insurance_premium(age, accident_history):
    return -9.95088805 * age + 499.18950284 * accident_history + 1997.9182518985917

st.title("🚗 Auto Insurance Premium Predictor")

st.markdown("""Estimate your **annual auto insurance premium** based on your **age** and **accident history**""")

age = st.number_input("Driver Age", min_value=16, max_value=100, value=30, step=1)

accident_option = st.selectbox("Had an Accident in the Past 2 Years?", ["yes", "no"])
accident_history = 1 if accident_option == "yes" else 0

if st.button("Predict Premium"):
    predicted_premium = predict_auto_insurance_premium(age, accident_history)
    st.success(f"💵 Estimated Annual Premium: **${predicted_premium:.2f}**")
